import requests
import waitress
import flask
from flask import Flask, request, json


not_found = {"message": "Not Found"}
failed = {"message": "Failed"}


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


def filter_member_dict(member):
    """
    Filtering member data for relevant keys.
    Relevant keys are tilltalsnamn, valkrets,
    bild_url_192, uppgift and intressent_id.
    """

    if member["personuppgift"] is None:
        email = "null"
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


def get_member_data(intressent_id):
    """
    Get a member data from the member's api
    and filter for relevant keys.
    """

    domain = 'http://data.riksdagen.se'
    members = 'personlista'
    format_type = 'json'
    response = requests.get('{}/{}/?iid={}&utformat={}'.format(domain, members, intressent_id, format_type))
    if response.status_code == 200:
        data = response.json()
        if data["personlista"]["@hits"] == "1":
            member = data["personlista"]["person"]
            filtered_member = filter_member_dict(member)
            return filtered_member, response.status_code
        elif data["personlista"]["@hits"] == "0":
            nullMemberDict = {}
            return nullMemberDict, response.status_code
    else:
        return {}, response.status_code


def get_speeches_data(anftyp, size):
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
    response = requests.get('{}/{}/?anftyp={}&sz={}&utformat={}'.format(domain, speeches, anftyp, size, format_type))
    if response.status_code == 200:
        data = response.json()
        speeches = data["anforandelista"]["anforande"]
        filtered_speeches = filter_speeches_dict(speeches)
        for speech in filtered_speeches:
            member_data, code = get_member_data(speech["intressent_id"])        
            speech.update(member_data)
        return filtered_speeches, code
    else:
        return [], response.status_code
        

def create_app():
    app = Flask("Parliament Challenge")

    @app.route('/latest-speeches/', methods=['GET'])
    def get_latest_speeches():
        """
        GET request:
            curl -X GET "localhost:8080/latest-speeches/?anftyp=Nej&sz=2"
        """
        """
        Clients can input the number of speeches required by them.
        Result will be a merged data of speeches with members. 
        """
        anftyp = flask.request.args["anftyp"]
        size = flask.request.args["sz"]
        speeches, code = get_speeches_data(anftyp, size)
        print(speeches)
        return json.dumps(speeches), code
    return app


def main():
    app = create_app()
    waitress.serve(app, host='0.0.0.0', port=8080)


if __name__ == "__main__":
    main()