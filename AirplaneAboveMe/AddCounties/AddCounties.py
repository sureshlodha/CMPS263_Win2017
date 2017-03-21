from censusgeocode import CensusGeocode
import csv
import time

cg = CensusGeocode()

start = time.time()
with open('flights2.csv', 'r') as f:
	d_reader = csv.DictReader(f)
	
	fieldnames = d_reader.fieldnames
	fieldnames.append('county')

	with open('flights.csv', 'a') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames)

		# writer.writeheader()

		for num, row in enumerate(d_reader):
			if num % 100 == 0:
				print(num, "rows processed")
			try:
				result = cg.coordinates(x=row['longitude'], y=row['latitude'])

				county = result[0]['Counties']
				county_name = county[0]['NAME']

				new_row = row
				new_row['county'] = county_name

				writer.writerow(new_row)
			except:
				continue