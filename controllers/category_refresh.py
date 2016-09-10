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

print session.updated_categories
