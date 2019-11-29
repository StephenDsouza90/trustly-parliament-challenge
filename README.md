# Trustly Parliament Challenge

### Problems
1. Not being able to match the releveant foreign key from get_foreignkey_speeches() to get_foreignkey_members()
```
This is correct

[{'anforande_id': ['778a7f0d-0812-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-28'], 'talare': ['Marie-Louise Hänel Sandström (M)'], 'parti': ['M'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70940/#anf63'], 'dok_titel': ['Protokoll 2019/20:40 Torsdagen den 28 november'], 'intressent_id': ['0810852280213'], 

This is the merger but the details are of another member

'valkrets': ['Stockholms kommun'], 'bild_url_192': ['http://data.riksdagen.se/filarkiv/bilder/ledamot/df3988c4-9541-465c-b02e-1410c3d31155_192.jpg'], 'uppgift': [], 'intressent_id_check': ['0277648711624']}]
```

2. Find a way to return ten speeches from the speeches_dict() and members_dict()
```
Since speeches_dict() is currently returning only 1 dict so 1 dict is being printed in get_ten_latest_speeches()

[{'anforande_id': ['778a7f0d-0812-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-28'], 'talare': ['Marie-Louise Hänel Sandström (M)'], 'parti': ['M'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70940/#anf63'], 'dok_titel': ['Protokoll 2019/20:40 Torsdagen den 28 november'], 'intressent_id': ['0810852280213'], 'valkrets': ['Stockholms kommun'], 'bild_url_192': ['http://data.riksdagen.se/filarkiv/bilder/ledamot/df3988c4-9541-465c-b02e-1410c3d31155_192.jpg'], 'uppgift': [], 'intressent_id_check': ['0277648711624']}]
```


## Approach
>> Speech data already provides the list of latest ten speeches.
>> Merger the members data to the speeches data.
>> Match foreign key which is "intressent_id" .. in english stakeholders_id
>> Present relevant combined data.


## Speech data: http://data.riksdagen.se/anforandelista/?anftyp=Nej&sz=10&utformat=json

Speeches data looks like this
```
{"anforandelista": {"@antal": "10", 
                    "anforande": [{
                "anforande_id": "1e288fdf-5f11-ea11-912c-901b0e9b71a8", 
                "dok_datum": "2019-11-27", 
                "talare": "Helena Gellerman (L)", 
                "parti": "L", 
                "protokoll_url_www": "http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70939/#anf162", 
                "dok_titel": "Protokoll 2019/20:39 Onsdagen den 27 november"
    }]}}
```

## Members data: http://data.riksdagen.se/personlista/?iid=&fnamn=&enamn=&f_ar=&kn=&parti=&valkrets=&rdlstatus=&org=&utformat=json&sort=sorteringsnamn&sortorder=asc&termlista=

Speeches data looks like this

```
{"personlista": {"@systemdatum": "2019-11-28 16:44:19",
                 "@hits": "349",
                 "person": [{
        "valkrets": "Skåne läns västra",
        "bild_url_192": "http://data.riksdagen.se/filarkiv/bilder/ledamot/45445eb9-01dc-4786-990e-c1864d4f7c50_192.jpg",
        "personuppgift": {"uppgift": 
        [{
          "kod": "Officiell e-postadress",
          "uppgift": ["tina.acketoft[på]riksdagen.se"],
            "typ": "eadress",
          "intressent_id": "0582811195313",
          "hangar_id": "2343333"
          }]}}
```

## CombinedDict

CombinedDict should looks like this

```
combinedDict = {
            "anforande_id": ..., 
            "dok_datum": ..., 
            "talare": ..., 
            "parti": ..., 
            "protokoll_url_www": ..., 
            "dok_titel": ...,
            "valkrets": ..., 
            "bild_url_192": ..., 
            "uppgift": ...
            }
```

## 1st Attempt - Returning only speeches data

Returning speeches data by making a dict in the speeches_dict() and using .append()

```
[
  {'anforande_id': [], 'dok_datum': [], 'talare': [], 'parti': [], 'protokoll_url_www': [], 'dok_titel': []}, 
  {'anforande_id': [], 'dok_datum': [], 'talare': [], 'parti': [], 'protokoll_url_www': [], 'dok_titel': []}, 
  
  {'anforande_id': ['808a7f0d-0812-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-28'], 'talare': ['Statsministern Stefan Löfven (S)'], 'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70940/#anf72'], 'dok_titel': ['Protokoll 2019/20:40 Torsdagen den 28 november']}, 
  
  {'anforande_id': ['7f8a7f0d-0812-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-28'], 'talare': ['Aylin Fazelian (S)'], 'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70940/#anf71'], 'dok_titel': ['Protokoll 2019/20:40 Torsdagen den 28 november']}, 
  
  {'anforande_id': ['7e8a7f0d-0812-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-28'], 'talare': ['Statsministern Stefan Löfven (S)'], 'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70940/#anf70'], 'dok_titel': ['Protokoll 2019/20:40 Torsdagen den 28 november']}, 
  
  {'anforande_id': ['7d8a7f0d-0812-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-28'], 'talare': ['Lars Jilmstad (M)'], 'parti': ['M'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70940/#anf69'], 'dok_titel': ['Protokoll 2019/20:40 Torsdagen den 28 november']}, 
  
  {'anforande_id': ['7c8a7f0d-0812-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-28'], 'talare': ['Statsministern Stefan Löfven (S)'], 'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70940/#anf68'], 'dok_titel': ['Protokoll 2019/20:40 Torsdagen den 28 november']}, 
  
  {'anforande_id': ['7b8a7f0d-0812-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-28'], 'talare': ['Lars-Arne Staxäng (M)'], 'parti': ['M'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70940/#anf67'], 'dok_titel': ['Protokoll 2019/20:40 Torsdagen den 28 november']}, 
  
  {'anforande_id': ['7a8a7f0d-0812-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-28'], 'talare': ['Statsministern Stefan Löfven (S)'], 'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70940/#anf66'], 'dok_titel': ['Protokoll 2019/20:40 Torsdagen den 28 november']}, 
  
  {'anforande_id': ['798a7f0d-0812-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-28'], 'talare': ['Anders Österberg (S)'], 'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70940/#anf65'], 'dok_titel': ['Protokoll 2019/20:40 Torsdagen den 28 november']}, 
  
  {'anforande_id': ['788a7f0d-0812-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-28'], 'talare': ['Statsministern Stefan Löfven (S)'], 'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70940/#anf64'], 'dok_titel': ['Protokoll 2019/20:40 Torsdagen den 28 november']}, 

  {'anforande_id': ['778a7f0d-0812-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-28'], 'talare': ['Marie-Louise Hänel Sandström (M)'], 'parti': ['M'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70940/#anf63'], 'dok_titel': ['Protokoll 2019/20:40 Torsdagen den 28 november']}
  ]
```

## 2nd Attempt - Returning speeches data and members data

Returned speeches data and members data by creating two seperate dicts with the speeches_dict() and members_dict().

Although this is not the correct approch but I wanted to return all the results to see what it looks like.

```
Speeches data


[
  {'anforande_id': [], 'dok_datum': [], 'talare': [], 'parti': [], 'protokoll_url_www': [], 'dok_titel': [], 'intressent_id': []},
  {'anforande_id': [], 'dok_datum': [], 'talare': [], 'parti': [], 'protokoll_url_www': [], 'dok_titel': [], 'intressent_id': []},
  
  {'anforande_id': ['808a7f0d-0812-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-28'], 'talare': ['Statsministern Stefan Löfven (S)'], 'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70940/#anf72'], 'dok_titel': ['Protokoll 2019/20:40 Torsdagen den 28 november'], 'intressent_id': ['0218878014918']}, 
  
  {'anforande_id': ['7f8a7f0d-0812-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-28'], 'talare': ['Aylin Fazelian (S)'], 'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70940/#anf71'], 'dok_titel': ['Protokoll 2019/20:40 Torsdagen den 28 november'], 'intressent_id': ['0523902030928']}, 
  
  {'anforande_id': ['7e8a7f0d-0812-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-28'], 'talare': ['Statsministern Stefan Löfven (S)'], 'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70940/#anf70'], 'dok_titel': ['Protokoll 2019/20:40 Torsdagen den 28 november'], 'intressent_id': ['0218878014918']}, 
  
  {'anforande_id': ['7d8a7f0d-0812-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-28'], 'talare': ['Lars Jilmstad (M)'], 'parti': ['M'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70940/#anf69'], 'dok_titel': ['Protokoll 2019/20:40 Torsdagen den 28 november'], 'intressent_id': ['0722683622001']}, 
  
  {'anforande_id': ['7c8a7f0d-0812-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-28'], 'talare': ['Statsministern Stefan Löfven (S)'], 'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70940/#anf68'], 'dok_titel': ['Protokoll 2019/20:40 Torsdagen den 28 november'], 'intressent_id': ['0218878014918']}, 
  
  {'anforande_id': ['7b8a7f0d-0812-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-28'], 'talare': ['Lars-Arne Staxäng (M)'], 'parti': ['M'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70940/#anf67'], 'dok_titel': ['Protokoll 2019/20:40 Torsdagen den 28 november'], 'intressent_id': ['0718937995813']}, 
  
  {'anforande_id': ['7a8a7f0d-0812-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-28'], 'talare': ['Statsministern Stefan Löfven (S)'], 'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70940/#anf66'], 'dok_titel': ['Protokoll 2019/20:40 Torsdagen den 28 november'], 'intressent_id': ['0218878014918']}, 
  
  {'anforande_id': ['798a7f0d-0812-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-28'], 'talare': ['Anders Österberg (S)'], 'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70940/#anf65'], 'dok_titel': ['Protokoll 2019/20:40 Torsdagen den 28 november'], 'intressent_id': ['0277648711624']}, 
  
  {'anforande_id': ['788a7f0d-0812-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-28'], 'talare': ['Statsministern Stefan Löfven (S)'], 'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70940/#anf64'], 'dok_titel': ['Protokoll 2019/20:40 Torsdagen den 28 november'], 'intressent_id': ['0218878014918']}, 
  
  {'anforande_id': ['778a7f0d-0812-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-28'], 'talare': ['Marie-Louise Hänel Sandström (M)'], 'parti': ['M'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70940/#anf63'], 'dok_titel': ['Protokoll 2019/20:40 Torsdagen den 28 november'], 'intressent_id': ['0810852280213']}, 
  
Members data

  {'valkrets': [], 'bild_url_192': [], 'uppgift': [], 'intressent_id': []}, 
  {'valkrets': [], 'bild_url_192': [], 'uppgift': [], 'intressent_id': []}, 
  
  {'valkrets': ['Stockholms kommun'], 'bild_url_192': ['http://data.riksdagen.se/filarkiv/bilder/ledamot/df3988c4-9541-465c-b02e-1410c3d31155_192.jpg'], 'uppgift': [], 'intressent_id': ['0277648711624']}, 
  
  {'valkrets': [], 'bild_url_192': [], 'uppgift': [], 'intressent_id': []}, 
  
  {'valkrets': [], 'bild_url_192': [], 'uppgift': [], 'intressent_id': []}, {'valkrets': ['Stockholms kommun'], 'bild_url_192': ['http://data.riksdagen.se/filarkiv/bilder/ledamot/df3988c4-9541-465c-b02e-1410c3d31155_192.jpg'], 'uppgift': [], 'intressent_id': ['0277648711624']}, 
  
  {'valkrets': [], 'bild_url_192': [], 'uppgift': [], 'intressent_id': []}, {'valkrets': [], 'bild_url_192': [], 'uppgift': [], 'intressent_id': []}, {'valkrets': ['Stockholms kommun'], 'bild_url_192': ['http://data.riksdagen.se/filarkiv/bilder/ledamot/df3988c4-9541-465c-b02e-1410c3d31155_192.jpg'], 'uppgift': [], 'intressent_id': ['0277648711624']}, 
  
  {'valkrets': [], 'bild_url_192': [], 'uppgift': [], 'intressent_id': []}, 
  
  {'valkrets': [], 'bild_url_192': [], 'uppgift': [], 'intressent_id': []}, 
  
  {'valkrets': ['Stockholms kommun'], 'bild_url_192': ['http://data.riksdagen.se/filarkiv/bilder/ledamot/df3988c4-9541-465c-b02e-1410c3d31155_192.jpg'], 'uppgift': [], 'intressent_id': ['0277648711624']}, 
  
  {'valkrets': [], 'bild_url_192': [], 'uppgift': [], 'intressent_id': []}, 
  
  {'valkrets': [], 'bild_url_192': [], 'uppgift': [], 'intressent_id': []}, 
  
  {'valkrets': ['Stockholms kommun'], 'bild_url_192': ['http://data.riksdagen.se/filarkiv/bilder/ledamot/df3988c4-9541-465c-b02e-1410c3d31155_192.jpg'], 'uppgift': [], 'intressent_id': ['0277648711624']}]
```

## 3rd Attempt - Returning combined data

Tried to return the combined data but it returned only the 1st speech.

I also wanted to check if the correct FK was coming so I added the "intressent_id".

I noticed that the members data was not matching the speeches data.

Problem addressed above as well.

```
[{'anforande_id': ['778a7f0d-0812-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-28'], 'talare': ['Marie-Louise Hänel Sandström (M)'], 'parti': ['M'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70940/#anf63'], 'dok_titel': ['Protokoll 2019/20:40 Torsdagen den 28 november'], 'intressent_id': ['0810852280213'], 

'valkrets': ['Stockholms kommun'], 'bild_url_192': ['http://data.riksdagen.se/filarkiv/bilder/ledamot/df3988c4-9541-465c-b02e-1410c3d31155_192.jpg'], 'uppgift': [], 'intressent_id_check': ['0277648711624']}]
```