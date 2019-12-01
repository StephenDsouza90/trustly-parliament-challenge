import requests
import waitress
import flask
from flask import Flask, request, json


not_found = {"message": "Not Found"}
success = {"message": "Success"}
failed = {"message": "Failed"}


def get_speeches():
    # use speeches api to extract data
    domain = 'http://data.riksdagen.se'
    speeches = 'anforandelista'
    size = 10
    format_type = 'json'
    response = requests.get('{}/{}/?anftyp=Nej&sz={}&utformat={}'.format(domain, speeches, size, format_type))

    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 404:
        return json.dumps(not_found)


def get_members():
    # use members api to extract data
    domain = 'http://data.riksdagen.se'
    members = 'personlista'
    format_type = 'json'
    response = requests.get('{}/{}/?iid=&fnamn=&enamn=&f_ar=&kn=&parti=&valkrets=&rdlstatus=&org=&utformat={}&sort=sorteringsnamn&sortorder=asc&termlista='.format(domain, members, format_type))

    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 404:
        return json.dumps(not_found)


def recursive_items(dictionary):
    # loop through nested dict
    # skips 1st nested loop
    for key, value in dictionary.items():
        if type(value) is dict:
            yield from recursive_items(value)
        else:
            yield (key, value)


def create_speeches_dict():
    # get speeches data from get_speeches func
    speeches_data = get_speeches()

    # loop through speeches_data to return relevant keys and values of ten latest speeches
    relevant_speeches = []
    for keys, values in recursive_items(speeches_data):
        for keys in values:
            anforande_id = [keys[x] for x in keys if x == "anforande_id"]
            dok_datum = [keys[x] for x in keys if x == "dok_datum"]
            talare = [keys[x] for x in keys if x == "talare"]
            parti = [keys[x] for x in keys if x == "parti"]
            protokoll_url_www = [keys[x] for x in keys if x == "protokoll_url_www"]
            dok_titel = [keys[x] for x in keys if x == "dok_titel"]
            intressent_id = [keys[x] for x in keys if x == "intressent_id"] # to be removed later

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

    # loop through members_data to return relevant values of ONLY the ten latest speeches
    NOT_relevant_members = []
    for keys, values in recursive_items(members_data):
        for keys in values:
            valkrets = [keys[x] for x in keys if x == "valkrets"]
            bild_url_192 = [keys[x] for x in keys if x == "bild_url_192"]
            uppgift = [keys[x] for x in keys if x == "uppgift"] # email not come
            intressent_id = [keys[x] for x in keys if x == "intressent_id"] # to be removed later

            membersDict = {
                "valkrets": valkrets,
                "bild_url_192": bild_url_192,
                "uppgift": uppgift,
                "intressent_id_check": intressent_id
                }
            NOT_relevant_members.append(membersDict)
    return NOT_relevant_members


def get_relevant_members():
    speeches_data = create_speeches_dict()
    members_data = create_members_dict()

    # access the value of FK in speeches_data and match that with the value of FK in the members_data
    relevant_members_dict = []
    for x in speeches_data:
        intressent_id = x["intressent_id"]
        for y in members_data:
            intressent_id_check = y["intressent_id_check"]
            if intressent_id == intressent_id_check:
                rel = y
                relevant_members_dict.append(rel)
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