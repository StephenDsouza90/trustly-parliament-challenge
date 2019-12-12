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

The member's api represents the details of the members of the Swedish parliament. In order get the relevant member data and link a speech to a member, a reference key **intressent_id** (which is common in both apis) is used as a filter option. The relevant keys and values that this api has are: **tilltalsnamn, valkrets, uppgift and bild_url_192**.

Link to the member's api: http://data.riksdagen.se/personlista/?iid=&utformat=json

### Merge

In order to merge a speech to a member, the function will filter the respective apis for the relevant keys and values and link a speech to a member through the reference key **intressent_id**. The function will then update the speech data with member data by combining both data sets together and present a merged data.

## Server

The `create app()` is responsible for creating the server and the `main()` is used to run the server. This application uses a localhost and port 8080.

## How to run locally

This app uses the curl request **curl -X GET "localhost:8080/latest-speeches/?anftyp=Nej&sz=10"** which has been mapped to the `get_latest_speeches()` in the `create_app()`.

```
Serving on http://StephenDsouza:8080

[
  {
    'anforande_id': 'e1a9afb5-6b1c-ea11-912c-901b0e9b71a8', 
    'dok_datum': '2019-12-11', 
    'parti': 'L', 
    'avsnittsrubrik': 'Energi', 
    'links': [{
      'rel': 'speech', 
      'href': 'http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70949/#anf226'
      }], 
    'intressent_id': '0322827326923', 
    'tilltalsnamn': 'Arman', 
    'valkrets': 'Värmlands län', 
    'uppgift': 'arman.teimouri[på]riksdagen.se', 
    'bild_url_192': 'http://data.riksdagen.se/filarkiv/bilder/ledamot/92355c36-d95d-42ed-9ad9-463bf9558767_192.jpg'
  }, 
  {
    'anforande_id': 'd8a9afb5-6b1c-ea11-912c-901b0e9b71a8', 
    'dok_datum': '2019-12-11', 
    'parti': 'C', 
    'avsnittsrubrik': 'Energi', 
    'links': [{
      'rel': 'speech', 
      'href': 'http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70949/#anf217'
      }], 
    'intressent_id': '0132818093422', 
    'tilltalsnamn': 'Rickard', 
    'valkrets': 'Göteborgs kommun', 
    'uppgift': 'rickard.nordin[på]riksdagen.se', 
    'bild_url_192': 'http://data.riksdagen.se/filarkiv/bilder/ledamot/a57d39bb-9f60-4def-ab90-97791ec56447_192.jpg'
  },
  {...}
]
```