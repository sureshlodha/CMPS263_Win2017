import json

json_data = open('data11111111.json').read()
count = 0
data = json.loads(json_data)

for item in data: 	
	a,b = item['Capacity'].split('E')
	item['Capacity']=a
	c,d = item['Capacity'].split('of')
	c = int(c)
	d = int(d)
	if c>d:
		item['Capacity'] = c
	else:
		item['Capacity'] = d
	item['Capacity']=int(item['Capacity'])
	print item['Capacity']
	count= count+1
print count	


with open('data11111111.json', 'w') as outfile:
    json.dump(data, outfile)