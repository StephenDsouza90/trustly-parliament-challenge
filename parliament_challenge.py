import requests
import waitress
import flask
from flask import Flask, request, json


not_found = {"message": "Not Found"}
success = {"message": "Success"}
failed = {"message": "Failed"}


def create_app():
    app = Flask("Parliament Challenge")

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
            print(not_found)
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
            print(not_found)
            return json.dumps(not_found)

    def recursive_items(dictionary):
        # loop through nested dict
        # skips 1st nested loop
        for key, value in dictionary.items():
            if type(value) is dict:
                yield from recursive_items(value)
            else:
                yield (key, value)

    def get_foreignkey_speeches():
        # Get speeches data from get_speeches func
        speeches_data = get_speeches()

        # Loop through speeches_data to find "intressent_id" which is the foreign key
        speech_foreignkey_list = []
        for keys, values in recursive_items(speeches_data):
            for keys in values:
                for x in keys:
                    if x == "intressent_id":
                        speech_foreignkey_list.append(keys[x])
        return speech_foreignkey_list

    def get_foreignkey_members():
        # Get members data from get_members func
        members_data = get_members()

        # Loop through members_data to find "intressent_id" which is the foreign key
        members_foreignkey_list = []
        for keys, values in recursive_items(members_data): 
            for keys in values:
                for x in keys:
                    if x == "intressent_id":
                        members_foreignkey_list.append(keys[x])
        return members_foreignkey_list

    def speeches_dict():
        # Get speeches data from get_speeches func
        speeches_data = get_speeches()

        # loop through speeches_data to return relevant values of ten latest speeches        
        for keys, values in recursive_items(speeches_data):
            for keys in values:
                anforande_id = [keys[x] for x in keys if x == "anforande_id"]
                dok_datum = [keys[x] for x in keys if x == "dok_datum"]
                talare = [keys[x] for x in keys if x == "talare"]
                parti = [keys[x] for x in keys if x == "parti"]
                protokoll_url_www = [keys[x] for x in keys if x == "protokoll_url_www"]
                dok_titel = [keys[x] for x in keys if x == "dok_titel"]
                intressent_id = [keys[x] for x in keys if x == "intressent_id"] # to be removed later
        return anforande_id, dok_datum, talare, parti, protokoll_url_www, dok_titel, intressent_id
    # printing only 1 .. need to find a way to print all ten

    def members_dict():
        # Get members data from get_members func
        members_data = get_members()

        # Get foreign keys list from get_foreignkey_speeches and get_foreignkey_members func
        foreignkey_speeches = get_foreignkey_speeches()
        foreignkey_members = get_foreignkey_members()

        # loop through foreignkey_speeches and find a match in foreignkey_members
        for i in foreignkey_speeches:
            for j in foreignkey_members:
                if i == j:
                    # loop through members_data to return relevant values of ONLY the ten latest speeches
                    for keys, values in recursive_items(members_data):
                        for keys in values:
                            valkrets = [keys[x] for x in keys if x == "valkrets"]
                            bild_url_192 = [keys[x] for x in keys if x == "bild_url_192"]
                            uppgift = [keys[x] for x in keys if x == "uppgift"] # email not come
                            intressent_id = [keys[x] for x in keys if x == "intressent_id"] 
        return valkrets, bild_url_192, uppgift, intressent_id
    # Problem with matching foreign keys because someone else details are coming
    # printing only 1 .. need to find a way to print all ten 

    @app.route('/ten-latest-speeches', methods=['GET'])
    def get_ten_latest_speeches():
        """
        curl -X GET "localhost:8080/ten-latest-speeches"
        """

        # Get relevant speeches data list from speeches_dict func
        speeches_data = speeches_dict()
        # Get relevant memebers data list from members_dict func
        members_data = members_dict()

        # Empty list to merge both data together
        ten_latest_speeches = []

        # Since speeches_data and members_data and tuples so use []
        if speeches_data:
            if members_data:
                combinedDict = {
                    "anforande_id": speeches_data[0],
                    "dok_datum": speeches_data[1],
                    "talare": speeches_data[2],
                    "parti": speeches_data[3], 
                    "protokoll_url_www": speeches_data[4], 
                    "dok_titel": speeches_data[5],
                    "intressent_id": speeches_data[6],
                    "valkrets": members_data[0],
                    "bild_url_192": members_data[1],
                    "uppgift": members_data[2],
                    "intressent_id_check": members_data[3]
                    }

                ten_latest_speeches.append(combinedDict)

        print(ten_latest_speeches)
        return json.dumps(ten_latest_speeches)
    return app


def main():
    app = create_app()
    waitress.serve(app, host='0.0.0.0', port=8080)


if __name__ == "__main__":
    main()