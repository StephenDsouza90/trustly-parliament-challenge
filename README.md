# Trustly Parliament Challenge

## Problem

This is a challenge by Trustly known as the **"Parliament Challenge"**.

The Swedish parliament has an open API platform for developers to use its resources to create applications. Among its resources are the speeches in the parliament and the data of its members.

The challenge by Trustly is to create an appliction that serves requests for parliament speeches. The expected response should be created by merging the data from the speech's api and member's api and should be in a JSON format.

The expected response should at least contain:

- A unique ID, representing the speech itself (anforande_id - speech's api)
- Date of speech (dok_datum- speech's api)
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

The speech's api represents the details of the speeches held at the Swedish parliament. This api has a filter option to get a certain number of speeches. In this challenge, the objective is to get the ten latest speeches. The api contains some of the relevant keys and values **(anforande_id, dok_datum, parti, avsnittsrubrik and protokoll_url_www)** which are extracted and stored in a list of dict.

The link to the speech's api is http://data.riksdagen.se/anforandelista/?anftyp=Nej&sz=10&utformat=json

### Member's API

The member's api represents the details of the members of the Swedish parliament. In order to link the speeches data to the members data, a reference key **intressent_id** (which is common in both apis) is used. By using this reference key as a filter option in the member's api, the relevant member's data (tilltalsnamn, valkrets, bild_url_192) is extracted and stored in a list of dict.

The link to the member's api is http://data.riksdagen.se/personlista/?iid=&utformat=json

### Merge

As a **speeches list of dict** and **memebers list of dict** is created, both data sets can be merged together by linking it through the reference key (which is also included in both list of dict). The merge will join the relevant speech to member and present the data in a single dict. 

An example of the output is as follows:

```
{
  'anforande_id': 'value', 
  'dok_datum': 'value', 
  'parti': 'value', 
  'avsnittsrubrik': 'value', 
  'links': [{
        'rel': 'speech', 
        'href': 'vale'
      }], 
  'intressent_id': 'value', 
  'tilltalsnamn': 'value', 
  'valkrets': 'value', 
  'bild_url_192': 'value'
}
```

## Server

The `create app()` is responsible for creating the server and the `main()` is used to run the server. This application uses a localhost and port 8080.

## How to run locally

This app uses the curl request **(>> curl -X GET "localhost:8080/ten-latest-speeches")** which has been mapped to the `get_ten_latest_speeches()` in the `create_app()`.

```
Serving on http://StephenDsouza:8080

[
  {
    'anforande_id': '877ba0aa-e216-ea11-912c-901b0e9b71a8', 
    'dok_datum': '2019-12-04', 
    'parti': 'MP', 
    'avsnittsrubrik': 'Samhällsplanering, bostadsförsörjning och byggande samt konsumentpolitik', 
    'links': [{
        'rel': 'speech', 
        'href': 'http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70944/#anf199'
      }], 
    'intressent_id': '0999976269027', 
    'tilltalsnamn': 'Amanda', 
    'valkrets': 
    'Stockholms län', 
    'bild_url_192': 'http://data.riksdagen.se/filarkiv/bilder/ledamot/d12313ba-680b-4784-b858-5c9e6db692e7_192.jpg'
  }, 
  {
    'anforande_id': '827ba0aa-e216-ea11-912c-901b0e9b71a8', 
    'dok_datum': '2019-12-04', 
    'parti': 'V', 
    'avsnittsrubrik': 'Samhällsplanering, bostadsförsörjning och byggande samt konsumentpolitik', 
    'links': [{
        'rel': 'speech', 
        'href': 'http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70944/#anf194'
      }], 
    'intressent_id': '0272006117024', 
    'tilltalsnamn': 'Jon', 
    'valkrets': 'Hallands län', 
    'bild_url_192': 'http://data.riksdagen.se/filarkiv/bilder/ledamot/e66d3e3a-3f97-4942-bc4a-f4aa89ad365a_192.jpg'
  },
  {...}
]
```