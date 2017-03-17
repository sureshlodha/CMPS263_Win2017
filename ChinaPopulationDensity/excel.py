#coding=utf-8
import xlrd
import json
import math
book = xlrd.open_workbook('population density.xlsx')
sheet = book.sheet_by_name('1-8')
provinceEnglish_lower = ['shanghai', 'hebei', 'shanxi', 'inner mongolia', 'liaoning', 'jilin', 'heilongjiang', 'jiangsu', 'zhejiang', 'anhui', 'fujian', 'jiangxi', 'shandong', 'henan', 'hubei', 'hunan', 'guangdong', 'guangxi', 'hainan', 'sichuan', 'guizhou', 'yunnan', 'tibet', 'shaanxi', 'gansu', 'qinghai', 'ningxia', 'xinjiang', 'beijing', 'tianjin', 'chongqing']
result = {}
city = []
value = []
provinceEnglish = []
city_low = []
for i in provinceEnglish_lower:
    j = str.capitalize(i)
    provinceEnglish.append(j)

i = 6;
while i<365:
    row = sheet.row_values(i)
    region= str.lstrip(str.lower((row[1]).encode()))
    destiny = row[5].encode()
    if len(region) == 0:
        i = i+6
    else:
        i = i+1
        city_low.append(region)
        value.append(int(float(destiny)))

for i in city_low:
    j = str.capitalize(i)
    city.append(j)


splitIndex={}
for j in  provinceEnglish:
    index = city.index(j)
    splitIndex[index] = city[index]
    # splitIndex[len(city)] = 'none'
split = sorted(splitIndex)

for i in provinceEnglish:
    result[i] = {}

for i in range(len(split)):
    if i<len(split)-1:
        for m in range(split[i]+1,split[i+1]):
            temp = city[split[i]]
            temp1 = city[m]
            result[temp][temp1] = value[m]
    else:
        for m in range(split[i]+1,len(city)):
            temp = city[split[i]]
            temp1 = city[m]
            result[temp][temp1] = value[m]
for i in split:
    temp = city[i]
    result[temp]['all'] = value[i]

json.dump(result,open('Eng-Density.json','w'))
