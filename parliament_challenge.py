import requests
import waitress
import flask
from flask import Flask, request, json


def get_speeches():
    """
    Use speech's api to get all speech resources.
    Speech api uses filter to get ten latest speeches.
    Loop through nested dict to return all items in the "anforande" key.
    """    

    domain = 'http://data.riksdagen.se'
    speeches = 'anforandelista'
    size = 10
    format_type = 'json'
    response = requests.get('{}/{}/?anftyp=Nej&sz={}&utformat={}'.format(domain, speeches, size, format_type))

    if response.status_code == 200:
        data = response.json()
        for k, v in data.items():
            anforande = v["anforande"]
            return anforande


def get_members():
    """
    Use member's api to get all member resources.
    Loop through nested dict to return all items in the "person" key.
    """    
    domain = 'http://data.riksdagen.se'
    members = 'personlista'
    format_type = 'json'
    response = requests.get('{}/{}/?iid=&fnamn=&enamn=&f_ar=&kn=&parti=&valkrets=&rdlstatus=&org=&utformat={}&sort=sorteringsnamn&sortorder=asc&termlista='.format(domain, members, format_type))

    if response.status_code == 200:
        data = response.json()
        for k, v in data.items():
            person = v["person"]
            return person


def create_speeches_dict():
    """
    Call the get_speeches function and create a dict of the relevant items.
    """

    speeches_data = get_speeches()

    relevant_speeches = []
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
        relevant_speeches.append(speechesDict)
    return relevant_speeches


def create_members_dict():
    """
    Call the get_members function and create a dict of the relevant items.
    Returning all member details. 
    """

    members_data = get_members()

    all_members = []
    for members in members_data:
        tilltalsnamn = [v for k, v in members.items() if k =="tilltalsnamn"]
        valkrets = [v for k, v in members.items() if k == "valkrets"]
        bild_url_192 = [v for k, v in members.items() if k == "bild_url_192"]
        intressent_id = [v for k, v in members.items() if k == "intressent_id"]

        membersDict = {
            "tilltalsnamn": tilltalsnamn[0],
            "valkrets": valkrets[0],
            "bild_url_192": bild_url_192[0],
            "intressent_id": intressent_id[0]
            }
        all_members.append(membersDict)
    return all_members


def get_relevant_members():
    """
    To get only relevant member details based on the speeches data,
    match member details to speeches data through a key/value 
    that matches in both data sets.
    Here the key "intressent_id" and its value is common in both data sets.
    Call both dicts that have been created in the create_speeches_dict 
    and create_members_dict function.
    Match the intressent_id in speeches data with intressent_id in members data
    """

    speeches_data = create_speeches_dict()
    members_data = create_members_dict()

    speeches_fk = [fk['intressent_id'] for fk in speeches_data]
    members_fk = [fk for fk in members_data if fk['intressent_id'] in speeches_fk]
    return members_fk


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
        Call the create_speeches_dict that holds the ten latest speeches
        with the relevant items.
        Call the get_relevant_members function that holds the relevant
        items of the members.
        Loop through both data sets to match the "intressent_id" and 
        merge the dict if match. 
        If the "ten_latest_speeches_dup.append(s)" is indented with the "s.update(m)",
        it returns only the updated speeches & members dict.
        If removed from the indent, it returns the updated dict as well as remaining dict
        but it also returns duplicates.
        In order to solve this, loop through the "ten_latest_speeches_dup" and remove duplicates.
        Set() does not hold duplicate items. Tuple() is used to maintain the order.
        """
    
        speeches = create_speeches_dict()
        members = get_relevant_members()
        
        ten_latest_speeches_dup = []
        for s in speeches:
            for m in members:
                if s["intressent_id"] == m["intressent_id"]:
                    s.update(m)
                ten_latest_speeches_dup.append(s)

        remove_dup = set()
        ten_latest_speeches = []
        for dup in ten_latest_speeches_dup:
            tup = tuple(dup.items())
            if tup not in remove_dup:
                remove_dup.add(tup)
                ten_latest_speeches.append(dup)
        print(ten_latest_speeches)
        return json.dumps(ten_latest_speeches)
    return app


def main():
    app = create_app()
    waitress.serve(app, host='0.0.0.0', port=8080)


if __name__ == "__main__":
    main()