
"""
This is a script for course project in CMPS263, UCSC 2017 Winter.
We visualize the data from Employment_process_China.csv and Employment_process_India.csv in the script.

Author:
Ran Xu
rxu3@ucsc.edu

"""

# -*- coding: utf-8 -*-
from bokeh.plotting import figure, output_file,show,save
from bokeh.models import Legend
import pandas as pd
import numpy as np
from datetime import date,datetime
from bokeh.models import HoverTool
from bokeh.plotting import ColumnDataSource


df_china = pd.read_csv('../output/viz/EB_WaitingTime/Employment_process_China.csv')
df_china.head()
# #Bokeh line chart
x=pd.date_range('1991-10-01',periods=300,freq='M')
y1=df_china['China_EB1']
y2=df_china['China_EB2']
y3=df_china['China_EB3']
df_india = pd.read_csv('../output/viz/EB_WaitingTime/Employment_process_India.csv')
df_india.head()
y4=df_india['India_EB1']
y5=df_india['India_EB2']
y6=df_india['India_EB3']

#It will produce an image of all the EB 1-3 in China

output_file('../output/viz/EB_WaitingTime/ALL_CHINA.html')

p=figure(plot_width=900,tools = 'pan,box_zoom,reset,save,xwheel_zoom,crosshair',x_axis_label='Month', y_axis_label='Waiting time (Months)',x_axis_type="datetime")
#p.line(x,y1,legend='EB1',line_color='orange')
p.circle(x,y1,legend='China EB1',fill_color='#1f78b4',line_color='#1f78b4')
#p.line(x,y2,legend='EB2',line_color='blue')
p.circle(x,y2,legend='China EB2',fill_color='#a6cee3',line_color='#a6cee3')
#p.line(x,y3,legend='EB3',line_color='green')
p.circle(x,y3,legend='China EB3',fill_color='#b2df8a',line_color='#b2df8a')
p.legend.location = "top_left"
#p.legend.orientation = "horizontal"
#p.legend.orientation = "top_left"
save(p)

#It will show the dot image of EB1 in China
output_file('../output/viz/EB_WaitingTime/EB1_CHINA.html')
p6=figure(plot_width=900,tools = 'pan,box_zoom,reset,save,xwheel_zoom,crosshair',x_axis_label='Month', y_axis_label='Waiting time (Months)',x_axis_type="datetime")
#p.line(x,y1,legend='EB1',line_color='orange')
p6.circle(x,y1,legend='China EB1',fill_color='#1f78b4',line_color='#1f78b4')
p6.legend.location = "top_left"
save(p6)

#It will show the dot image of EB2 in China
output_file('../output/viz/EB_WaitingTime/EB2_CHINA.html')
p7=figure(plot_width=900,tools = 'pan,box_zoom,reset,save,xwheel_zoom,crosshair',x_axis_label='Month', y_axis_label='Waiting time (Months)',x_axis_type="datetime")
#p.line(x,y2,legend='EB2',line_color='blue')
p7.circle(x,y2,legend='China EB2',fill_color='#a6cee3',line_color='#a6cee3')
p7.legend.location = "top_left"
save(p7)

#It will show the dot image of EB3 in China
output_file('../output/viz/EB_WaitingTime/EB3_CHINA.html')
p8=figure(plot_width=900,tools = 'pan,box_zoom,reset,save,xwheel_zoom,crosshair',x_axis_label='Month', y_axis_label='Waiting time (Months)',x_axis_type="datetime")
p8.circle(x,y3,legend='China EB3',fill_color='#b2df8a',line_color='#b2df8a')
p8.legend.location = "top_left"
save(p8)





#It will produce an image of all the EB 1-3 in India 

#p2 = Area(data,tools = 'pan,box_zoom,reset,save,xwheel_zoom',title = "India EB1-3 Waiting Time (Month)",legend="top_left", xlabel="Year/Month",ylabel="Waiting time (month)")
output_file('../output/viz/EB_WaitingTime/ALL_INDIA.html')
#p2 = Bar(df_india, values='EB1_month_diff',label='Year/Month',title='India EB1-3 Waiting Time (Month)', legend='top_right')
p2=figure(plot_width=900,tools = 'pan,box_zoom,reset,save,xwheel_zoom,crosshair',x_axis_label='Month', y_axis_label='Waiting time (Months)',x_axis_type="datetime")
#p2.line(x,y4,legend='EB1',line_color='orange')
p2.circle(x,y4,legend='India EB1',fill_color='#5e3c99',line_color='#5e3c99')
#p2.line(x,y5,legend='EB2',line_color='blue')
p2.circle(x,y5,legend='India EB2',fill_color='#b2abd2',line_color='#b2abd2')
#p2.line(x,y6,legend='EB3',line_color='green')
p2.circle(x,y6,legend='India EB3',fill_color='#fdb863',line_color='#fdb863')
p2.legend.location = "top_left"
#p2.legend.orientation = "horizontal"
save(p2)

# x1=range(1, 300)
# bar=Bar(df,values=blend('EB1_month_diff','EB2_month_diff','EB3_month_diff',name='EB',labels_name='EB1-3'),stack=cat(columns='EB1-3', sort=False),label=cat(columns='Current_year', sort=False),color=color(columns='EB1-3', palette=['SaddleBrown', 'Silver', 'Goldenrod'],
#                       sort=False),title = 'India EB1-3 Waiting Time (Month)')
# save(bar)
#It will show the dot image of EB1 in India
output_file('../output/viz/EB_WaitingTime/EB1_INDIA.html')
#p2 = Bar(df_india, values='EB1_month_diff',label='Year/Month',title='India EB1-3 Waiting Time (Month)', legend='top_right')
p9=figure(plot_width=900,tools = 'pan,box_zoom,reset,save,xwheel_zoom,crosshair',x_axis_label='Month', y_axis_label='Waiting time (Months)',x_axis_type="datetime")
p9.circle(x,y4,legend='India EB1',fill_color='#5e3c99',line_color='#5e3c99')
p9.legend.location = "top_left"
save(p9)

#It will show the dot image of EB2 in India

output_file('../output/viz/EB_WaitingTime/EB2_INDIA.html')
#p2 = Bar(df_india, values='EB1_month_diff',label='Year/Month',title='India EB1-3 Waiting Time (Month)', legend='top_right')
p10=figure(plot_width=900,tools = 'pan,box_zoom,reset,save,xwheel_zoom,crosshair',x_axis_label='Month', y_axis_label='Waiting time (Months)',x_axis_type="datetime")
p10.circle(x,y5,legend='India EB2',fill_color='#b2abd2',line_color='#b2abd2')
p10.legend.location = "top_left"
save(p10)

#It will show the dot image of EB3 in India
output_file('../output/viz/EB_WaitingTime/EB3_INDIA.html')
#p2 = Bar(df_india, values='EB1_month_diff',label='Year/Month',title='India EB1-3 Waiting Time (Month)', legend='top_right')
p11=figure(plot_width=900,tools = 'pan,box_zoom,reset,save,xwheel_zoom,crosshair',x_axis_label='Month', y_axis_label='Waiting time (Months)',x_axis_type="datetime")
p11.circle(x,y6,legend='India EB3',fill_color='#fdb863',line_color='#fdb863')
p11.legend.location = "top_left"
save(p11)

#EB1 in both country
output_file('../output/viz/EB_WaitingTime/EB1_BOTH.html')
p3=figure(plot_width=900,tools = 'pan,box_zoom,reset,save,xwheel_zoom,crosshair',x_axis_label='Month', y_axis_label='Waiting time (Months)',x_axis_type="datetime")
#p3.line(x,y1,legend='China EB1',line_color='green')
p3.circle(x,y1,legend='China EB1',fill_color='#1f78b4',line_color='#1f78b4')
#p3.line(x,y4,legend='India EB1',line_color='dark purple')
p3.circle(x,y4,legend='India EB1',fill_color='#5e3c99',line_color='#5e3c99')
p3.segment(x,y1,x,y4,line_dash="4 4", line_width=1, color='gray')
p3.legend.location = "top_left"
#p3.legend.orientation = "horizontal"
save(p3)

#EB2 in both country

output_file('../output/viz/EB_WaitingTime/EB2_BOTH.html')
p4=figure(plot_width=900,tools = 'pan,box_zoom,reset,save,xwheel_zoom,crosshair',x_axis_label='Month', y_axis_label='Waiting time (Months)',x_axis_type="datetime")
#p4.line(x,y2,legend='China EB2',line_color='light blue')
p4.circle(x,y2,legend='China EB2',fill_color='#a6cee3',line_color='#a6cee3')
#p4.line(x,y5,legend='India EB2',line_color='blue')
p4.circle(x,y5,legend='India EB2',fill_color='#b2abd2',line_color='#b2abd2')
p4.segment(x,y2,x,y5,line_dash="4 4", line_width=1, color='gray')
p4.legend.location = "top_left"
save(p4)

#EB3 in both country
output_file('../output/viz/EB_WaitingTime/EB3_BOTH.html')
p5=figure(plot_width=900,tools = 'pan,box_zoom,reset,save,xwheel_zoom,crosshair',x_axis_label='Month', y_axis_label='Waiting time (Months)',x_axis_type="datetime")
#p5.line(x,y3,legend='China EB3',line_color='green')
p5.circle(x,y3,legend='China EB3',fill_color='#b2df8a',line_color='#b2df8a')
#p5.line(x,y6,legend='India EB3',line_color='blue')
p5.circle(x,y6,legend='India EB3',fill_color='#fdb863',line_color='#fdb863')
p5.segment(x,y3,x,y6,line_dash="4 4", line_width=1, color='gray')
p5.legend.location = "top_left"
save(p5)


#EB1-3 in both country, 
output_file('../output/viz/EB_WaitingTime/ALL_BOTH.html')
p12=figure(plot_width=900,tools = 'pan,box_zoom,reset,save,xwheel_zoom,crosshair',x_axis_label='Month', y_axis_label='Waiting time (Months)',x_axis_type="datetime")
#p.line(x,y1,legend='EB1',line_color='orange')
p12.circle(x,y1,legend='China EB1',fill_color='#1f78b4',line_color='#1f78b4')
#p.line(x,y2,legend='EB2',line_color='blue')
p12.circle(x,y2,legend='China EB2',fill_color='#a6cee3',line_color='#a6cee3')
#p.line(x,y3,legend='EB3',line_color='green')
p12.circle(x,y3,legend='China EB3',fill_color='#b2df8a',line_color='#b2df8a')
#p2 = Bar(df_india, values='EB1_month_diff',label='Year/Month',title='India EB1-3 Waiting Time (Month)', legend='top_right')
#p12=figure(plot_width=900,tools = 'pan,box_zoom,reset,save,xwheel_zoom',x_axis_label='Month', y_axis_label='Waiting time (Months)',x_axis_type="datetime")
#p2.line(x,y4,legend='EB1',line_color='orange')
p12.circle(x,y4,legend='India EB1',fill_color='#5e3c99',line_color='#5e3c99')
#p2.line(x,y5,legend='EB2',line_color='blue')
p12.circle(x,y5,legend='India EB2',fill_color='#b2abd2',line_color='#b2abd2')
#p2.line(x,y6,legend='EB3',line_color='green')
p12.circle(x,y6,legend='India EB3',fill_color='#fdb863',line_color='#fdb863')
p12.legend.location = "top_left"
save(p12)
