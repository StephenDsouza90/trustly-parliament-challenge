# Trustly Parliament Challenge

## Introduction

The parliament challenge by Trustly is approached as follows:

1. Get speeches resource from its respective apis. Since speeches data is in a nested dict, the for loop has been used to iterate over the required dict which is "anforande". The speeches api allows for extracting the ten latest speeches.

> Speech api: http://data.riksdagen.se/anforandelista/?anftyp=Nej&sz=10&utformat=json

2. Get members resource from its respective apis. Since members data is in a nested dict, the for loop has been used to iterate over the required dict which is "person". All members data has been extracted.

> Members api: http://data.riksdagen.se/personlista/?iid=&fnamn=&enamn=&f_ar=&kn=&parti=&valkrets=&rdlstatus=&org=&utformat=json&sort=sorteringsnamn&sortorder=asc&termlista=

3. Create a speeches dict of the ten latest speeches and extract the relevant information (Given below). The intressent_id is an extra data extracted because it is a common object between the speeches data and members data. 
- anforande_id
- dok_datum
- talare
- parti
- protokoll_url_www
- dok_titel
- intressent_id 

speeches
```
[
  {
    'anforande_id': ['49102c9a-e312-ea11-912c-901b0e9b71a8'], 
    'dok_datum': ['2019-11-29'], 
    'talare': ['Arbetsmarknadsministern Eva Nordmark (S)'], 
    'parti': ['S'], 
    'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf170'], 
    'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 
    'intressent_id': ['0661583406713']
    }, 

  {'anforande_id': ['48102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Ali Esbati (V)'], 'parti': ['V'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf169'], 'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['014386615025']}, 
  {'anforande_id': ['47102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Arbetsmarknadsministern Eva Nordmark (S)'], 'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf168'], 'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['0661583406713']}, 
  {'anforande_id': ['46102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Ali Esbati (V)'], 'parti': ['V'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf167'], 'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['014386615025']}, 
  {'anforande_id': ['45102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Arbetsmarknadsministern Eva Nordmark (S)'], 'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf166'], 'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['0661583406713']}, 
  {'anforande_id': ['44102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Ali Esbati (V)'], 'parti': ['V'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf165'], 'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['014386615025']}, 
  {'anforande_id': ['43102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Arbetsmarknadsministern Eva Nordmark (S)'], 'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf164'], 'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['0661583406713']}, 
  {'anforande_id': ['42102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Infrastrukturministern Tomas Eneroth (S)'], 'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf163'], 'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['0284192765516']}, 
  {'anforande_id': ['41102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Jens Holm (V)'], 'parti': ['V'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf162'], 'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['0216534495014']}, 
  {'anforande_id': ['40102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Infrastrukturministern Tomas Eneroth (S)'], 'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf161'], 'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['0284192765516']}
  ]
```

4. Create a members dict of all members and extract the relevant information (Given below). Again the intressent_id is an extra data extracted because it is a common object between the speeches data and members data. 
- valkrets 
- bild_url_192
- uppgift
- intressent_id

5. Get the relevant members information based on the ten latest speeches by matching a common object which is intressent_id. By this approach, only the relevant members information can be extracted and stored in a list.

members
```
[
  {
    'valkrets': ['Stockholms kommun'], 
    'bild_url_192': ['http://data.riksdagen.se/filarkiv/bilder/ledamot/979e9852-69ed-4077-8140-52ab99414a6c_192.jpg'], 'uppgift': [], 
    'intressent_id_FK': ['014386615025']
    }, 

  {'valkrets': ['Stockholms kommun'], 'bild_url_192': ['http://data.riksdagen.se/filarkiv/bilder/ledamot/979e9852-69ed-4077-8140-52ab99414a6c_192.jpg'], 'uppgift': [], 'intressent_id_FK': ['014386615025']}, 
  {'valkrets': ['Stockholms kommun'], 'bild_url_192': ['http://data.riksdagen.se/filarkiv/bilder/ledamot/979e9852-69ed-4077-8140-52ab99414a6c_192.jpg'], 'uppgift': [], 'intressent_id_FK': ['014386615025']}, 
  {'valkrets': ['Stockholms kommun'], 'bild_url_192': ['http://data.riksdagen.se/filarkiv/bilder/ledamot/5b7ac02c-0819-426d-bc5d-41b8c21ca4dd_192.jpg'], 'uppgift': [], 'intressent_id_FK': ['0216534495014']}
  ]
```

6. Merge data

### Problems
Need to find a way to merge the data together.

Currenty speeches and members are in one list but this needs to be changed.
```
[
  {'anforande_id': ['49102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Arbetsmarknadsministern Eva Nordmark (S)'], 'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf170'], 'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['0661583406713']}, 
  
  {'anforande_id': ['48102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Ali Esbati (V)'], 'parti': ['V'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf169'], 'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['014386615025']}, 
  
  {'anforande_id': ['47102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Arbetsmarknadsministern Eva Nordmark (S)'], 'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf168'], 'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['0661583406713']}, 
  
  {'anforande_id': ['46102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Ali Esbati (V)'], 'parti': ['V'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf167'], 'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['014386615025']}, 
  
  {'anforande_id': ['45102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Arbetsmarknadsministern Eva Nordmark (S)'], 'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf166'], 'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['0661583406713']}, 
  
  
  {'anforande_id': ['44102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Ali Esbati (V)'], 'parti': ['V'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf165'], 'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['014386615025']}, 
  
  {'anforande_id': ['43102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Arbetsmarknadsministern Eva Nordmark (S)'], 'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf164'], 'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['0661583406713']}, 
  
  {'anforande_id': ['42102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Infrastrukturministern Tomas Eneroth (S)'], 'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf163'], 'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['0284192765516']}, 
  
  {'anforande_id': ['41102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Jens Holm (V)'], 'parti': ['V'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf162'], 'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['0216534495014']}, 
  
  {'anforande_id': ['40102c9a-e312-ea11-912c-901b0e9b71a8'], 'dok_datum': ['2019-11-29'], 'talare': ['Infrastrukturministern Tomas Eneroth (S)'], 'parti': ['S'], 'protokoll_url_www': ['http://www.riksdagen.se/sv/Dokument-Lagar/Kammaren/Protokoll/Riksdagens-snabbprotokoll_H70941/#anf161'], 'dok_titel': ['Protokoll 2019/20:41 Fredagen den 29 november'], 'intressent_id': ['0284192765516']}, 
  
  
  {'valkrets': ['Stockholms kommun'], 'bild_url_192': ['http://data.riksdagen.se/filarkiv/bilder/ledamot/979e9852-69ed-4077-8140-52ab99414a6c_192.jpg'], 'uppgift': [], 'intressent_id_FK': ['014386615025']}, 
  
  {'valkrets': ['Stockholms kommun'], 'bild_url_192': ['http://data.riksdagen.se/filarkiv/bilder/ledamot/979e9852-69ed-4077-8140-52ab99414a6c_192.jpg'], 'uppgift': [], 'intressent_id_FK': ['014386615025']}, 
  
  {'valkrets': ['Stockholms kommun'], 'bild_url_192': ['http://data.riksdagen.se/filarkiv/bilder/ledamot/979e9852-69ed-4077-8140-52ab99414a6c_192.jpg'], 'uppgift': [], 'intressent_id_FK': ['014386615025']}, 
  
  {'valkrets': ['Stockholms kommun'], 'bild_url_192': ['http://data.riksdagen.se/filarkiv/bilder/ledamot/5b7ac02c-0819-426d-bc5d-41b8c21ca4dd_192.jpg'], 'uppgift': [], 'intressent_id_FK': ['0216534495014']}
  ]
```

### Required output

when common object matches
```
{
  "anforande_id": value,
  "dok_datum": value,
  "talare": value,
  "parti": value, 
  "protokoll_url_www": value, 
  "dok_titel": value,
  "intressent_id": value
  "valkrets": value,
  "bild_url_192": value,
  "uppgift": value,
  }
```

when common object does not exist
```
{
  "anforande_id": value,
  "dok_datum": value,
  "talare": value,
  "parti": value, 
  "protokoll_url_www": value, 
  "dok_titel": value,
  "intressent_id": value
  }
```