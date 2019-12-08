# Trustly Parliament Challenge

## Problem

This is a challenge by Trustly known as the **"Parliament Challenge"**.

The Swedish parliament has an open API platform for developers to use its resources to create applications. Among its resources are the speeches in the parliament and the data of its members.

The challenge by Trustly is to create an appliction that serves requests for parliament speeches. The expected response should be created by merging the data from the speech's api and member's api and should be in a JSON format.

The expected response should at least contain:

- A unique ID, representing the speech itself (anforande_id - speech's api)
- Date of speech (dok_datum - speech's api)
- The name of the speaker, and only the name (tilltalsnamn - member's api)
- Political affiliation (parti - speech's api)
- The official e-mail address (uppgift - member's api)
- Constituency (valkrets - member's api)
- A decent sized image that could be used in a web site listing (bild_url_192 - member's api)
- The debate subject (avsnittsrubrik - speech's api)
- A link to the speech (HATEOAS style) (protokoll_url_www - speech's api)

The link to the challenge can be found on https://github.com/trustly/parliament-challenge

## Approach

### Speech's API

The speech's api represents the details of the speeches held at the Swedish parliament. This api has a filter option to get the number of speeches that the client requires. In this challenge, the objective is to get the ten latest speeches. The relevant keys and values that this api has are: **anforande_id, dok_datum, parti, avsnittsrubrik and protokoll_url_www**.

Link to the speech's api: http://data.riksdagen.se/anforandelista/?anftyp=Nej&sz=10&utformat=json

### Member's API

The member's api represents the details of the members of the Swedish parliament. In order get the relevant member data and link the speech to a member, a reference key **intressent_id** (which is common in both apis) is used as a filter option. The relevant keys and values that this api has are: **tilltalsnamn, valkrets, bild_url_192**.

Link to the member's api: http://data.riksdagen.se/personlista/?iid=&utformat=json

### Merge

In order to merge a speech to a member, the function will filter the respective apis for the relevant keys and values and link a speech to a member through the reference key **intressent_id**. The function will then update the speech data with member data by combining both data sets together and present a merged data.

## Server

The `create app()` is responsible for creating the server and the `main()` is used to run the server. This application uses a localhost and port 8080.

## How to run locally

This app uses the curl request **curl -H "Content-Type: application/json" -X GET -d "{\"anftyp\":\"Nej\", \"size\":10}" "localhost:8080/latest-speeches"** which has been mapped to the `get_latest_speeches()` in the `create_app()`.

```
Serving on http://StephenDsouza:8080

[
  {
    'anforande_id': '6dc3f668-4e18-ea11-912c-901b0e9b71a8', 
    'dok_datum': '2019-12-06', 
    'parti': 'S', 
    'avsnittsrubrik': 'Svar på interpellation 2019/20:148 om måluppfyllnad i livsmedelsstrategin', 
    'links': [{
      'rel': 'speech', 
      'href': 'http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70946/#anf89'
      }], 
    'intressent_id': '0339894357417', 
    'tilltalsnamn': 'Jennie', 
    'valkrets': 'Hallands län', 
    'bild_url_192': 'http://data.riksdagen.se/filarkiv/bilder/ledamot/4c6f215d-de3a-452d-83b5-f472b8668b7e_192.jpg'
  }, 
  {
    'anforande_id': '6cc3f668-4e18-ea11-912c-901b0e9b71a8', 
    'dok_datum': '2019-12-06', 
    'parti': 'M', 
    'avsnittsrubrik': 'Svar på interpellation 2019/20:148 om måluppfyllnad i livsmedelsstrategin', 
    'links': [{
      'rel': 'speech', 
      'href': 'http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70946/#anf88'
      }], 
    'intressent_id': '028954589415', 
    'tilltalsnamn': 'Ann-Sofie', 
    'valkrets': 'Västra Götalands läns norra', 
    'bild_url_192': 'http://data.riksdagen.se/filarkiv/bilder/ledamot/f91f6a86-591c-449c-b3dd-1fdaa86338cd_192.jpg'
  }, 
  {...}
]
```