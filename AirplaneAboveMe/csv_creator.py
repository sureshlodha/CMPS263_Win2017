#Script by Patrick Cudahy

#Commented out sections of are for generating the csvfile
#and are switched out for appending data. The apiKey will
#no longer be functional as of 3/13. The script is meant
#be paired with psLogFlights.ps1 to run every 30 min with
#sys.argv[1] being the number of iterations.

import sys
from suds import null, WebFault
from suds.client import Client
import logging
import csv
import time


username = 'pcudahy'
apiKey   = '12345'
url      = 'http://flightxml.flightaware.com/soap/FlightXML2/wsdl'


def main():
	start = time.time()

	with open('flights.csv', 'r') as f:
		d_reader = csv.DictReader(f)
		
		fieldnames = d_reader.fieldnames

	logging.basicConfig(level=logging.INFO)
	api = Client(url, username=username, password=apiKey)
	api.service.SetMaximumResultSize("1000")

	#Planes in a square that covers California
	result = api.service.SearchBirdseyeInFlight("{range lat 34.28 41.87} {range lon -122.37 -117}", 1000, 0)
	flights = result['aircraft']
	# fieldnames = []
	with open('flights.csv', 'a') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames)

		for item in flights:
			row = {}
			for data in item:
				# fieldnames.append(data[0])
				row[data[0]] = data[1]
			# fieldnames.append('timePeriod')
			row['timePeriod'] = sys.argv[1]
			writer.writerow(row)

	end = time.time()
	print 'Time Period', sys.argv[1], ': ', (end - start)
	# with open('flights.csv', 'a') as csvfile:
	# 	writer = csv.DictWriter(csvfile, fieldnames)

	# 	writer.writeheader()
	# 	writer.writerow(row)
	

if __name__ == "__main__":
	main()