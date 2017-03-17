import json

json_data = open('data11111111.json').read()
data = json.loads(json_data)
count= 0
for item in data:
	if item['Day_And_Time']!= " TBA To Be Arranged" and "Cancelled" and "TBA" not in item :
		aa,bb = item['Day_And_Time'].split()
		if  bb !="Cancelled":
			cc,dd = bb.split('-')
			start,ff= cc.split(':')
			end,gg = dd.split(':')
			if "00" not in gg:
				end = int(end)+1
			if "PM" in dd and "12" not in dd:
				end = int(end)+12
			if "PM" in cc and "12" not in cc:
				start = int(start)+12	
			item['starttime'] =int(start)
			item['endtime'] = int(end)
			# print item['starttime']
			count= count+1


	# item['Day_And_Time']=item['Day_And_Time'].replace("MWF ","MoWeFr ").replace("MW ","MoWe ").replace("WF ","WeFr ").replace("M ","Mo ").replace("W ","We ").replace("F ","Fr ")

print count
# with open('data11111111.json', 'w') as outfile:
#     json.dump(data, outfile)

print data











