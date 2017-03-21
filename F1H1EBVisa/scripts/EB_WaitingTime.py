
"""
This is a script for course project in CMPS263, UCSC 2017 Winter.
We wraggle data and analyize EmploymentChina.csv and EmploymentIndia.csv in the script.

Author:
Yusheng Fang

"""
import glob,csv,re
import time
from datetime import date

# Oct = re.compile('Oct.*')
# Nov = re.compile('Nov.*')
# Dec = re.compile('Dec.*')
# Jan = re.compile('Jan.*')
# Feb = re.compile('Feb.*')
# Mar = re.compile('Mar.*')
# Apr = re.compile('Apr.*')
# May = re.compile('May.*')
# June = re.compile('June.*')
# July = re.compile('July.*')
# Aug = re.compile('Aug.*')
# Sept = re.compile('Sept.*')

#The array for replace from month to number
array_month = [10,11,12,1,2,3,4,5,6,7,8,9]
dict_month = {'Oct':10,'Nov':11,'Dec':12,'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9}

#process the file EmploymentChina.csv
csvread=open('../datasource/EmploymentChina.csv','rb')
Employment = csv.reader(csvread)
with open('../output/viz/EB_WaitingTime/Employment_process_China.csv','wb') as f:
  writer=csv.writer(f)
  writer.writerow(['Current_Year','Current_Month','1st_year','1st_month','China_EB1','2nd_year','2nd_month','China_EB2','3rd_year','3rd_month','China_EB3'])
  #index for the month array
  i=0
  for row in Employment:
    write_string =[]
    if row[0]=='':
      continue
    elif row[0][0]=='F'and row[0][1]=='Y':
      year=int(re.search(r'\d+',row[0]).group())


    else:

      if i<3:
        FY=year-1
      else:
        FY=year
      write_string.append(FY)
      write_string.append(array_month[i])
      current_year = FY
      current_month = array_month[i]
      # if row[1]=='':
      #   write_string.append('')
      #   write_string.append('')
      #process the EB1
      if re.match('C.*',row[1])or re.match('U.*',row[1]):
        write_string.append(row[1])
        write_string.append(row[1])
        write_string.append(0)
      else:
        action_year=int(re.search(r'(-)(\d+)',row[1]).group(2))
        if action_year>80:
          action_year=action_year+1900
        else:
          action_year=action_year+2000
        write_string.append(action_year)
        month=re.search(r'(-)(\w+)-',row[1]).group(2)
        write_string.append(dict_month[month])
        action_month=dict_month[month]
        EB1_month_diff=current_year*12+current_month-action_year*12-action_month
        write_string.append(EB1_month_diff)



      #PROCESS EB2
      if re.match('C.*',row[2])or re.match('U.*',row[2]) :
        write_string.append(row[2])
        write_string.append(row[2])
        write_string.append(0)
      else:
        action_year=int(re.search(r'(-)(\d+)',row[2]).group(2))
        if action_year>80:
          action_year=action_year+1900
        else:
          action_year=action_year+2000
        write_string.append(action_year)
        month=re.search(r'(-)(\w+)-',row[2]).group(2)
        write_string.append(dict_month[month])
        action_month=dict_month[month]
        EB2_month_diff=current_year*12+current_month-action_year*12-action_month
        write_string.append(EB2_month_diff)

      #process EB3
      if re.match('C.*',row[3])or re.match('U.*',row[3]) :
        write_string.append(row[3])
        write_string.append(row[3])
        write_string.append(0)
      else:
        action_year=int(re.search(r'(-)(\d+)',row[3]).group(2))
        if action_year>80:
          action_year=action_year+1900
        else:
          action_year=action_year+2000
        write_string.append(action_year)
        month=re.search(r'(-)(\w+)-',row[3]).group(2)
        write_string.append(dict_month[month])
        action_month=dict_month[month]
        EB3_month_diff=current_year*12+current_month-action_year*12-action_month
        write_string.append(EB3_month_diff)


      if i<11:
        i=i+1
      else:
        i=0
      print(write_string)
      writer.writerow(write_string)
    #index for the month array

#process the file EmploymentIndia.csv
csvread=open('../datasource/EmploymentIndia.csv','rb')
Employment = csv.reader(csvread)
with open('../output/viz/EB_WaitingTime/Employment_process_India.csv','wb') as f:
  writer=csv.writer(f)
  writer.writerow(['Current_Year','Current_Month','1st_year','1st_month','India_EB1','2nd_year','2nd_month','India_EB2','3rd_year','3rd_month','India_EB3'])
  #index for the month array
  i=0
  for row in Employment:
    write_string =[]
    if row[0]=='':
      continue
    elif row[0][0]=='F'and row[0][1]=='Y':
      year=int(re.search(r'\d+',row[0]).group())


    else:

      if i<3:
        FY=year-1
      else:
        FY=year
      write_string.append(FY)
      write_string.append(array_month[i])
      current_year = FY
      current_month = array_month[i]
      # if row[1]=='':
      #   write_string.append('')
      #   write_string.append('')
      #process the EB1
      if re.match('C.*',row[1])or re.match('U.*',row[1]):
        write_string.append(row[1])
        write_string.append(row[1])
        write_string.append(0)
      else:
        action_year=int(re.search(r'(-)(\d+)',row[1]).group(2))
        if action_year>80:
          action_year=action_year+1900
        else:
          action_year=action_year+2000
        write_string.append(action_year)
        month=re.search(r'(-)(\w+)-',row[1]).group(2)
        write_string.append(dict_month[month])
        action_month=dict_month[month]
        EB1_month_diff=current_year*12+current_month-action_year*12-action_month
        write_string.append(EB1_month_diff)



      #PROCESS EB2
      if re.match('C.*',row[2])or re.match('U.*',row[2]) :
        write_string.append(row[2])
        write_string.append(row[2])
        write_string.append(0)
      else:
        action_year=int(re.search(r'(-)(\d+)',row[2]).group(2))
        if action_year>80:
          action_year=action_year+1900
        else:
          action_year=action_year+2000
        write_string.append(action_year)
        month=re.search(r'(-)(\w+)-',row[2]).group(2)
        write_string.append(dict_month[month])
        action_month=dict_month[month]
        EB2_month_diff=current_year*12+current_month-action_year*12-action_month
        write_string.append(EB2_month_diff)

      #process EB3
      if re.match('C.*',row[3])or re.match('U.*',row[3]) :
        write_string.append(row[3])
        write_string.append(row[3])
        write_string.append(0)
      else:
        action_year=int(re.search(r'(-)(\d+)',row[3]).group(2))
        if action_year>80:
          action_year=action_year+1900
        else:
          action_year=action_year+2000
        write_string.append(action_year)
        month=re.search(r'(-)(\w+)-',row[3]).group(2)
        write_string.append(dict_month[month])
        action_month=dict_month[month]
        EB3_month_diff=current_year*12+current_month-action_year*12-action_month
        write_string.append(EB3_month_diff)


      if i<11:
        i=i+1
      else:
        i=0
      print(write_string)
      writer.writerow(write_string)
    #index for the month array
