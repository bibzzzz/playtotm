from bs4 import BeautifulSoup
import urllib2
import requests
import datetime

db = DAL('sqlite://storage.sqlite')

engine_array = {'http://google.com/':'US',
               #'http://google.com.au/':'AUS',
               'http://google.co.uk/':'UK',
               #'http://google.it/':'ITA',
               'http://google.co.jp/':'JAP',
               #'http://google.com.br/':'BRA',
               'http://google.fr/':'FRA'
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

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

db = category.importdb()

categorylist = []

for engine in engine_array:

    url = engine + 'trends/hottrends/atom/hourly'
    decode_style = decode_dict[engine_array[engine]]

    scrape  = requests.get(url)
    scrape_time = datetime.datetime.now()
    data = scrape.text
    array = data.split("</a>")

    terms = []

    for entry in array:
        term_entry = entry.rfind('>') + 1
        terms.append(entry[term_entry:])

        url_base = engine + 'search?q='

        for term in terms[0:4]:

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

            if len(category_result) > 50:
                category = "None"
            else:
                category = category_result
            db.trend_pull.insert(time_stamp = scrape_time, engine = engine_array[engine],trend = term, category = category)
            categorylist.append(category)