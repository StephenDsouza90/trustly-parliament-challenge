import requests
import waitress
import flask
from flask import Flask, request, json


def get_speeches():
    # use speeches api to extract data
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
    # use members api to extract data
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
    # get speeches data from get_speeches func
    speeches_data = get_speeches()
    
    # loop through speeches_data to return relevant keys and values of ten latest speeches
    relevant_speeches = []

    for speeches in speeches_data:
        anforande_id = [v for k, v in speeches.items() if k == "anforande_id"]
        dok_datum = [v for k, v in speeches.items() if k == "dok_datum"]
        talare = [v for k, v in speeches.items() if k =="talare"]
        parti = [v for k, v in speeches.items() if k == "parti"]
        protokoll_url_www = [v for k, v in speeches.items() if k == "protokoll_url_www"]
        dok_titel = [v for k, v in speeches.items() if k == "dok_titel"]
        intressent_id = [v for k, v in speeches.items() if k == "intressent_id"] # to be removed later            

        speechesDict = {
            "anforande_id": anforande_id,
            "dok_datum": dok_datum,
            "talare": talare,
            "parti": parti, 
            "protokoll_url_www": protokoll_url_www, 
            "dok_titel": dok_titel,
            "intressent_id": intressent_id
            }
        relevant_speeches.append(speechesDict)
    return relevant_speeches


def create_members_dict():
    # get members data from get_members func
    members_data = get_members()

    # loop through members_data to return relevant values of ONLY those keys that are needed
    all_members = []
    for members in members_data:
        valkrets = [v for k, v in members.items() if k == "valkrets"]
        bild_url_192 = [v for k, v in members.items() if k == "bild_url_192"]
        uppgift = [v for k, v in members.items() if k == "uppgift"] # email not come
        intressent_id = [v for k, v in members.items() if k == "intressent_id"] # to be removed later

        membersDict = {
            "valkrets": valkrets,
            "bild_url_192": bild_url_192,
            "uppgift": uppgift,
            "intressent_id": intressent_id
            }
        all_members.append(membersDict)
    return all_members


def get_relevant_members():
    speeches_data = create_speeches_dict()
    members_data = create_members_dict()

    # access the value of FK in speeches_data and match that with the value of FK in the members_data
    relevant_members_dict = []
    for s in speeches_data:
        intressent_id = s["intressent_id"]
        for m in members_data:
            intressent_id_FK = m["intressent_id"]
            if intressent_id == intressent_id_FK:
                relevant_members = m
                relevant_members_dict.append(relevant_members)
    return relevant_members_dict


def create_app():
    app = Flask("Parliament Challenge")


    @app.route('/ten-latest-speeches', methods=['GET'])
    def get_ten_latest_speeches():
        """
        curl -X GET "localhost:8080/ten-latest-speeches"
        """
        # ten latest speeches
        speeches = create_speeches_dict()

        # relevant members data based on FK
        # only some members data are there as some do not exist
        members = get_relevant_members()

        # merge both data together
        ten_latest_speeches = []

        if speeches:
            for s in speeches:
                ten_latest_speeches.append(s)
    
        if members:
            for m in members:
                ten_latest_speeches.append(m)

        print(ten_latest_speeches)
        return json.dumps(ten_latest_speeches)    
    return app


def main():
    app = create_app()
    waitress.serve(app, host='0.0.0.0', port=8080)


if __name__ == "__main__":
    main()