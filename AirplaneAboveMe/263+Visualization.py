
# coding: utf-8

# In[44]:

import re
from bokeh.io import show, output_file
from bokeh.models import (
    ColumnDataSource,
    HoverTool,
    LogColorMapper
)
from bokeh.palettes import Magma6 as palette
from bokeh.plotting import figure,vplot

from bokeh.sampledata.us_counties import data as counties
import csv
from os.path import join

#from bokeh.sampledata.unemployment import data as unemployment
aircraft = {}
destination = {}

reader = csv.reader(open('/Users/amazhari/anaconda3/lib/python3.5/site-packages/bokeh/sampledata/aircraft_above.csv'), delimiter=',', quotechar='"')
for row in reader:
    dummy, state_id, county_id, dummy, dummy, dummy, dummy, destination1, rate = row
    if(state_id!=''):
        aircraft[(int(state_id), int(county_id))] = (rate)
        destination[(int(state_id), int(county_id))] = (destination1)

counties = {
    code: county for code, county in counties.items() if county["state"] == "ca"
}

# county_xs = [county["lons"] for county in counties.values()]
# county_ys = [county["lats"] for county in counties.values()]
# county_names = [county['name'] for county in counties.values()]
# #county_rates = [aircraft[county_id] for county_id in counties]

#destination = []
color_mapper = LogColorMapper(palette=palette)

reader = csv.reader(open('/Users/amazhari/Documents/PhD/CS263/Project/flights_final.csv'), delimiter=',', quotechar='"')

county_xs =[]
county_ys = []
county_names = []
county_rate = []
heading = []
identity = []
altitude =[]
groundspeed = []
origin = []
destination = []

#County List
county_list = []
#For graph represent in order
county_count_graph = []
common_aircraft = []
#Count for how many airplane are in each county
county_count = {}
#Count for how many different type of airplane are in each county
county_count_aircraft_type = {}

for row in reader:
    #print(row,len(row))
    dummy, ident, dummy, aircraft_type, dummy, org,dest, dummy, dummy, dummy, dummy, dummy, lon, lat, dummy, dummy,dummy, dummy, gs, alt,head, dummy, dummy, dummy, dummy, dummy, dummy, = row

    if(lon!="longitude"):
         county_ys.append([float(lat),float(lat),float(lat)+0.05,float(lat)+0.05])
         county_xs.append([float(lon),float(lon)+0.05,float(lon)+0.05,float(lon)])
         county_names.append(aircraft_type)
         county_rate.append(aircraft_type)
         heading.append(head)
         identity.append(ident)
         origin.append(org)
         destination.append(dest)
         groundspeed.append(gs)
         altitude.append(alt+"00")
         common_aircraft.append('-')
         county_count_graph.append('-')
         
    #if(state_id!=''):
    #    aircraft[(int(state_id), int(county_id))] = (rate)
    #    destination[(int(state_id), int(county_id))] = (destination1)


#print(county_xs)

for county in counties.values():
    county_xs.append(county["lons"])
    county_ys.append(county["lats"])
    county_names.append(county['name'])
    county_rate.append('-')
    identity.append('-')
    heading.append('-')
    altitude.append('-')
    groundspeed.append('-')
    origin.append('-')
    destination.append('-')

##Aircraft counting
#Make county list, init county_count and county_count_aircraft_type
for county in counties.values():
    county_list.append(county['name'])
    county_count[county['name']] = 0
    county_count_aircraft_type[county['name']] = {}
    
#Reopen Flight record file
reader = csv.reader(open('/Users/amazhari/Documents/PhD/CS263/Project/flights_final.csv'), delimiter=',', quotechar='"')
for row in reader:
    #print(row,len(row))
    dummy, ident, dummy, aircraft_type, dummy, org,dest, dummy, dummy, dummy, dummy, dummy, lon, lat, dummy, dummy,dummy, dummy, gs, alt,head, dummy, dummy, dummy, dummy, dummy, county, = row

    #Exclude header row
    if(lon!="longitude"):
        for county_t in county_list:
            #Match county in flight record and county list
            if(county.lower().find(county_t.lower())!=-1):
                #Matched, count up
                county_count[county_t] = county_count[county_t] + 1
                
                #Aircraft type, exclude undefine
                if(aircraft_type!=''):
                    try:
                        county_count_aircraft_type[county_t][aircraft_type] = county_count_aircraft_type[county_t][aircraft_type]+1
                    except:
                        county_count_aircraft_type[county_t][aircraft_type] = 1
                        
#Rearrange new list in order to match map list
for county in county_list:
    #Rearrange airplane count in different county
    try:
        county_count_graph.append(county_count[county])
    except:   
        county_count_graph.append(0)
    
    #Rearrange most common airplane
    #Find most common from list 
    max_value = 0
    max_aircraft_type = ''
    for aircraft_type in county_count_aircraft_type[county]:
        if county_count_aircraft_type[county][aircraft_type] >= max_value:
            #Update when found new max
            max_value = county_count_aircraft_type[county][aircraft_type]
            max_aircraft_type = aircraft_type
    #Add to graph list
    common_aircraft.append(max_aircraft_type)

    


airline_code =[]

for flight_code in identity:
    if re.search("[A-Z]{3}", flight_code):
        match = re.search("[A-Z]{3}", flight_code)
#        print(match.group(0))
        airline_code.append("https://flightaware.com/images/airline_logos/90p/"+ match.group(0)+".png")
    else:
        airline_code.append("https://photos.flightaware.com/photos/retriever/f3596703946e6a070ff1b6b97c34269fd03b0baf")

source = ColumnDataSource(data=dict(
    x=county_xs,
    y=county_ys,
    name=county_names,
    rate=county_count_graph,
    iden=identity,
    head=heading,
    alt=altitude,
    gs=groundspeed,
    org=origin,
    dest=destination,
    most_common_aircraft =common_aircraft,
    airline_code=airline_code
))

TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"
p = figure(
    title="What Is That Airplane Overhead?", tools=TOOLS,
    x_axis_location=None, y_axis_location=None
)
p.grid.grid_line_color = None

p.patches('x', 'y', source=source,
          fill_color={'field': 'rate', 'transform': color_mapper},
          fill_alpha=.2, line_color="black", line_width=1)

hover = p.select_one(HoverTool)
hover.point_policy = "snap_to_data"
hover.tooltips = """            
            <div>
                <img
                    src="@airline_code" height="42" alt="@imgs" width="42"
                    "
                    border="2"
                ></img>
                <p>Name:@name</p>
                <p>Flight:@iden</p>
                <p>Longitude:$x , Latitude:$y </p>
                <p>Origin:@org</p>
                <p>Destination:@dest</p>
                <p>Altitude (Feet):@alt</p>
                <p>Heading (Degrees):@head</p>
                <p>Ground Speed (Knots):@gs</p>
                <p>Most Common Aircraft Type:@most_common_aircraft</p>
            </div>"""
                  
#     ("Name", "@name"),
#     ("(Long, Lat)", "($x, $y)"),
#     ("Aircraft Flying Through Per Day", "@rate"),
#     ("Flight", "@iden"),
#     ("Origin", "@org"),
#     ("Destination", "@dest"),
#     ("Altitude (Feet)", "@alt"),
#     ("Heading (Degrees)","@head"),
#     ("Ground Speed (Knots)", "@gs"),
#     ("Most Common Aircraft Type","@most_common_aircraft")


# hover = HoverTool(
#         tooltips="""
#         <div>
#             <div>
#                 <img
#                     src="@imgs" height="42" alt="@imgs" width="42"
#                     style="float: left; margin: 0px 15px 15px 0px;"
#                     border="2"
#                 ></img>
#             </div>
#             <div>
#                 <span style="font-size: 17px; font-weight: bold;">@desc</span>
#                 <span style="font-size: 15px; color: #966;">[$index]</span>
#             </div>
#             <div>
#                 <span style="font-size: 15px;">Location</span>
#                 <span style="font-size: 10px; color: #696;">($x, $y)</span>
#             </div>
#         </div>
#         """
#     )





# source = ColumnDataSource(data=dict(
#     x=g_aircraft_x,
#     y=g_aircraft_y,
#     name=g_aircraft_type,
#     #name=county_names,
#     rate=g_aircraft_type
# ))


# p2 = figure(
#     title="Geospatial California", tools=TOOLS,
#     x_axis_location=None, y_axis_location=None
# )
# p2.grid.grid_line_color = None

# p2.patches('x', 'y', source=source,
#           fill_color={'field': 'rate', 'transform': color_mapper},
#           fill_alpha=0.7, line_color="black", line_width=2)

# hover2 = p2.select_one(HoverTool)
# hover2.point_policy = "snap_to_data"
# hover2.tooltips = [
#     ("Name", "@name"),
#     ("Aircraft likely above you", "@rate"),
#     ("(Long, Lat)", "($x, $y)"),
# ]

#output_notebook
output_file("Planeoverhead_3_19.html")
show(p)
#show(p2)


# In[ ]:




# In[ ]:



