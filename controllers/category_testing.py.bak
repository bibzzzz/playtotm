def cat_test():

    count = db.trend_pull.category.count()
    count_cutoff = 3          #update if we want to increase the cutoff
    session.rows = db(((db.trend_pull.engine == 'US') | (db.trend_pull.engine == 'UK') | (db.trend_pull.engine == 'AUS')) & (db.trend_pull.category<>"Random")).select(db.trend_pull.category,db.trend_pull.engine,groupby=db.trend_pull.category|db.trend_pull.engine,orderby=db.trend_pull.category|db.trend_pull.engine)

    session.recat_dict = {'1995 film':'Film'
				  ,'1996 film':'Film'
				  ,'1997 film':'Film'
				  ,'1998 film':'Film'
				  ,'1999 film':'Film'
				  ,'2000 film':'Film'
				  ,'2008 film':'Film'
				  ,'2009 film':'Film'
				  ,'2010 film':'Film'
				  ,'2011 film':'Film'
				  ,'2012 film':'Film'
				  ,'2013 film':'Film'
				  ,'2014 film':'Film'
				  ,'2015 film':'Film'
				  ,'2016 film':'Film'
				  ,'Film series':'Film'
				  ,'Film actor':'Actor'
				  ,'Film actress':'Actress'
				  ,'Airline company':'Airline'
				  ,'American TV Program':'American television'
				  ,'American TV program':'American television'
				  ,'American Television Series':'American television'
				  ,'American comedy series':'American television'
				  ,'American television program':'American television'
				  ,'American television series':'American television'
				  ,'American television show':'American television'
				  ,'Australian TV program':'Australian television'
				  ,'Australian TV series':'Australian television'
				  ,'Australian television program':'Australian television'
				  ,'Australian television series':'Australian television'
				  ,'Australian television show':'Australian television'
				  ,'TV Episode':'General television'
				  ,'TV Journalist':'General television'
				  ,'TV Network':'General television'
				  ,'TV Personality':'General television'
				  ,'Television Network':'General television'
				  ,'Television Personality':'General television'
				  ,'Television Program Creator':'General television'
				  ,'Television broadcasting company':'General television'
				  ,'Television host':'General television'
				  ,'Television network':'General television'
				  ,'Television personality':'General television'
				  ,'Television presenter':'General television'
				  ,'Television producer':'General television'
				  ,'Television station':'General television'
				  ,'Television actress':'Actress'
				  ,'Television actor':'Actor'
				  ,'American football linebacker':'American football'
				  ,'American football cornerback':'American football'
				  ,'American football defensive end':'American football'
				  ,'American football defensive tackle':'American football'
				  ,'American football strong safety':'American football'
				  ,'American football quarterback':'American football'
				  ,'American football running back':'American football'
				  ,'American football tight end':'American football'
				  ,'American football wide receiver':'American football'
				  ,'Australian Federal MP':'Australian Politician'
				  ,'Australian Senator':'Australian Politician'
				  ,'Consumer electronics company':'Company'
				  ,'Fast food restaurant company':'Company'
				  ,'Supermarket company':'Company'
				  ,'Restaurant company':'Company'
				  ,'Retail company':'Company'
				  ,'Retail-store company':'Company'
				  ,'Retail-Store company':'Company'
				  ,'company':'Company'
				  ,'NCAA Basketball Team':'Basketball'
				  ,'Basketball Player':'Basketball'
				  ,'Basketball player':'Basketball'
				  ,'Basketball Team':'Basketball'
				  ,'Basketball team':'Basketball'
				  ,'Basketball Coach':'Basketball'
				  ,'Baseball player':'Baseball'
				  ,'Baseball Player':'Baseball'
				  ,'Baseball Team':'Baseball'
				  ,'Baseball team':'Baseball'
				  ,'Video game':'Video games'
				  ,'Video game series':'Video games'
				  ,'Country in Africa':'Country'
				  ,'Country in Asia':'Country'
				  ,'Country in Europe':'Country'
				  ,'Country in Oceania':'Country'
				  ,'Professional golfer':'Golfer'
				  ,'Boxer':'Professional Boxer'
				  ,'Rock band':'Band'
				  ,'Non-profit association':'Nonprofit organization'
				  ,'Radio DJ':'DJ'
				  ,'Snake':'Animal'
				  ,'Soccer Player':'Soccer'
				  ,'Soccer player':'Soccer'
				  ,'Soccer club':'Soccer'
				  ,'Soccer team':'Soccer'
				  ,'Sports Columnist':'Sports Reporter'
				  ,'Freestyle swimmer':'Swimmer'
				  }


    return locals()

def cat_refresh():
	
	rules_dict = {'football':'Football'
				  ,'american football':'American football'
				  ,'boxer':'Boxing'
				  ,'soccer':'Soccer'
				  ,'rugby':'Rugby'
				  ,'swimmer':'Swimming'
				  ,' dj':'DJ'
				  ,'golf':'Golf'
				  ,'video game':'Video games'
				  ,'basketball':'Basketball'
				  ,'baseball':'Baseball'
				  ,'ice hockey':'Ice hockey'
				  ,'cricket':'Cricket'
				  ,'company':'Company'
				  ,'television':'Television'
				  ,'television':'Television'
				  ,' tv':'Television'
				  ,'american comedy series':'Television'
				  ,'airline':'Airline'
				  ,'country':'Geography'
				  ,'film':'Film'
				  ,'novel by ':'Literature'
				  ,'book by ':'Literature'
				  #,'books':'Literature'   #used for correction
				  ,'comic':'Comic books'
				  ,'city in ':'Geography'
				  ,'actor':'Actor'
				  ,'actress':'Actress'
				  ,' mp':'Politics'
				  ,'senator':'Politics'
				  ,'politician':'Politics'
				  ,'president of ':'Politics'
				  ,'political':'Politics'
				  ,'premier of ':'Politics'
				  ,'prime minister of ':'Politics'
				  ,'mayor of ':'Politics'
				  ,'secretary of state':'Politics'
				  ,'radio':'Radio'
				  ,'stand-up comedian':'Comedian'
				  ,'non-profit association':'Non-profit organization'
				  ,'rock band':'Band'
				  ,'business':'Businessperson'
				  ,'capital of ':'Geography'
				  ,'town in ':'Geography'
				  #,'state':'Geography'  #concern for any catogeries containing 'United States'
				  ,'territory':'Geography'
				  ,'borough':'Geography'
				  ,'island in ':'Geography'
				  ,'river in ':'Geography'
				  ,'airport in ':'Geography'
				  ,'stadium in ':'Geography'
				  ,'college in ':'Geography'
				  ,'university in ':'Geography'
				  ,'neighborhood in ':'Geography'
				  ,'neighbourhood in ':'Geography'
				  ,'commune in ':'Geography'
				  ,'arena in ':'Geography'
				  ,'ski resort in ':'Geography'
				  ,'shopping centre in ':'Geography'
				  ,'designer':'Designer'
				  ,'rapper':'Hip-hop artist'
				  ,'dog breed':'Animal'
				  ,'snake':'Animal'
				  ,'fashion model':'Model'
				  ,'tennis':'Tennis'
				  }
	
	rows = db((db.trend_pull.category<>"Random")).select()
	session.updated_categories = []


	for row in rows:
		category = row.category
		for rule in rules_dict:
			if rule in row.category.lower():
				category = rules_dict[rule]
				row.update_record(category=category)
				session.updated_categories.append(category)

#handle other categories
		if row.category.lower() == 'city':
			category = 'Geography'
			row.update_record(category=category)
			session.updated_categories.append(category)
		
		if row.category.lower() == 'state':
			category = 'Geography'
			row.update_record(category=category)
			session.updated_categories.append(category)
	return locals()

def update_db():
	db(db.auxverb.id==392).delete()
	#db((db.trend_pull.id>=26806)&(db.trend_pull.id<=27892)).delete()
