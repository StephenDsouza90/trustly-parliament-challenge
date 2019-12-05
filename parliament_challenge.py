import requests
import waitress
import flask
from flask import Flask, request, json


def get_speeches_api():
    """
    Use speech's api to get speech resources.
    Speech's api gets latest speeches and size determines how many resources to get.
    Loop through dict to return all values in the "anforande" key.
    These values include the keys and values of the speeches.
    """

    domain = 'http://data.riksdagen.se'
    speeches = 'anforandelista'
    size = 6
    format_type = 'json'
    response = requests.get('{}/{}/?anftyp=Nej&sz={}&utformat={}'.format(domain, speeches, size, format_type))
    if response.status_code == 200:
        data = response.json()
        for k, v in data.items():
            anforande = v["anforande"]
            return anforande


def create_speeches_dict():
    """
    Use the get_speeches_api() function to create a dict of the relevant items.
    """

    speeches_data = get_speeches_api()
    speeches_list = []
    for speeches in speeches_data:
        anforande_id = [v for k, v in speeches.items() if k == "anforande_id"]
        dok_datum = [v for k, v in speeches.items() if k == "dok_datum"]
        parti = [v for k, v in speeches.items() if k == "parti"]
        avsnittsrubrik = [v for k, v in speeches.items() if k == "avsnittsrubrik"]
        protokoll_url_www = [v for k, v in speeches.items() if k == "protokoll_url_www"]
        intressent_id = [v for k, v in speeches.items() if k == "intressent_id"]
        speechesDict = {
            "anforande_id": anforande_id[0],
            "dok_datum": dok_datum[0],
            "parti": parti[0], 
            "avsnittsrubrik": avsnittsrubrik[0],
            "protokoll_url_www": protokoll_url_www[0], 
            "intressent_id": intressent_id[0]
            }
        speeches_list.append(speechesDict)
    return speeches_list


def create_speeches_reference_list():
    """
    Create a reference list from create_speeches_dict()
    so that the reference value can be used in the member's
    api to filter to the relevant member's data. 
    """

    speeches_data = create_speeches_dict()
    reference_list = []
    for reference in speeches_data:
        ref = reference["intressent_id"]
        reference_list.append(ref)
    return reference_list


def get_members_api():
    """
    Use member's api to get member resources.
    Member's api uses reference id from create_speeches_reference_list() 
    to filter to the relevant member's data.
    Loop through dict to return all values in the "person" key.
    These values include the keys and values of the members.
    """

    reference = create_speeches_reference_list()    
    members_list = []
    for ref in reference:
        domain = 'http://data.riksdagen.se'
        members = 'personlista'
        reference = ref
        format_type = 'json'
        response = requests.get('{}/{}/?iid={}&utformat={}'.format(domain, members, reference, format_type))
        if response.status_code == 200:
            data = response.json()
            for k, v in data.items():
                person = v["person"]
                members_list.append(person)
    return members_list


def create_members_dict():
    """
    Use the get_members_api() function to create a dict of the relevant items.
    """

    members_data = get_members_api()
    members_list = []
    for members in members_data:
        tilltalsnamn = [v for k, v in members.items() if k == "tilltalsnamn"]
        valkrets = [v for k, v in members.items() if k == "valkrets"]
        bild_url_192 = [v for k, v in members.items() if k == "bild_url_192"]
        intressent_id = [v for k, v in members.items() if k == "intressent_id"]
        membersDict = {
            "tilltalsnamn": tilltalsnamn[0],
            "valkrets": valkrets[0],
            "bild_url_192": bild_url_192[0],
            "intressent_id": intressent_id[0]
            }
        members_list.append(membersDict)
    return members_list


def create_app():
    """
    Create app
    """
    app = Flask("Parliament Challenge")

    @app.route('/ten-latest-speeches', methods=['GET'])
    def get_ten_latest_speeches():
        """
        GET request:
            >> curl -X GET "localhost:8080/ten-latest-speeches"
        """
        """
        Merger function: 
        Loop through the create_speeches_dict() which contains 
        the ten latest speeches with the relevant items.
        Loop through the create_members_dict() which that contians
        the relevant items of the members.
        Merge relevant speeches data to members data if reference key 
        "intressent_id" from speeches matches members.
        """
    
        speeches = create_speeches_dict()
        members = create_members_dict()        
        ten_latest_speeches = []
        for s in speeches:
            for m in members:
                if s["intressent_id"] == m["intressent_id"]:
                    s.update(m)
                    ten_latest_speeches.append(s)
        print(ten_latest_speeches)
        return json.dumps(ten_latest_speeches)
    return app


def main():
    app = create_app()
    waitress.serve(app, host='0.0.0.0', port=8080)


if __name__ == "__main__":
    main()