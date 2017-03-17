#inspect courses of a specific major (by setting the variable major_abbr)

from lxml import html
import requests
import mechanize
import json
all_data = []
count = 0
br = mechanize.Browser()
br.open("https://pisa.ucsc.edu/cs9/prd/sr9_2013/index.php")

major_abbr = 'PSYC'
major_page= html.parse('http://registrar.ucsc.edu/catalog/programs-courses/course-descriptions/psyc.html')
subject = str(major_page.xpath('//*[@id="title"]')[0].text_content())

for class_element in major_page.xpath('//*[@class="content contentBox"]/*'):
	class_of_the_subject = {}
	
	if len(class_element.xpath('strong'))>0:
		class_number = str(class_element.xpath('strong')[0].text_content().replace('.',''))
	else:
		continue
    
    #search class one by one using mechanize

	br.select_form('searchForm')
	br.form['binds[:term]'] = ['2172',]
	br.form['binds[:reg_status]'] = ['all',]
	br.form['binds[:subject]'] = [major_abbr,]
	br.form['binds[:catalog_nbr]'] = class_number
	response = br.submit()
	page = html.document_fromstring(response.read())
	print 'search:', major_abbr, class_number,'*************************************'
	class_list_2 = page.xpath('//div[@class="panel panel-default row"]')
	if page.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/h2/a[2]'):
		class_of_the_subject['Subject'] = subject
		class_of_the_subject['Class_Number'] = major_abbr+class_number
		class_of_the_subject['Class_name'] = str(page.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/h2/a[2]')[0].text_content())
		class_of_the_subject['Instructor'] = str(page.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/text()')[0])
		class_of_the_subject['Capacity'] = str(page.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/div[5]')[0].text_content())
		class_of_the_subject['Day_And_Time'] = str(page.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/div[4]/text()')[0])
		class_of_the_subject['Class_Location'] = str(page.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/div[3]/text()')[0])
		class_of_the_subject['index']= str(page.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/h2/a[2]/@href')[0])
		all_data.append(class_of_the_subject)
		count = count +1
		print 'https://pisa.ucsc.edu/cs9/prd/sr9_2013/',class_of_the_subject['index']
print count








