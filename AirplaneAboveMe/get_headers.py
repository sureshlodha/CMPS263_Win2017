import csv

with open('flights.csv', 'r') as f:
	d_reader = csv.DictReader(f)
	
	headers = d_reader.fieldnames

print headers