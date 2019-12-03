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

1. The function `get_speeches()` is responsible for getting the speeches resources from its respective apis. The speeches api has a filter to extract the ten latest speeches. Since the data is in a nested dict, the for loop has been used to iterate over to the required dict which is "anforande". Speech api: http://data.riksdagen.se/anforandelista/?anftyp=Nej&sz=10&utformat=json

2. The function `get_members()` is responsible for getting the members resources from its respective apis. Here all members data has been extracted. Since the data is in a nested dict, the for loop has been used to iterate over to the required dict which is "person". Members api: http://data.riksdagen.se/personlista/?iid=&fnamn=&enamn=&f_ar=&kn=&parti=&valkrets=&rdlstatus=&org=&utformat=json&sort=sorteringsnamn&sortorder=asc&termlista=

3. Now since the ten latest speeches are in the `get_speeches()` function, a list of dict has been created in the `create_speeches_dict()` function contianing only the relevant keys and values of speeches. An additional key and value `intressent_id` has been added which can be used as a foreign key and be useful for merging the speeches data to members data. The relevant keys are:
- anforande_id
- dok_datum
- parti
- avsnittsrubrik
- protokoll_url_www
- intressent_id 

4. Now since we have all the members data in the `get_members()` function, a list of dict has been created in the `create_members_dict()` function containing only the relevant keys and values of all memebers. An additional key and value `intressent_id` has been added which can be used as a foreign key and be useful for merging the speeches data to members data. The relevant keys are: 
- tilltalsnamn
- valkrets 
- bild_url_192
- intressent_id

5. Some of the speakers/speeches in the speeches data are not in the members resource api, therefore, the relevant members data has been filtered in `get_relevant_members()` function based on the speeches data. This function matches the value of the `intressent_id` in the speeches list of dict to the value of the `intressent_id` in the members list of dict.

6. Now that we have the relevant keys and values of the ten latest speeches and the relevant keys and values of the members data based on those speeches, the data has been merged. The required output should be as follows:

when `intressent_id` matches
```
{
  "anforande_id": value,
  "dok_datum": value,
  "parti": value,
  "avsnittsrubrik: value,
  "protokoll_url_www": value,
  "intressent_id": value, 
  "tilltalsnamn": value, 
  "valkrets": value,
  "bild_url_192": value
  }
```

when `intressent_id` does not match or exist
```
{
  "anforande_id": value,
  "dok_datum": value,
  "parti": value,
  "avsnittsrubrik": value, 
  "protokoll_url_www": value, 
  "intressent_id": value
  }
```

In order to merger the data to get the ten latest speeches with relevant keys and values (with both speeches and members data), the `create_speeches_dict()`and `get_relevant_members()` function has been called since the relevant items are stored in the list of dict in these functions. In order to merge the speeches and members data together, both dicts have been matched by the `intressent_id` and an `update()` function merges both data sets together.

However, a concern is that the `update()` only returns the items that have been updated and merged together. In order to solve this problem, the `ten_latest_speeches_dup.append(s)` has been kept outside the if condition's indent. This solves the problem of returning the updated/merged items along with the remaining items that did not need a merge (since those speeches data was not in the members resources).

However, another concern araises because this returns duplicate items. In order to solve this problem, the `set()` function is used remove duplicate items and `tuple()` function is used to maintain the order.

## Server

The `create app()` function is responsible for creating the server and the `main` is used to run the server. This application uses a localhost and port 8080.

## How to run locally

This app uses the curl request (>> curl -X GET "localhost:8080/ten-latest-speeches") which has been mapped to the `get_ten_latest_speeches()` function in the `create_app()` function.

```
Serving on http://StephenDsouza:8080

[
  {
    "anforande_id": "1c4cbd6a-0116-ea11-912c-901b0e9b71a8", 
    "avsnittsrubrik": "Svar p\u00e5 interpellation 2019/20:112 om arbetsmilj\u00f6 och psykisk oh\u00e4lsa", 
    "dok_datum": "2019-12-03", 
    "intressent_id": "0661583406713", 
    "parti": "S", 
    "protokoll_url_www": "http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70943/#anf41"
    }, 
  {
    "anforande_id": "1b4cbd6a-0116-ea11-912c-901b0e9b71a8", 
    "avsnittsrubrik": "Svar p\u00e5 interpellation 2019/20:112 om arbetsmilj\u00f6 och psykisk oh\u00e4lsa", 
    "bild_url_192": "http://data.riksdagen.se/filarkiv/bilder/ledamot/96765f90-7072-436d-8143-264d7cbd7fa9_192.jpg", 
    "dok_datum": "2019-12-03", 
    "intressent_id": "0671241874717", 
    "parti": "M", 
    "protokoll_url_www": "http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70943/#anf40", 
    "tilltalsnamn": "Elisabeth", 
    "valkrets": "V\u00e4sterbottens l\u00e4n"
    }, 
  {"anforande_id": "1a4cbd6a-0116-ea11-912c-901b0e9b71a8", "avsnittsrubrik": "Svar p\u00e5 interpellation 2019/20:112 om arbetsmilj\u00f6 och psykisk oh\u00e4lsa", "dok_datum": "2019-12-03", "intressent_id": "0661583406713", "parti": "S", "protokoll_url_www": "http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70943/#anf39"}, 
  {"anforande_id": "194cbd6a-0116-ea11-912c-901b0e9b71a8", "avsnittsrubrik": "Svar p\u00e5 interpellation 2019/20:112 om arbetsmilj\u00f6 och psykisk oh\u00e4lsa", "bild_url_192": "http://data.riksdagen.se/filarkiv/bilder/ledamot/96765f90-7072-436d-8143-264d7cbd7fa9_192.jpg", "dok_datum": "2019-12-03", "intressent_id": "0671241874717", "parti": "M", "protokoll_url_www": "http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70943/#anf38", "tilltalsnamn": "Elisabeth", "valkrets": "V\u00e4sterbottens l\u00e4n"}, 
  {"anforande_id": "184cbd6a-0116-ea11-912c-901b0e9b71a8", "avsnittsrubrik": "Svar p\u00e5 interpellation 2019/20:112 om arbetsmilj\u00f6 och psykisk oh\u00e4lsa", "dok_datum": "2019-12-03", "intressent_id": "0661583406713", "parti": "S", "protokoll_url_www": "http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70943/#anf37"}, 
  {"anforande_id": "174cbd6a-0116-ea11-912c-901b0e9b71a8", "avsnittsrubrik": "Svar p\u00e5 interpellation 2019/20:112 om arbetsmilj\u00f6 och psykisk oh\u00e4lsa", "bild_url_192": "http://data.riksdagen.se/filarkiv/bilder/ledamot/96765f90-7072-436d-8143-264d7cbd7fa9_192.jpg", "dok_datum": "2019-12-03", "intressent_id": "0671241874717", "parti": "M", "protokoll_url_www": "http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70943/#anf36", "tilltalsnamn": "Elisabeth", "valkrets": "V\u00e4sterbottens l\u00e4n"}, 
  {"anforande_id": "164cbd6a-0116-ea11-912c-901b0e9b71a8", "avsnittsrubrik": "Svar p\u00e5 interpellation 2019/20:112 om arbetsmilj\u00f6 och psykisk oh\u00e4lsa", "dok_datum": "2019-12-03", "intressent_id": "0661583406713", "parti": "S", "protokoll_url_www": "http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70943/#anf35"}, 
  {"anforande_id": "154cbd6a-0116-ea11-912c-901b0e9b71a8", "avsnittsrubrik": "Svar p\u00e5 interpellation 2019/20:111 om utvecklingstid", "dok_datum": "2019-12-03", "intressent_id": "0661583406713", "parti": "S", "protokoll_url_www": "http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70943/#anf34"}, 
  {"anforande_id": "144cbd6a-0116-ea11-912c-901b0e9b71a8", "avsnittsrubrik": "Svar p\u00e5 interpellation 2019/20:111 om utvecklingstid", "bild_url_192": "http://data.riksdagen.se/filarkiv/bilder/ledamot/db90fc94-9496-4748-9b84-bcfadc24af74_192.jpg", "dok_datum": "2019-12-03", "intressent_id": "0588282566419", "parti": "M", "protokoll_url_www": "http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70943/#anf33", "tilltalsnamn": "Lars", "valkrets": "G\u00e4vleborgs l\u00e4n"},   
  {"anforande_id": "134cbd6a-0116-ea11-912c-901b0e9b71a8", "avsnittsrubrik": "Svar p\u00e5 interpellation 2019/20:111 om utvecklingstid", "dok_datum": "2019-12-03", "intressent_id": "0661583406713", "parti": "S", "protokoll_url_www": "http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70943/#anf32"}
  ]
```