import json

json_data = open('data11111111.json').read()
count = 0
data = json.loads(json_data)
all_time = []
duplicate_location= ["TA Studio","TA Lecture","TA Mainstage","TA 2nd Stage","TA Offices","TA Foundry",]
duplicate_location2=["Martial Arts","Fitness/Wellness","East Field","Dance Studio","E Racquet Ct","E Tennis Ct","E Racquet Ct","East Gym","OPERS Conference","50 Mtr Pool",]
for item in data: 
	if 'E Baskin' in item['Class_Location']:
		item['Class_Location']=item['Class_Location'].replace ('E Baskin','J Baskin Engr')
	for ii in duplicate_location:
		if ii in item['Class_Location']:
			item['Class_Location']= item['Class_Location']+'  (Theater Arts)'
	for ee in duplicate_location2:
		if ee in item['Class_Location']:
			item['Class_Location']= item['Class_Location']+'  (East field)'
	# print item['Class_Location']
	count = count+1
print count

with open('data11111111.json', 'w') as outfile:
    json.dump(data, outfile)






