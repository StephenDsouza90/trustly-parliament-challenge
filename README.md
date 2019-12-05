# Trustly Parliament Challenge

## Problem

This is a challenge by Trustly known as the "Parliament Challenge".

The Swedish parliament has an open API platform for developers to use its resources to create applications. Among its resources are the speeches in the parliament and the data of its members.

The challenge by Trustly is to create an appliction that serves requests for parliament speeches. The expected response should be created by merging the data from the speeches api and members api and should be in a JSON format.

The expected response should at least contain:

- A unique ID, representing the speech itself (anforande_id)
- Date of speech (dok_datum)
- The name of the speaker, and only the name (tilltalsnamn)
- Political affiliation (parti)
- The official e-mail address (uppgift)
- Constituency (valkrets)
- A decent sized image that could be used in a web site listing (bild_url_192)
- The debate subject (avsnittsrubrik)
- A link to the speech (HATEOAS style) (protokoll_url_www)

The link to the challenge can be found on https://github.com/trustly/parliament-challenge

## Approach

The challenge is approached as follows:

1. The function `get_speeches_api()` is responsible for getting the speech resources from its respective apis. The speech's api has a filter to extract the number of latest speeches. The for loop has been used to iterate over to the required dict which is "anforande". Speech api: http://data.riksdagen.se/anforandelista/?anftyp=Nej&sz=10&utformat=json

2. As the required number of latest speeches are in the `get_speeches_api()` function, a list of dict is created in the `create_speeches_dict()` function containing only the relevant keys and values. An additional key and value `intressent_id` is added which can be used as a reference key and be useful for merging the speeches data to members data. The relevant keys are:
- anforande_id
- dok_datum
- parti
- avsnittsrubrik
- protokoll_url_www
- intressent_id 

3. In order get the relevant member's data by using the reference key, the `create_speeches_reference_list()` creates a list of all the reference keys and this list is passed on to the `get_members_api()` function.

4. The function `get_members_api()` is responsible for getting the relevant member resources from its respective apis. By using the reference key, the relevant member's data is extracted. The for loop has been used to iterate over to the required dict which is "person". Members api: http://data.riksdagen.se/personlista/?iid=&utformat=json

5. As the required member's data is in the `get_members_api()` function, a list of dict is created in the `create_members_dict()` function containing only the relevant keys and values of memebers. An additional key and value `intressent_id` is added which can be used as a reference key and be useful for merging the speeches data to members data. The relevant keys are: 
- tilltalsnamn
- valkrets 
- bild_url_192
- intressent_id

6. As the relevant keys and values of the latest speeches and the relevant keys and values of the members data based on those speeches has been created in the `create_speeches_dict()` and `create_members_dict()` functions respectively, the data is merged by matching the reference keys from both data sets and an `update()` function merges both data sets together. The required output is as follows:

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

The `create app()` function is responsible for creating the server and the `main` is used to run the server. This application uses a localhost and port 8080.

## How to run locally

This app uses the curl request (>> curl -X GET "localhost:8080/ten-latest-speeches") which has been mapped to the `get_ten_latest_speeches()` function in the `create_app()` function.

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
  }
]
```