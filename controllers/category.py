from bs4 import BeautifulSoup
import urllib2
import requests
import datetime


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
			   'http://google.co.in/':'IND',
			   'http://google.co.kr/':'KOR',
			   'http://google.ca/':'CAN',
			   'http://google.co.nz/':'NZ',
			   'http://google.li/':'LI'
               }


hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
   'Accept-Encoding': 'none',
   'Accept-Language': 'en-US,en;q=0.8',
   'Connection': 'keep-alive'}

insert_array = {}
insert_row = 0

for engine in engine_array:
    
    url = engine + 'trends/hottrends/atom/hourly'
    engine_code = engine_array[engine]
    scrape  = requests.get(url)
    scrape_time = datetime.datetime.now()
    data = scrape.text
    array = data.split("</a>")
    
    terms = []
    categorylist = []

    for entry in array:
        term_entry = entry.rfind('>') + 1
        terms.append(entry[term_entry:])
    
    url_base = engine + 'search?q='
    
    term_count = 0
    entry_count = 0
	
    #for term in terms[0:4]:
    while (term_count <= len(terms) - 1) & (entry_count <= 4):

        term = terms[term_count]
		
        if len(db((db.trend_pull.engine == engine_code) & (db.trend_pull.trend == term)).select()) == 0:
            adj_term = term.replace(" ", "+")
            adj_term = adj_term.replace("'","%27")
            url = (url_base + adj_term).encode('utf-8')

            req = urllib2.Request(url, headers=hdr)
            data = urllib2.urlopen(req).read()

            page = BeautifulSoup(data,'html.parser')
            page_string = str(page)

            category_base = page_string.split('span class="kno-fb-ctx" data-ved=', 1)[-1]
            category_string = category_base.split('</span></div>', 1)[0]
            category_result = category_string.split('>', 1)[-1]
            #entry_base = page_string.split('kno-ecr-pt kno-fb-ctx', 1)[-1]
            #entry_string = entry_base.split('</div>', 1)[0]
            #entry_result = entry_string.split('>', 1)[-1]

            if len(category_result) > 50:
                category = "Random"
                categorylist.append('no category')
                #db.trend_pull.insert(time_stamp = scrape_time, engine = engine_array[engine],trend = term, category = category)
                entry_count += 1
            else:
                category = category_result
                categorylist.append(category)
                #term = entry_result
                #db.trend_pull.insert(time_stamp = scrape_time, engine = engine_array[engine],trend = term, category = category)
                entry_count += 1

            insert_array[insert_row] = [scrape_time,engine_array[engine],term,category]
            insert_row += 1
        term_count += 1

    #print(engine)
    #print(terms[0:term_count])
    #print(categorylist)
print(insert_array)

print("database updating...")
print(datetime.datetime.now())
	
for insert in insert_array:
	db.trend_pull.insert(time_stamp = insert_array[insert][0], engine = insert_array[insert][1],trend = insert_array[insert][2], category = insert_array[insert][3])

print(datetime.datetime.now())
