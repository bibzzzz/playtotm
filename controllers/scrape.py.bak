def scrape():
    import requests
    import datetime
    from bs4 import BeautifulSoup
    import urllib2

    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

    engine_array = {'http://google.com/':'US',
                   'http://google.com.au/':'AUS',
                   'http://google.co.uk/':'UK',
                   'http://google.it/':'ITA',
                   'http://google.co.jp/':'JAP',
                   'http://google.com.br/':'BRA',
                   'http://google.fr/':'FRA',
                   'http://google.com.ar/':'ARG',
                   'http://google.de/':'GER',
                   'http://google.es/':'ESP',
                   'http://google.com.mx/':'MEX',
                   'http://google.com.tr/':'TUR',
                   'http://google.com.vn/':'VN',
                   'http://google.co.za/':'SAF',
                   'http://google.cn/':'CHN',
                   'http://google.ru/':'RUS',
                   'http://google.co.in/':'IND'
                   }

    
    entrylist = []
    categorylist = []

    for search_engine in engine_array:
        url = search_engine + 'trends/hottrends/atom/hourly'
        scrape  = requests.get(url)
        scrape_time = datetime.datetime.now()
        data = scrape.text
        array = data.split("</a>")

        for entry in array:
            entry_part = entry.rfind('>') + 1
            adj_search_term = entry[entry_part:].replace(" ", "+")
            url = search_engine + 'search?q=' + adj_search_term
            req = urllib2.Request(url, headers=hdr)
            req_data = urllib2.urlopen(req).read()

            page = BeautifulSoup(req_data,'html.parser')
            page_string = str(page)

            category_base = page_string.split('_gdf kno-fb-ctx', 1)[-1]
            category_string = category_base.split('</div>', 1)[0]
            category_result = category_string.split('>', 1)[-1]
			
			#entry_base = page_string.split('kno-ecr-pt kno-fb-ctx', 1)[-1]
			#entry_string = entry_base.split('</div>', 1)[0]
            #entry_result = entry_string.split('>', 1)[-1]
	
            if len(category_result) > 50:
                category_entry = "None"
				
            else:
                category_entry = category_result
				#entry = entry_result
                
            db.trend_pull.insert(time_stamp = scrape_time, engine = engine_array[search_engine],trend = entry[entry_part:].replace("'","%27"), category = 'none')
            entrylist.append(entry[entry_part:].replace("'","%27"))
            categorylist.append(category_entry)

    return locals()

def categorise():
    from bs4 import BeautifulSoup
    import urllib2
    import requests
    import datetime

    
    engine_array = {'http://google.com/':'US',
                   #'http://google.com.au/':'AUS',
                   'http://google.co.uk/':'UK',
                   #'http://google.it/':'ITA',
                   #'http://google.co.jp/':'JAP'
                   #'http://google.com.br/':'BRA',
                   #'http://google.fr/':'FRA',
                   #'http://google.de/':'GER'
                   }
    
    decode_dict = {'US':'latin1',
                 'AUS':'latin1',
                 'UK':'latin1',
                 'ITA':'latin1',
                 'JAP':'932',
                 'BRA':'latin1',
                 'FRA':'latin1',
                 'ARG':'latin1',
                 'GER':'latin1',
                 'ESP':'latin1',
                 'MEX':'latin1',
                 'TUR':'latin1',
                 'VN':'none',
                 'SAF':'latin1',
                 'CHN':'gbk',
                 'RUS':'koi8-r',
                 'IND':'latin1'
                 }
    
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

    categorylist = []
    
    for engine in engine_array:
        
        url = engine + 'trends/hottrends/atom/hourly'
        decode_style = decode_dict[engine_array[engine]]
        engine_code = engine_array[engine]
        scrape  = requests.get(url)
        scrape_time = datetime.datetime.now()
        data = scrape.text
        array = data.split("</a>")
        
        terms = []

        for entry in array:
            entry = 'Man Utd'
            term_entry = entry.rfind('>') + 1
            terms.append(entry[term_entry:])
        
        url_base = engine + 'search?q='
        
        for term in terms[0:4]:
            
            if len(db((db.trend_pull.engine == engine_code) & (db.trend_pull.trend == term)).select()) == 0:
                adj_term = term.replace(" ", "+")
                adj_term = adj_term.replace("'","%27")
                url = (url_base + adj_term).encode('utf-8')

                req = urllib2.Request(url, headers=hdr)
                data = urllib2.urlopen(req).read()

                page = BeautifulSoup(data,'html.parser')
                page_string = str(page)

                category_base = page_string.split('_gdf kno-fb-ctx', 1)[-1]
                category_string = category_base.split('</div>', 1)[0]
                category_result = category_string.split('>', 1)[-1]
                entry_base = page_string.split('kno-ecr-pt kno-fb-ctx', 1)[-1]
                entry_string = entry_base.split('</div>', 1)[0]
                entry_result = entry_string.split('>', 1)[-1]

                if len(category_result) > 50:
                    category = "Random"
                else:
                    category = category_result
                    term = entry_result
                    entry_term = term.replace("'","%27")
                    entry_term = entry_term.replace(" ", "+")
					
                if len(db((db.trend_pull.engine == engine_code) & (db.trend_pull.trend == term)).select()) == 0:
					db.trend_pull.insert(time_stamp = scrape_time, engine = engine_array[engine],trend = term, category = category)
					categorylist.append(category)
                else:
					categorylist.append('already classified')
            
    return locals()
