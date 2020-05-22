# Trustly Parliament Challenge

## Problem

This is a challenge by **Trustly** known as the **"Parliament Challenge"**.

The Swedish Parliament has an open API platform for developers to use its resources to create applications. Among its resources are the speeches in the parliament and the data of its members.

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

The speech's api represents the details of the speeches held at the Swedish Parliament. This api has a filter option to get the number of speeches that the client requires. In this challenge, the objective is to get the ten latest speeches. 

The relevant keys and values that this api has are: 

- **anforande_id**
- **dok_datum**
- **parti**
- **avsnittsrubrik**
- **protokoll_url_www**

Link to the speech's api: http://data.riksdagen.se/anforandelista/?anftyp=Nej&sz=10&utformat=json

### Member's API

The member's api represents the details of the members of the Swedish Parliament. In order get the relevant member data and link a speech to a member, a reference key **intressent_id** (which is common in both apis) is used as a filter option. 

The relevant keys and values that this api has are: 

- **tilltalsnamn**
- **valkrets**
- **uppgift**
- **bild_url_192**

Link to the member's api: http://data.riksdagen.se/personlista/?iid=&utformat=json

### Merge

In order to merge a speech to a member, the speech data is filtered for the relevant keys and values and is linked to a member data through the reference key **intressent_id**. The member data is also filtered for the relevant keys and values. The speech data is updated with the relevant member data by combining both data sets together and presents a merged data.

## AsyncIO

The `parliament_challenge_asynchronous.py` implements the Trustly Parliament Challenge asynchronously allowing the app to run multiple requests concurrently. In concurrent programming, multiple tasks also have the ability to run in an overlapping manner thus making the app to run faster and efficeintly.

The `asyncio` is a built-in Python package that runs on a single-thread (called the event loop) allowing for cooperative multitasking among the coroutine functions. A coroutine function can “pause” while waiting on their ultimate result and let other functions run in the meantime.

To make this app run concurrently, the keywords `async/await` are used to define the coroutine functions. Furthermore, each speech data is updated with a memeber data in a seperate task, eliminating the dependencey between each merger. 

## Server

**Synchronous**

The `create app()` uses the `Flask` web framework for creating the server and the `main()` uses `waitress` for running the server.

**Asynchronous**

The `create app()` uses the `Quart` web framework for creating the server and the `main()` uses `hypercorn` for running the server.

## How to run locally

**Synchronous**

This app uses the curl request **curl -X GET "localhost:8080/latest-speeches/?anftyp=Nej&sz=10"** which has been mapped to the `get_latest_speeches()` in the `create_app()`.

```

Serving on http://StephenDsouza:8080

```

**Asynchronous**

This app uses the curl request **curl -X GET "127.0.0.1:8080/latest-speeches/?anftyp=Nej&sz=10"** which has been mapped to the `get_latest_speeches()` in the `create_app()`.

```

Running on 127.0.0.1:8080 over http (CTRL + C to quit)

```

```

[
  {
    "anforande_id": "3d645c5e-d698-ea11-9132-901b0eac4c78", 
    "avsnittsrubrik": "F\u00f6rb\u00e4ttringar f\u00f6r barn inom den psykiatriska tv\u00e5ngsv\u00e5rden", 
    "bild_url_192": "http://data.riksdagen.se/filarkiv/bilder/ledamot/87042942-c4f6-46ff-9eac-fceaf25729d5_192.jpg", 
    "dok_datum": "2020-05-14", 
    "intressent_id": "0161616238120", 
    "links": [
      {
        "href": "http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H709121/#anf99", 
        "rel": "speech"
      }
    ], 
    "parti": "L", 
    "tilltalsnamn": "Lina", 
    "uppgift": "lina.nordquist[p\u00e5]riksdagen.se", 
    "valkrets": "Uppsala l\u00e4n"
  }, 
  {
    "anforande_id": "3c645c5e-d698-ea11-9132-901b0eac4c78", 
    "avsnittsrubrik": "F\u00f6rb\u00e4ttringar f\u00f6r barn inom den psykiatriska tv\u00e5ngsv\u00e5rden", 
    "bild_url_192": "http://data.riksdagen.se/filarkiv/bilder/ledamot/560c0817-1b91-478a-b273-87a82888328e_192.jpg", 
    "dok_datum": "2020-05-14", 
    "intressent_id": "0454698803028", 
    "links": [
      {
        "href": "http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H709121/#anf98", 
        "rel": "speech"
      }
    ], 
    "parti": "C", 
    "tilltalsnamn": "Sofia", 
    "uppgift": "sofia.nilsson[p\u00e5]riksdagen.se", 
    "valkrets": "Sk\u00e5ne l\u00e4ns norra och \u00f6stra"
  }, 
  {...}
]

```