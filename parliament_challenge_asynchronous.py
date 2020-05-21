import asyncio
import requests_async as requests

from quart import Quart, request, json
from hypercorn.config import Config
from hypercorn.asyncio import serve


def create_app():
    app = Quart("Parliament Challenge")

    @app.route('/latest-speeches/', methods=['GET'])
    async def get_latest_speeches():
        """
        GET request:
            curl -X GET "http://127.0.0.1:8080/latest-speeches/?anftyp=Nej&sz=10"
        """
        """
        Clients can input the number of speeches required by them.
        Result will be a merged data of speeches with members. 
        """
        anftyp = request.args["anftyp"]
        size = request.args["sz"]
        speeches = await get_speeches(anftyp, size)
        return json.dumps(speeches)
    return app


async def get_speeches(anftyp, size):
    """
    Get speeches data from speech's api
    and filter for relevant keys.
    For each speech we query the member api 
    to get the member data and 
    then merge it with the speech data.
    """

    domain = 'http://data.riksdagen.se'
    speeches = 'anforandelista'
    format_type = 'json'
    response = await requests.get('{}/{}/?anftyp={}&sz={}&utformat={}'.format(domain, speeches, anftyp, size, format_type))
    if response.status_code == 200:
        data = response.json()
        # When a server responds with more than one speech.
        if data["anforandelista"]["@antal"] > "1":
            speeches = data["anforandelista"]["anforande"]
            filtered_speeches = filter_speeches_dict(speeches)
            tasks = []
            loop = asyncio.get_event_loop()
            for speech in filtered_speeches:
                task = loop.create_task(merge_speech_with_member_data(speech))
                tasks.append(task)
            await asyncio.wait(tasks)
            merged_speeches = [t.result() for t in tasks]
            return merged_speeches
        # When a server responds only with one speech.
        # A dict is returned and to handle this, the dict is stored 
        # in a list because the filter_speeches_dict accepts a list.
        elif data["anforandelista"]["@antal"] == "1":
            speeches = [
                data["anforandelista"]["anforande"]
            ]
            filtered_speech = filter_speeches_dict(speeches)[0]
            member_data = await get_member_data(filtered_speech["intressent_id"])
            filtered_speech.update(member_data)
            return filtered_speech
    else:
        return [], response.status_code


def filter_speeches_dict(speeches):
    """
    Filtering speeches data for relevant keys.
    Relevant keys are anforande_id, dok_datum,
    parti, avsnittsrubrik, links and intressent_id.
    """

    speeches_list = []
    for s in speeches:
        speechesDict = {
                "anforande_id": s.get("anforande_id"),
                "dok_datum": s.get("dok_datum"),
                "parti": s.get("parti"), 
                "avsnittsrubrik": s.get("avsnittsrubrik"),
                "links": [{ 
                    "rel": "speech",
                    "href": s.get("protokoll_url_www")
                    }],
                "intressent_id": s.get("intressent_id")
                }
        speeches_list.append(speechesDict)
    return speeches_list


async def merge_speech_with_member_data(speech):
    """
    Merge the speech data with member data.    
    """

    member_data = await get_member_data(speech["intressent_id"])
    speech.update(member_data)
    return speech


async def get_member_data(intressent_id):
    """
    Get a member data from the member's api
    and filter for relevant keys.
    """

    domain = 'http://data.riksdagen.se'
    members = 'personlista'
    format_type = 'json'
    response = await requests.get('{}/{}/?iid={}&utformat={}'.format(domain, members, intressent_id, format_type))
    if response.status_code == 200:
        data = response.json()
        # One member data being returned at a time.
        if data["personlista"]["@hits"] == "1":
            member = data["personlista"]["person"]
            filtered_member = filter_member_dict(member)
            return filtered_member
        # In case a member detail is non-existent,
        # returning an empty dict to indicate that 
        # the detail does not exist in the member data.
        elif data["personlista"]["@hits"] == "0":
            return {}, response.status_code
    else:
        return {}, response.status_code


def filter_member_dict(member):
    """
    Filtering member data for relevant keys.
    Relevant keys are tilltalsnamn, valkrets,
    bild_url_192, uppgift and intressent_id.
    """

    if member["personuppgift"] is None:
        email = None
    else:
        for e in member["personuppgift"]["uppgift"]:
            if e["kod"] == "Officiell e-postadress":
                uppgift = e["uppgift"]
                email = uppgift[0]

    membersDict = {
        "tilltalsnamn": member.get("tilltalsnamn"),
        "valkrets": member.get("valkrets"),
        "uppgift": email,
        "bild_url_192": member.get("bild_url_192"),
        "intressent_id": member.get("intressent_id")
    }
    return membersDict


def main():
    loop = asyncio.get_event_loop()
    app = create_app()
    config = Config()
    config.bind = ["localhost:8080"]
    loop.run_until_complete(serve(app, config))


if __name__ == "__main__":
    main()