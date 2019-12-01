# Trustly Parliament Challenge

### Problems
1. Not being able to merger speeches data with members data

speeches
```
[{'anforande_id': ['49102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Arbetsmarknadsministern Eva Nordmark (S)'],
 'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf170'], 'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['0661583406713']},


{'anforande_id': ['48102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Ali Esbati (V)'], 'parti': ['V'], 
'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf169'], 
'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['014386615025']}, 


{'anforande_id': ['47102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Arbetsmarknadsministern Eva Nordmark (S)'], 
'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf168'], 
'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['0661583406713']}, 


{'anforande_id': ['46102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Ali Esbati (V)'], 'parti': ['V'], 
'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf167'], 
'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['014386615025']}, 


{'anforande_id': ['45102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Arbetsmarknadsministern Eva Nordmark (S)'], 
'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf166'], 
'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['0661583406713']}, 


{'anforande_id': ['44102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Ali Esbati (V)'], 'parti': ['V'], 
'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf165'], 
'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['014386615025']}, 


{'anforande_id': ['43102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Arbetsmarknadsministern Eva Nordmark (S)'], 
'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf164'], 
'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['0661583406713']}, 


{'anforande_id': ['42102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Infrastrukturministern Tomas Eneroth (S)'], 
'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf163'], 
'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['0284192765516']}, 


{'anforande_id': ['41102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Jens Holm (V)'], 'parti': ['V'], 
'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf162'], 
'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['0216534495014']}, 


{'anforande_id': ['40102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Infrastrukturministern Tomas Eneroth (S)'], 
'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf161'], 
'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['0284192765516']}]
```

members
```
[{'valkrets': ['Stockholms kommun'], 'bild_url_192': ['http://data.riksdagen.se/filarkiv/bilder/ledamot/979e9852-69ed-4077-8140-52ab99414a6c_192.jpg'], 'uppgift': [], 
'intressent_id_check': ['014386615025']}, 


{'valkrets': ['Stockholms kommun'], 'bild_url_192': ['http://data.riksdagen.se/filarkiv/bilder/ledamot/979e9852-69ed-4077-8140-52ab99414a6c_192.jpg'], 'uppgift': [], 
'intressent_id_check': ['014386615025']}, 


{'valkrets': ['Stockholms kommun'], 'bild_url_192': ['http://data.riksdagen.se/filarkiv/bilder/ledamot/979e9852-69ed-4077-8140-52ab99414a6c_192.jpg'], 'uppgift': [], 
'intressent_id_check': ['014386615025']}, 


{'valkrets': ['Stockholms kommun'], 'bild_url_192': ['http://data.riksdagen.se/filarkiv/bilder/ledamot/5b7ac02c-0819-426d-bc5d-41b8c21ca4dd_192.jpg'], 'uppgift': [], 
'intressent_id_check': ['0216534495014']}]
```

## Approach
>> Speech data already provides the list of latest ten speeches.

>> Merger the members data to the speeches data.

>> Match foreign key which is "intressent_id" .. in english stakeholders_id

>> Present relevant combined data.


## Speech data: http://data.riksdagen.se/anforandelista/?anftyp=Nej&sz=10&utformat=json

## Members data: http://data.riksdagen.se/personlista/?iid=&fnamn=&enamn=&f_ar=&kn=&parti=&valkrets=&rdlstatus=&org=&utformat=json&sort=sorteringsnamn&sortorder=asc&termlista=

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