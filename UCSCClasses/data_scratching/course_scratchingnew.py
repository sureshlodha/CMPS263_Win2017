from lxml import html
import requests
import mechanize
import json

page = html.parse('http://registrar.ucsc.edu/catalog/programs-courses/course-descriptions/art.html')
base_url = 'http://registrar.ucsc.edu/catalog/programs-courses/course-descriptions/'
all_data = []
wrong_data = []
count = 0
# all_subject = ['ACEN', 'AMST', 'ANTH', 'APLX', 'AMS', 'ARAB', 'ART', 'ARTG', 'ASTR', 'BIOC', 'BIOL', 'BIOE', 'BME', 'CRSN', 'CHEM', 'CHIN', 'CLEI', 'CLNI', 'CLTE', 'CMMU', 'CMPM', 'CMPE', 'CMPS', 'COWL', 'LTCR', 'CRES', 'CRWN', 'DANM', 'EART', 'ECON', 'EDUC', 'EE', 'ENGR', 'LTEL', 'ENVS', 'ETOX', 'FMST', 'FILM', 'FREN', 'LTFR', 'GAME', 'GERM', 'LTGE', 'GREE', 'LTGR', 'HEBR', 'HNDI', 'HIS', 'HAVC', 'HISC', 'HUMN', 'ISM', 'ITAL', 'LTIT', 'JAPN', 'JWST', 'KRSG', 'LAAD', 'LATN', 'LALS', 'LTIN', 'LGST', 'LING', 'LIT', 'MATH', 'MERR', 'METX', 'LTMO', 'MUSC', 'OAKS', 'OCEA', 'PHIL', 'PHYE', 'PHYS', 'POLI', 'PRTR', 'PORT', 'LTPR', 'PSYC', 'PUNJ', 'RUSS', 'SCIC', 'SOCD', 'SOCS', 'SOCY', 'SPAN', 'SPHS', 'SPSS', 'LTSP', 'STEV', 'TIM', 'THEA', 'UCDC', 'WMST', 'LTWL', 'WRIT', 'YIDD']
#len(all_subject) = 97

br = mechanize.Browser()
br.open("https://pisa.ucsc.edu/cs9/prd/sr9_2013/index.php")

for major in page.xpath('//*[@id="subNav"]/ul/li[14]/ul/li[3]/ul/*'):
	major_page= html.parse(base_url+major.xpath('a/@href')[0]) 	                             #open web page of another major
	major_name = major_page.xpath('//*[@id="title"]')[0].text_content()
	major_abbr = str(major.xpath('a/@href')[0]).replace('.html','').upper()
	
	if major_abbr in ['CLST', 'EEB','MCDB']:
		continue								                         # CLST, EEB, MCDB which show up in base_url are not in all_subject

	subject = str(major_page.xpath('//*[@id="title"]')[0].text_content())

	for class_element in major_page.xpath('//*[@class="content contentBox"]/*'):
		class_of_the_subject = {}
		
		if len(class_element.xpath('strong'))>0:
			class_number = str(class_element.xpath('strong')[0].text_content().replace('.',''))
		else:
			continue

		# there are some problematic course number data. Repair them
		if len(major_abbr+ class_number)>8:
			for ch in ['Keywords and Concepts: Geography and Ecology',' Literary Interpretation', ' Theory and Interpretation', ' Creative Writing',' Biblical Hebrew, Egyptian Hieroglyph, Sanskrit',' French Literature',' German Literature',' Greek Literature',' Italian Literature',' Latin Literature',' Spanish/Latin American/Latino Literature',' Proseminar']:
				if ch in class_number:
					class_number = class_number.replace(ch,'')
        
        #search class one by one using mechanize
		try:
			br.select_form('searchForm')
			br.form['binds[:term]'] = ['2172',]
			br.form['binds[:reg_status]'] = ['all',]
			br.form['binds[:subject]'] = [major_abbr,]
			br.form['binds[:catalog_nbr]'] = class_number
			response = br.submit()
			page = html.document_fromstring(response.read())

			class_list_2 = page.xpath('//div[@class="panel panel-default row"]')
			if class_list_2 == []:
				continue
			class_of_the_subject['Subject'] = subject
			class_of_the_subject['Class_Number'] = major_abbr+class_number
			class_of_the_subject['Class_name'] = str(page.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/h2/a[2]')[0].text_content())
			class_of_the_subject['Instructor'] = str(page.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/text()')[0])
			class_of_the_subject['Capacity'] = str(page.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/div[5]')[0].text_content())
			class_of_the_subject['Day_And_Time'] = str(page.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/div[4]/text()')[0])
			class_of_the_subject['Class_Location'] = str(page.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/div[3]/text()')[0])
			all_data.append(class_of_the_subject)
			count = count+1
			print count

		except:
			print "This is an error message!",major_abbr+ class_number
	# break
print all_data
with open('data11111111.json', 'w') as f:
	 json.dump(all_data, f)







