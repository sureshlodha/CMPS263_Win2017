# Pathway from F1 Student to U.S. Citizen

To reproduce our result, make sure you have installed Python2 and library “psycopg2”, “numpy”, “plotly”, “pandas”, “pygal”, “bokeh”. And make user you have configure a PostgreSQL server on your machine.

The COMPLETE steps are followings:

Clone my github repo to your local machine:
git clone https://github.com/ericucsc/H1B_EB_Applicants_Visulization.git

Download additional data files from their source website:
1. Download [“PERM_FY2016.xlsx”](https://www.foreignlaborcert.doleta.gov/docs/Performance_Data/Disclosure/FY15-FY16/PERM_Disclosure_Data_FY16.xlsx), and then convert it to .csv file using MS Excel, and put it under “./datasource/” as “PERM_Disclosure_Data_FY16.csv”

2. Download [“H1B_FY2016.xlsx”](https://www.foreignlaborcert.doleta.gov/docs/Performance_Data/Disclosure/FY15-FY16/H-1B_Disclosure_Data_FY16.xlsx) and then convert it to .csv file using MS Excel, and put it to “./datasource/” as “H-1B_FY16.csv”


Optional data files (we have prepared them in “./datasource/“):
1. [China Final Action Dates](https://travel.state.gov/content/dam/visas/family-preference-cut-off-dates/Cut-off_Dates_China_online.pdf). Download the pdf and then convert it to .docx using Adobe Acrobat, then convert it to .csv using MS Word. The result has been saved to “./datasource/EmploymentChina.csv”

2. [India Final Action Dates](https://travel.state.gov/content/dam/visas/family-preference-cut-off-dates/Cut-off_Dates_India_online.pdf)
Download the pdf file and then convert it to .docx using Adobe Acrobat, then convert it to .csv using MS Word. The result has been saved to “./datasource/EmploymentIndia.csv”

Our visualization includes 3 web pages of visualization, which are “H1B Companies”, “EB Companies”, “EB Waiting Time“. The following scrips produce intermediate files for our visualization. To execute the scripts, make sure you are under directory “./scripts/“

To get query results to .csv files for EB Companies:```	python EB_Company.py query
```
To get the visualization-ready .csv files for EB Companies:
```
	python EB_Company.py viz
```
To get the visualization-ready .csv files for H1B Companies (may need to modify the configuration(username, password,etc.) on line 5 to connect PostgreSQL server):
```
	python H1B_Company.py
```
To get the visualization-ready .csv files for EB Waiting Time:
```
	python EB_WaitingTime.py
```

To get plot visualization-ready .html file for EB Companies:
```
	python Company_plot.py perm
```
To get the visualization-ready .html file for H1B Companies:
```
	python Company_plot.py h1b
```
To get plot visualization-ready .html files for EB Waiting Time:
```
	python EB_WT_plot.py
```

To view the Final Visualization, open the file “./index.html” in your browser. We recommend Safari, Firefox, Chrome(least choice).
