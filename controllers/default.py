# coding: utf8
# try something like
from gluon.contrib.user_agent_parser import mobilize
@mobilize
def index():
    import uuid
    import urllib2
    import simplejson
    import random
    import operator
    import math

    session.combos = []
    #CREATE NEW GAME_ID
    session.game_id = str(uuid.uuid4())
    session.group_id = session.game_id
    session.past_game_ids = list(set([row.group_id for row in db((db.leaderboard.id>0)).select(db.leaderboard.group_id)]))
    session.past_game_ids.append(session.group_id)
    session.past_game_ids.append('Universal')
    #session.ip_country = urllib2.urlopen("http://ipinfo.io/"+request.client+"/country").read().strip()
    #session.ip_city = urllib2.urlopen("http://ipinfo.io/"+request.client+"/city").read().strip()
    #response.flash = 'Set up a new game!'

    #engine_dict = {'http://google.com/complete/search?output=toolbar&q=':'US',
    #                                                          'http://google.com.au/complete/search?output=toolbar&q=':'AU',
    #                                                          'http://google.co.uk/complete/search?output=toolbar&q=':'UK',
    #                                                          'http://google.co.it/complete/search?output=toolbar&q=':'IT',
    #                                                          'http://google.co.br/complete/search?output=toolbar&q=':'BR',
    #                                                          'http://google.co.jp/complete/search?output=toolbar&q=':'JP'}

    flag_dict = {'US':'http://upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/23px-Flag_of_the_United_States.svg.png',
                 'AUS':'http://upload.wikimedia.org/wikipedia/en/thumb/b/b9/Flag_of_Australia.svg/23px-Flag_of_Australia.svg.png',
                 'UK':'http://upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/23px-Flag_of_the_United_Kingdom.svg.png',
                 'ITA':'http://upload.wikimedia.org/wikipedia/en/thumb/0/03/Flag_of_Italy.svg/23px-Flag_of_Italy.svg.png',
                 'JAP':'http://upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/23px-Flag_of_Japan.svg.png',
                 'BRA':'http://upload.wikimedia.org/wikipedia/en/thumb/0/05/Flag_of_Brazil.svg/23px-Flag_of_Brazil.svg.png',
                 'FRA':'http://upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/23px-Flag_of_France.svg.png',
                 'ARG':'http://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Flag_of_Argentina.svg/23px-Flag_of_Argentina.svg.png',
                 'GER':'http://upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/23px-Flag_of_Germany.svg.png',
                 'ESP':'http://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Flag_of_Spain.svg/23px-Flag_of_Spain.svg.png',
                 'MEX':'http://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Flag_of_Mexico.svg/23px-Flag_of_Mexico.svg.png',
                 'TUR':'http://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/23px-Flag_of_Turkey.svg.png',
                 'VN':'http://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Flag_of_Vietnam.svg/23px-Flag_of_Vietnam.svg.png',
                 'SAF':'http://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Flag_of_South_Africa.svg/23px-Flag_of_South_Africa.svg.png',
                 #'CHN':'http://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png',
                 'RUS':'http://upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/23px-Flag_of_Russia.svg.png',
                 'IND':'http://upload.wikimedia.org/wikipedia/en/thumb/4/41/Flag_of_India.svg/23px-Flag_of_India.svg.png',
				 'KOR':'http://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/23px-Flag_of_South_Korea.svg.png',
				 'CAN':'http://upload.wikimedia.org/wikipedia/en/thumb/c/cf/Flag_of_Canada.svg/23px-Flag_of_Canada.svg.png',
				 'NZ':'http://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Flag_of_New_Zealand.svg/23px-Flag_of_New_Zealand.svg.png',
				 'LI':'http://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Flag_of_Liechtenstein.svg/23px-Flag_of_Liechtenstein.svg.png'
                 }

    geo_dict = {'US':'US',
                 'AUS':'AU',
                 'UK':'GB',
                 'ITA':'IT',
                 'JAP':'JP',
                 'BRA':'BR',
                 'FRA':'FR',
                 'ARG':'AR',
                 'GER':'DE',
                 'ESP':'ES',
                 'MEX':'MX',
                 'TUR':'TR',
                 'VN':'VN',
                 'SAF':'ZA',
                 #'CHN':'CN',
                 'RUS':'RU',
                 'IND':'IN',
				 'KOR':'KR',
				 'CAN':'CA',
				 'NZ':'NZ',
				 'LI':'LI'
                 }

    reverse_geo_dict = {v:k for k, v in geo_dict.items()}

    engine_dict = {'http://google.com/complete/search?output=toolbar&hl=en&q=':'US',
                   'http://google.com.au/complete/search?output=toolbar&hl=en&q=':'AUS',
                   'http://google.co.uk/complete/search?output=toolbar&hl=en&q=':'UK',
                   'http://google.it/complete/search?output=toolbar&hl=it&q=':'ITA',
                   'http://google.co.jp/complete/search?output=toolbar&hl=ja&q=':'JAP',
                   'http://google.com.br/complete/search?output=toolbar&hl=pt-BR&q=':'BRA',
                   'http://google.fr/complete/search?output=toolbar&hl=fr&q=':'FRA',
                   'http://google.com.ar/complete/search?output=toolbar&hl=es&q=':'ARG',
                   'http://google.de/complete/search?output=toolbar&hl=de&q=':'GER',
                   'http://google.es/complete/search?output=toolbar&hl=es&q=':'ESP',
                   'http://google.com.mx/complete/search?output=toolbar&hl=es-419&q=':'MEX',
                   'http://google.com.tr/complete/search?output=toolbar&hl=tr&q=':'TUR',
                   'http://google.com.vn/complete/search?output=toolbar&hl=vi&q=':'VN',
                   'http://google.co.za/complete/search?output=toolbar&hl=es&q=':'SAF',
                   #'http://google.cn/complete/search?output=toolbar&hl=zh-cn&q=':'CHN',
                   'http://google.ru/complete/search?output=toolbar&hl=ru&q=':'RUS',
                   'http://google.co.in/complete/search?output=toolbar&hl=en&q=':'IND',
				   'http://google.co.kr/complete/search?output=toolbar&hl=kr&q=':'KOR',
				   'http://google.ca/complete/search?output=toolbar&hl=en&q=':'CAN',
				   'http://google.co.nz/complete/search?output=toolbar&hl=en&q=':'NZ',
				   'http://google.li/complete/search?output=toolbar&hl=de&q=':'LI'
                   }

    reverse_engine_dict = {v:k for k, v in engine_dict.items()}

    n_rounds_dict = {1:3,2:3,3:2,4:2,5:2,6:1,7:1,8:1,9:1,10:1}

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
                 #'CHN':'gbk',
                 'RUS':'koi8-r',
                 'IND':'latin1',
				 'KOR':'none',
				 'CAN':'latin1',
				 'NZ':'latin1',
				 'LI':'latin1'
                 }

    lang_dict = {'US':'EN',
                 'AUS':'EN',
                 'UK':'EN',
                 'ITA':'IT',
                 'JAP':'JP',
                 'BRA':'PR',
                 'FRA':'FR',
                 'ARG':'ES',
                 'GER':'DE',
                 'ESP':'ES',
                 'MEX':'ES',
                 'TUR':'TR',
                 'VN':'VN',
                 'SAF':'EN',
                 #'CHN':'CN',
                 'RUS':'RU',
                 'IND':'EN',
				 'KOR':'KR',
				 'CAN':'EN',
				 'NZ':'EN',
				 'LI':'DE'
                 }

    search_type_array = {'Classic':'search_term_submit',
                         'Trivia':'category_submit'
                         }

    avatar_list = ['https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRhdYjg-EnyYEjkSeHPZ7Da9hqj7oF0fdZjxaXIBTZw2hqKwgpC'
				   ,'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTbpIVWjEfMXdof6m6-XsF408XjkKfETc3MJoigoslvA-576ymO3g'
				   ,'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxSKE_uDAoVXE5PUadfANnFmnDNUJDSi2b3vWzOjRMIDf9tOkOoA'
				   ,'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSV6aBhczk38wYxkUf2Tz-zGTohHuOJIaLY8LreYMCO1sgBcp6Edg'
				   ,'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQ2rUgIMicIJzh5VlOLgNbsxBDaqlxlHD8adLupyVNaUOdGmLXi'
				   ,'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHhkTi7KylDMEK_xvRSw2YMye6TjzL3MmdTxToadNiPWm9myVFLg'
				   ,'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsCv_npfU7Qp4J21zDWE6-yfsZfqCZP4J7iQHSVid3VWratlcM'
				   ,'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRCKrV-bOSTRvQ3dFwD3ZN3IxKnWLQvEeEj985Nc3VhWV3b-gzylw'
				   ,'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRY_xfznJkxn8OXjc9bQwVVv6NHHYNtb9tsA93ucA_tEXqRXJt53w'
				   ,'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQrXkF1SkkqD-bLwL2QImw1YRIcjO25J3ENGh1WInQX39ojacFy']
	
    if session.game_mode == None:
        session.game_mode = 'Trivia'
    if session.engine == None:
		session.engine = reverse_engine_dict[reverse_geo_dict['US']]
        #if session.ip_country in reverse_geo_dict.keys():
        #    session.engine = reverse_engine_dict[reverse_geo_dict[session.ip_country]]
        #else:
		#	session.engine = reverse_engine_dict[reverse_geo_dict['US']]


    #rows = db((db.trend_pull.engine==engine_dict[session.engine])).select(orderby=~db.trend_pull.id,limitby=(0,10))

    session.latest_trends = [row.trend for row in db((db.trend_pull.engine==engine_dict[session.engine])).select(orderby=~db.trend_pull.id,limitby=(0,10))]
    session.recent_trends = {}
    for trend in session.latest_trends:
        trend_term = trend.replace(" ", "+")
        trend_url = session.engine.replace("/complete/search?output=toolbar&", "/search?q=").replace("?q=", "?") + trend_term
        session.recent_trends[trend] = trend_url
	pass

    if session.player_names == None:
        session.player_names = ''

    form =  SQLFORM.factory(Field('player_names',default=session.player_names),Field('search_engine_location',requires=IS_IN_SET(sorted(engine_dict.items(),key = operator.itemgetter(1)),zero=None,error_message=T('Select a search engine region')),default=session.engine),Field('game_mode',requires=IS_IN_SET(['Classic','Trivia'],zero=None),default=session.game_mode)).process()
    form.element(_type='submit')['_class']='btn btn-primary'


    if form.accepted:

        session.game_mode = form.vars.game_mode
        session.game_id = 'Universal'    #form.vars.game_id
        session.sts = search_type_array[session.game_mode]
        #session.number_of_rounds = int(float(form.vars.number_of_rounds))
        session.player_names = form.vars.player_names
        session.playerlist = list(map(str,form.vars.player_names.split(',')))
        playerlist = []
        for item in session.playerlist:
            playerlist.append(item.strip())
        session.playerlist = playerlist

        if len(session.playerlist)!=len(set(session.playerlist)):
            session.flash = 'Come on now... each name must be unique!'
            redirect(URL('index'))
        if session.player_names != '' and len(session.playerlist) == 1 and session.game_mode == 'Classic':
            session.flash = "This game can only be played alone in Trivia mode, and player names must be seperated by commas"
            redirect(URL('index'))
        if len(session.playerlist) > 10:
            session.flash = 'This is getting out of hand! Please enter up to 10 players.'
            redirect(URL('index'))
        else:
            if session.player_names == '':
                session.playerlist = ['Beavis','Butthead']
            session.player_avatars = {}
            i = 0
            for player in session.playerlist:
                #adj_player = player.replace(" ", "+")
                #searchUrl = 'http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=' + adj_player + '&safe=images' + '&imgsz=medium'  #+ '&imgc=gray'
                #f = urllib2.urlopen(searchUrl)
                #gi_results = simplejson.load(f)
                #if gi_results['responseData']['results'] is None:
                #    n_avatar_options = 0
                #else:
                #    n_avatar_options = len(gi_results['responseData']['results'])
                #if n_avatar_options >= 1:
                #    avatar_index = random.randint(0,(n_avatar_options-1))
                #    image_url = gi_results['responseData']['results'][avatar_index]['unescapedUrl']
                #    adj_image_url = image_url.replace('\u003d', '=')
                #    session.player_avatars[player] = adj_image_url
                #else:
                #    session.player_avatars[player] = 'http://image.spreadshirtmedia.com/image-server/v1/designs/11885448,width=190,height=190.png/y-u-no_design.png'
				session.player_avatars[player] = avatar_list[i]
				i += 1
        session.engine = form.vars.search_engine_location
        session.engine_code = engine_dict[form.vars.search_engine_location]
        session.lang_code = lang_dict[session.engine_code]
        session.engine_flag_url = flag_dict[session.engine_code]
        session.decode_style = decode_dict[session.engine_code]
        session.geo_code = geo_dict[session.engine_code]
        session.game_round_count = 1
        session.round_history = {}
        session.cat_history = {}
        session.q_master_index = 0
        session.loser_avatar_url = 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRGM2Q7ZXIsJ__7OGRX768WxkmDIaW1dy8AyTi37mtuvR0Wzh-n'
        session.number_of_rounds = n_rounds_dict[len(session.playerlist)]
        #initialize total scores
        session.user_total_scores = {}
        for user in session.playerlist:
            session.user_total_scores[user] = 0
        session.max_score = 0
        session.ordered_game_totals = sorted(session.user_total_scores.items(),key = operator.itemgetter(1),reverse = True)
        session.latest_trends = [row.trend for row in db((db.trend_pull.engine==engine_dict[session.engine])).select(orderby=~db.trend_pull.id,limitby=(0,10))]
        session.recent_trends = {}
        for trend in session.latest_trends:
			trend_term = trend.replace(" ", "+")
			trend_url = session.engine.replace("/complete/search?output=toolbar&", "/search?q=").replace("?q=", "?") + trend_term
			session.recent_trends[trend] = trend_url
		#HERE IS WHERE WE STORE GAMES TO THE DB
        db.game_session.insert(time_stamp = request.now, engine=session.engine, player_names=session.player_names,game_rounds=session.number_of_rounds)
        redirect(URL('setup_confirmation'))
    elif form.errors:
        response.flash = 'You got issues!'
        pass


    return locals()

@mobilize
def search_term_submit():

    import urllib2
    from xml.dom import minidom
    import xml.etree.ElementTree
    import random
    import simplejson
    import HTMLParser
    #import io

    session.q_master = session.playerlist[session.q_master_index]
    session.a_playerlist = session.playerlist[(session.q_master_index+1):len(session.playerlist)] + session.playerlist[0:session.q_master_index]
    search_label = session.q_master + ', begin the search'
    form = SQLFORM.factory(Field('search_term',label=search_label,requires=IS_NOT_EMPTY(error_message=T('You have to enter something, man!')))).process(message_onsuccess="Ain't nobody searching for that - try something less specific!",message_onfailure='I know you can do better than that!')
    form.element(_type='submit')['_class']='btn btn-primary'
    form.add_button("Random",URL('generate_random_question'))

    if form.accepted:

        session.search_term = form.vars.search_term
        session.round_count = 1
        session.selected_answers = []
        adj_search_term = request.vars.search_term.replace(" ", "+")
        search_url = session.engine + adj_search_term + '+'
        url_output = urllib2.urlopen(search_url)
        xml_string = url_output.read()
        #xml_doc = minidom.parseString(xml_string)
        #suggestion_list = xml_doc.getElementsByTagName('CompleteSuggestion')

        xml_string = xml_string.replace('<?xml version="1.0"?><toplevel>','')
        xml_string = xml_string.replace('<CompleteSuggestion><suggestion data=','')
        xml_string = xml_string.replace('/></CompleteSuggestion>',',')
        xml_string = xml_string.replace(',</toplevel>','')
        xml_string = xml_string.replace('"','')

        suggestion_list = list(map(str,xml_string.split(',')))
        n_suggestions = len(suggestion_list)

        html_parser = HTMLParser.HTMLParser()
        ##parser = xml.etree.ElementTree.XMLParser(encoding="utf-8")

        if n_suggestions == 10:

                pts_list = list(reversed(range(n_suggestions)))
                ##suggestion_tree = xml.etree.ElementTree.fromstring(xml_string, parser=parser)
                #suggestion_tree = xml.etree.ElementTree.fromstring(xml_string)

                ordered_suggestion_list = list()
                answer_list = {}

                i = 10
                #for data in suggestion_tree.iter('suggestion'):
                #        suggestion = data.get('data')
                #        answer_list[i] = suggestion
                #        ordered_suggestion_list.append(suggestion)
                #        i -= 1

                for suggestion in suggestion_list:
                        if session.decode_style == 'none':
                            answer_list[i] = html_parser.unescape(suggestion)
                            ordered_suggestion_list.append(html_parser.unescape(suggestion))
                        else:
                            answer_list[i] = html_parser.unescape(suggestion.decode(session.decode_style))
                            ordered_suggestion_list.append(html_parser.unescape(suggestion.decode(session.decode_style)))
                        i -= 1

                random_suggestion_list = sorted(ordered_suggestion_list, key=lambda k: random.random())

                session.random_list = {}
                i = 0
                for item in random_suggestion_list:
                    session.random_list[i] = item
                    i += 1

                if len(session.random_list) < 10:
                    redirect(URL('search_term_submit'))
                else:
                    #STORE THE SEARCH TERMS TO THE DB
                    db.search_term.insert(time_stamp = request.now, engine=session.engine, search_term=session.search_term)
                    searchUrl = 'http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=' + adj_search_term + '&safe=images' + '&imgsz=medium' # + '&imgsz=xxlarge'
                    f = urllib2.urlopen(searchUrl)
                    gi_results = simplejson.load(f)
                    try:
                        if gi_results['responseData']['results'] is None:
                            n_results = 0
                        else:
                            n_results = len(gi_results['responseData']['results'])
                        if n_results > 0:
                            image_url = gi_results['responseData']['results'][0]['unescapedUrl']
                            session.adj_image_url = image_url.replace('\u003d', '=')
                        else:
                            session.adj_image_url = 'http://image.spreadshirtmedia.com/image-server/v1/designs/11885448,width=190,height=190.png/y-u-no_design.png'
                    except:
                        session.adj_image_url = 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRjZbDX7PbZX6mdExHbfFN2KJsCJj-N-fYyM_Qkzd8xJRMOj5kw'
                    session.answer_list = answer_list
                    session.player_answers = {}
                    redirect(URL('search_term_execute'))
    if session.game_round_count > len(session.playerlist)*session.number_of_rounds:
        redirect(URL('game_end'))

    return locals()


@mobilize
def category_submit():

    import urllib2
    from xml.dom import minidom
    import xml.etree.ElementTree
    import random
    import simplejson
    import HTMLParser
    #import io

    session.q_master = session.playerlist[session.q_master_index]
    session.a_playerlist = session.playerlist[(session.q_master_index):len(session.playerlist)] + session.playerlist[0:session.q_master_index]
    search_label = session.q_master + ', select a category'

    #rows = db((db.trend_pull.engine==session.engine_code)).select().sort(lambda row: random.random())

    count = db.trend_pull.category.count()
    count_cutoff = 5         #update if we want to increase the cutoff
    rows = db((db.trend_pull.engine==session.engine_code) & (db.trend_pull.category<>"Random")).select(groupby=db.trend_pull.category,having=count>count_cutoff).sort(lambda row: random.random())

    session.category_list = []
    i = 0
    j = 0
    while i <= 7:
        cat_i = rows[j].category
        if cat_i in session.category_list:
            j += 1
        else:
            session.category_list.append(cat_i)
            i += 1
            j +=1

	session.category_counter = 0
	session.auxrows = db((db.auxverb.user_language==session.lang_code)).select().sort(lambda row: random.random())

    if session.game_round_count > len(session.playerlist)*session.number_of_rounds:
        redirect(URL('game_end'))

    return locals()


def generate_category_question():
    import urllib2
    from xml.dom import minidom
    import xml.etree.ElementTree
    import random
    import simplejson
    import HTMLParser

    session.category = request.vars['category']

    #session.category = 'Random'
    if session.category_counter == 0:
        session.catrows = db((db.trend_pull.engine==session.engine_code) & (db.trend_pull.category==session.category)).select().sort(lambda row: random.random())
        session.n_cat_rows = len(session.catrows)


    row_i = 0
    session.found_match = 0
    while (session.found_match == 0) & (row_i < session.n_cat_rows):
        session.cat_trend = session.catrows[row_i].trend
        if session.cat_trend in session.cat_history.keys():
            row_i += 1
        else:
            session.found_match = 1

    if session.found_match == 0 or session.category_counter == 6:
        session.flash = "Sorry, it looks like that category has been exhausted!"
        redirect(URL('category_submit'))
    else:
        session.search_term = session.cat_trend

    session.round_count = 1
    session.selected_answers = []
    adj_search_term = session.search_term.replace(" ", "+")
    adj_search_term = adj_search_term.replace("'","%27")

    if session.category_counter < 5:

        n_rows = len(session.auxrows)

        if session.auxrows[session.category_counter].term_prefix == '':
			search_prefix = str()
        else:
			search_prefix = str(session.auxrows[session.category_counter].term_prefix)
        if str(session.auxrows[session.category_counter].term_suffix) == '':
			search_suffix = str()
        else:
			search_suffix = str(session.auxrows[session.category_counter].term_suffix)
    else:
        search_prefix = str()
        search_suffix = str()



    search_url = session.engine + search_prefix + adj_search_term + search_suffix + '+'
    session.search_term = search_url.split('q=', 1)[1]
    session.search_term = session.search_term.replace('+',' ')

    url_output = urllib2.urlopen(search_url)
    xml_string = url_output.read()

    xml_string = xml_string.replace('<?xml version="1.0"?><toplevel>','')
    xml_string = xml_string.replace('<CompleteSuggestion><suggestion data=','')
    xml_string = xml_string.replace('/></CompleteSuggestion>',',')
    xml_string = xml_string.replace(',</toplevel>','')
    xml_string = xml_string.replace('"','')

    suggestion_list = list(map(str,xml_string.split(',')))

    #xml_doc = minidom.parseString(xml_string)
    #suggestion_list = xml_doc.getElementsByTagName('CompleteSuggestion')
    n_suggestions = len(suggestion_list)

    html_parser = HTMLParser.HTMLParser()

    pts_list = list(reversed(range(n_suggestions)))
    #suggestion_tree = xml.etree.ElementTree.fromstring(xml_string)

    ordered_suggestion_list = list()
    answer_list = {}

    i = 10
    #for data in suggestion_tree.iter('suggestion'):
    #        suggestion = data.get('data')
    #        answer_list[i] = suggestion
    #        ordered_suggestion_list.append(suggestion)
    #        i -= 1
    for suggestion in suggestion_list:
        if session.decode_style == 'none':
            answer_list[i] = html_parser.unescape(suggestion)
            ordered_suggestion_list.append(html_parser.unescape(suggestion))
        else:
            answer_list[i] = html_parser.unescape(suggestion.decode(session.decode_style))
            ordered_suggestion_list.append(html_parser.unescape(suggestion.decode(session.decode_style)))
        i -= 1

    random_suggestion_list = sorted(ordered_suggestion_list, key=lambda k: random.random())

    session.random_list = {}
    i = 0
    for item in random_suggestion_list:
        session.random_list[i] = item
        i += 1

    if len(session.random_list) < 10:
        tries = session.auxrows[session.category_counter].times_ran
        session.auxrows[session.category_counter].update_record(times_ran = tries + 1)
        session.category_counter += 1
        redirect(URL('generate_category_question',vars={'category':session.category}))
    else:
        #db.search_term.insert(time_stamp = request.now, engine=session.engine, search_term=session.search_term)
        if session.category_counter < 6:
			if (search_prefix == '') | (search_suffix == ''):
				successes = session.auxrows[session.category_counter].success
				tries = session.auxrows[session.category_counter].times_ran
				session.auxrows[session.category_counter].update_record(success = successes + 1)
				session.auxrows[session.category_counter].update_record(times_ran = tries + 1)
        searchUrl = 'http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=' + adj_search_term + '&safe=images' +'&imgsz=medium' #+ '&as_filetype=gif'  #+ '&imgsz=xxlarge'
        f = urllib2.urlopen(searchUrl)
        gi_results = simplejson.load(f)

        try:
            if gi_results['responseData']['results'] is None:
                n_results = 0
            else:
                n_results = len(gi_results['responseData']['results'])
            if n_results > 0:
                image_url = gi_results['responseData']['results'][0]['unescapedUrl']
                session.adj_image_url = image_url.replace('\u003d', '=')
            else:
                session.adj_image_url = 'http://image.spreadshirtmedia.com/image-server/v1/designs/11885448,width=190,height=190.png/y-u-no_design.png'
        except:
            session.adj_image_url = 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRjZbDX7PbZX6mdExHbfFN2KJsCJj-N-fYyM_Qkzd8xJRMOj5kw'

    session.answer_list = answer_list
    session.player_answers = {}

    redirect(URL('search_term_execute'))


def generate_random_question():
    import urllib2
    from xml.dom import minidom
    import xml.etree.ElementTree
    import random
    import simplejson
    import HTMLParser

    #isolate search engine
    rows = db(db.search_term.engine==session.engine).select().sort(lambda row: random.random())

    #try finding new random search if game has already contained the one being asked
    n_rows = len(rows)
    row_i = 0
    found_match = 0
    while (found_match == 0) & (row_i < n_rows):
        if rows[row_i].search_term in session.round_history.keys():
            row_i += 1
        else:
            found_match = 1

    if row_i == n_rows:
        session.flash = "Sorry, it looks like you're going to need to come up with something yourself now!"
        redirect(URL('search_term_submit'))
    else:
        session.search_term = rows[row_i].search_term

    session.round_count = 1
    session.selected_answers = []
    adj_search_term = session.search_term.replace (" ", "+")
    adj_search_term = adj_search_term.replace("'","%27")
    search_url = session.engine + adj_search_term + '+'
    url_output = urllib2.urlopen(search_url)
    xml_string = url_output.read()

    xml_string = xml_string.replace('<?xml version="1.0"?><toplevel>','')
    xml_string = xml_string.replace('<CompleteSuggestion><suggestion data=','')
    xml_string = xml_string.replace('/></CompleteSuggestion>',',')
    xml_string = xml_string.replace(',</toplevel>','')
    xml_string = xml_string.replace('"','')

    suggestion_list = list(map(str,xml_string.split(',')))

    #xml_doc = minidom.parseString(xml_string)
    #suggestion_list = xml_doc.getElementsByTagName('CompleteSuggestion')
    n_suggestions = len(suggestion_list)

    html_parser = HTMLParser.HTMLParser()

    pts_list = list(reversed(range(n_suggestions)))
    #suggestion_tree = xml.etree.ElementTree.fromstring(xml_string)

    ordered_suggestion_list = list()
    answer_list = {}

    i = 10
    #for data in suggestion_tree.iter('suggestion'):
    #        suggestion = data.get('data')
    #        answer_list[i] = suggestion
    #        ordered_suggestion_list.append(suggestion)
    #        i -= 1
    for suggestion in suggestion_list:
        if session.decode_style == 'none':
            answer_list[i] = html_parser.unescape(suggestion)
            ordered_suggestion_list.append(html_parser.unescape(suggestion))
        else:
            answer_list[i] = html_parser.unescape(suggestion.decode(session.decode_style))
            ordered_suggestion_list.append(html_parser.unescape(suggestion.decode(session.decode_style)))
        i -= 1

    random_suggestion_list = sorted(ordered_suggestion_list, key=lambda k: random.random())

    session.random_list = {}
    i = 0
    for item in random_suggestion_list:
        session.random_list[i] = item
        i += 1

    if len(session.random_list) < 10:
        session.flash = 'Sorry, our bad... try again'
        redirect(URL('search_term_submit'))
    else:
        #db.search_term.insert(time_stamp = request.now, engine=session.engine, search_term=session.search_term)
        searchUrl = 'http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=' + adj_search_term + '&safe=images' + '&imgsz=medium'
        f = urllib2.urlopen(searchUrl)
        gi_results = simplejson.load(f)

        try:
            if gi_results['responseData']['results'] is None:
                n_results = 0
            else:
                n_results = len(gi_results['responseData']['results'])
            if n_results > 0:
                image_url = gi_results['responseData']['results'][0]['unescapedUrl']
                session.adj_image_url = image_url.replace('\u003d', '=')
            else:
                session.adj_image_url = 'http://image.spreadshirtmedia.com/image-server/v1/designs/11885448,width=190,height=190.png/y-u-no_design.png'
        except:
            session.adj_image_url = 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRjZbDX7PbZX6mdExHbfFN2KJsCJj-N-fYyM_Qkzd8xJRMOj5kw'

        session.answer_list = answer_list
        session.player_answers = {}
        #session.flash = 'Complete the search'
        redirect(URL('search_term_execute',vars={'search_term':session.search_term}))

    return locals()

def image_store():
    import urllib2
    import simplejson
    import cStringIO

    #fetcher = urllib2.build_opener()
    searchTerm = 'michael+jordan'
    searchUrl = 'http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=' + searchTerm + '&imgc=gray'
    f = urllib2.urlopen(searchUrl)
    gi_results = simplejson.load(f)
    image_url = gi_results['responseData']['results'][0]['tbUrl']
    #file = cStringIO.StringIO(urllib2.urlopen(image_url).read())
    #img = Image.open(file)
    adj_image_url = image_url.replace('\u003d', '=')
    test = IMG(_src=URL(adj_image_url),_alt='test')
    test2 = IMG(_src='http://t3.gstatic.com/images?q=tbn:ANd9GcQC8-5IHcAc4lc7deD7y4siuO37AixOAzSikpzM4OpGVVe5FdRnvPteA7c',_alt='test')
    test3 = session.player_avatars
    return locals()

@mobilize
def search_term_execute():
    import math

    if session.round_count <= len(session.a_playerlist):
        answer_player = session.a_playerlist[session.round_count - 1]
        session.answer_label = answer_player + ', choose most popular'

    #response.flash = 'Complete the search'
    #remove already selected answers from answer_selection list
    inverted_random_list = {v:k for k, v in session.random_list.items()}

    for entry in session.selected_answers:
        del inverted_random_list[entry]

    filtered_random_list = {v:k for k, v in inverted_random_list.items()}

    form = SQLFORM.factory(Field('choose_most_popular',label=session.answer_label,requires=IS_IN_SET(filtered_random_list,error_message=T('You have to pick something, man!')))).process()
    form.element(_type='submit')['_class']='btn btn-primary'

    if (form.accepted) & (session.round_count <= len(session.a_playerlist)):
        session.round_count += 1
        session.player_answers[answer_player] = filtered_random_list[int(form.vars.choose_most_popular)]
        session.selected_answers.append(filtered_random_list[int(form.vars.choose_most_popular)])
        redirect(URL('search_term_execute',vars={'search_term':session.search_term}))
    elif session.round_count > len(session.a_playerlist):
        if session.q_master_index == (len(session.playerlist) - 1):
            session.q_master_index = 0
        else:
            session.q_master_index += 1

        inv_answer_list = {v:k for k, v in session.answer_list.items()}
        session.user_round_scores = {}
        session.user_round_answers = {}
        for user in session.a_playerlist:
            user_round_answer = session.player_answers[user]
            user_round_score = inv_answer_list[user_round_answer]
            session.user_round_scores[user] = user_round_score
            session.user_total_scores[user] += user_round_score
            session.user_round_answers[user] = user_round_answer
            user_total_scores = session.user_total_scores

        if session.game_mode == 'Trivia':
            session.cat_history[session.cat_trend] = (session.user_round_scores,session.user_round_answers)

        session.round_history[session.search_term] = (session.user_round_scores,session.user_round_answers)
        session.inv_user_round_answers = {v:k for k, v in session.user_round_answers.items()}
        session.game_round_count += 1
        inverted_total_scores = {v:k for k, v in session.user_total_scores.items()}
        session.max_score = max(inverted_total_scores)
        session.group_score = sum(inverted_total_scores)
        redirect(URL('score_update'))
    elif form.errors:
        response.flash = "Oh no you didn't!"
        pass
    else:
        pass
    return locals()

@mobilize
def score_update():
    import operator
    session.ordered_game_totals = sorted(session.user_total_scores.items(),key = operator.itemgetter(1),reverse = True)
    sorted_answers = sorted(session.answer_list.items(),key = operator.itemgetter(0),reverse = True)

    answer_link_array = {}
    for answer in sorted_answers:
        link_term = answer[1].replace (" ", "+")
        link_url = session.engine.replace("/complete/search?output=toolbar&", "/search?q=").replace("?q=", "?") + link_term
        answer_link_array[answer[0]] = link_url

    return locals()

@mobilize
def game_end():
    import datetime
    import scipy.stats as stats
    #ordered_game_totals = sorted(session.user_total_scores.items(),key = operator.itemgetter(1),reverse = True)
    for player in session.ordered_game_totals:
        db.leaderboard.insert(player_name = player[0],group_id = session.group_id,game_mode = session.game_mode,engine = session.engine,final_score = player[1],group_score = session.group_score,n_rounds = session.number_of_rounds,time_stamp = datetime.datetime.now(),n_players = len(session.playerlist))
    if session.game_id == 'Universal':
		session.past_individual_scores = [row.final_score for row in db((db.leaderboard.engine==session.engine)&(db.leaderboard.n_rounds==session.number_of_rounds)&(db.leaderboard.n_players==len(session.playerlist))&(db.leaderboard.game_mode==session.game_mode)).select(db.leaderboard.final_score)]
    else:
		session.past_individual_scores = [row.final_score for row in db((db.leaderboard.engine==session.engine)&(db.leaderboard.n_rounds==session.number_of_rounds)&(db.leaderboard.n_players==len(session.playerlist))&(db.leaderboard.game_mode==session.game_mode)&(db.leaderboard.group_id==session.game_id)).select(db.leaderboard.final_score)]
    session.past_individual_scores = map(int, session.past_individual_scores)
    session.individual_scores = {}
    for player in session.ordered_game_totals:
		session.individual_scores[player[0]] = int(stats.percentileofscore(session.past_individual_scores,player[1]))

    if session.game_id == 'Universal':
		session.past_group_scores = [row.group_score for row in db((db.leaderboard.engine==session.engine)&(db.leaderboard.n_rounds==session.number_of_rounds)&(db.leaderboard.game_mode==session.game_mode)&(db.leaderboard.n_players==len(session.playerlist))).select(db.leaderboard.group_score,groupby=db.leaderboard.group_id)]
    else:
		session.past_group_scores = [row.group_score for row in db((db.leaderboard.engine==session.engine)&(db.leaderboard.n_rounds==session.number_of_rounds)&(db.leaderboard.game_mode==session.game_mode)&(db.leaderboard.group_id==session.game_id)&(db.leaderboard.n_players==len(session.playerlist))).select(db.leaderboard.group_score,groupby=db.leaderboard.group_id)]
    session.past_group_scores = map(int, session.past_group_scores)
    session.group_percentile_score = int(stats.percentileofscore(session.past_group_scores,session.group_score))
    session.game_complete = 1
    return locals()

@mobilize
def setup_confirmation():
    response.flash = 'Are you happy with these settings?'
    #session.flash = 'Suggest a search term'
    return locals()

def trend_pull():
    from bs4 import BeautifulSoup
    import requests

    url = 'www.google.com.au/trends/hottrends/atom/hourly'

    scrape  = requests.get("http://" +url)
    data = scrape.text

    return locals()

def get_category():
    #from lxml import html
    #import requests

    #page = requests.get('https://www.google.com/search?q=pink%20floyd')
    #tree = html.fromstring(page.text)
    #buyers = tree.xpath('//div[@title="_gdf kno-fb-ctx"]/text()')

    #import urllib2
    #from bs4 import BeautifulSoup
    #import requests

    #url = 'www.google.com/search?q=pink%20floyd'
    #scrape  = requests.get("http://" +url)
    #data = scrape.text

    #string = '<div class="_gdf kno-fb-ctx" data-ved="'

    #soup = BeautifulSoup(data)
    #test1 = data[0]
    #test2 = len(data)
    #response = soup.findAll('div',{'class':'s'})
    #soup = bs4.BeautifulSoup(urllib2.urlopen('https://www.google.com/search?q=pink%20floyd').read())

    #import sys
    #from PyQt4.QtGui import *
    #from PyQt4.QtCore import *
    #from PyQt4.QtWebKit import *

    #app = QApplication(sys.argv)
    #QWebPage
    #url = 'www.google.com/search?q=pink%20floyd'
    #test = QUrl(url)
    #test2 = QtNetwork.QNetworkRequest()
    #loadFinished.connect(self._loadFinished)
    #test = Render(url)
    #app.quit()


    return locals()

def how_to_play():
    return locals()

def faq():
    return locals()

def about():
    player_avatars = {'Larry': 'http://t1.gstatic.com/images?q=tbn:ANd9GcR0g14raRRR84WCT_x9OH-Rl-S2bTS_xGNTm6a_R2VNj97y5vE-llEZ6YPz', 'Curly': 'http://t2.gstatic.com/images?q=tbn:ANd9GcRziR6fUxxUdQTO0IgCFUPG1U4_DEos8czhxRkl_r4x3Szi6S-Rw1eGUY4', 'Moe': 'http://t3.gstatic.com/images?q=tbn:ANd9GcQLvXOKrqIDh1dx9kbQmm53PKEtv_mX96d_Bp6Gy-oI3sbkBfdL1hbf_pWB'}
    return locals()

def errorpage():
    from gluon.tools import Mail
    mail = Mail()
    mail.settings.server = 'smtp.gmail.com:587'
    mail.settings.sender = 'playtotm@gmail.com'
    mail.settings.login = 'playtotm@gmail.com:b3tt3rProtection'
    mail.send(to=['playtotm@gmail.com'],subject='ERROR',message='dev error...')
    return locals()


#TODO create money
