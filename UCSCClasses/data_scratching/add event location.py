import json

events_json = open('eeee.json').read()
events_data = json.loads(events_json)
location_json = open('events_locations2.json').read()
location_data = json.loads(location_json)

for item in events_data:
	for location in location_data:
		if item['title']== location['title']:
			item['location']= location['location']


for item in events_data:
	try:
		print item['location']
	except:
		item['location'] = 'null'
for item in events_data:
	print 	item['date']	
 