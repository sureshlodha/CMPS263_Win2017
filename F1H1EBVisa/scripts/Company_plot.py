"""
This is a script for course project in CMPS263, UCSC 2017 Winter.
We generate graphs using pygal, potly libraries.

Author:
Yanzhong Li     yli185@ucsc.edu

"""

import csv
import sys
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import *
import pandas as pd
import pygal
import plotly.graph_objs as go
from pygal.style import Style
from pygal.style import DarkenStyle



US_STATES = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
US_STATE_SHORT_dic = {'WA': 'Washington', 'DE': 'Delaware', 'WI': 'Wisconsin', 'WV': 'West Virginia', 'HI': 'Hawaii', 'FL': 'Florida', 'WY': 'Wyoming', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'TX': 'Texas', 'LA': 'Louisiana', 'NC': 'North Carolina', 'ND': 'North Dakota', 'NE': 'Nebraska', 'TN': 'Tennessee', 'NY': 'New York', 'PA': 'Pennsylvania', 'CA': 'California', 'NV': 'Nevada', 'VA': 'Virginia', 'CO': 'Colorado', 'AK': 'Alaska', 'AL': 'Alabama', 'AR': 'Arkansas', 'VT': 'Vermont', 'IL': 'Illinois', 'GA': 'Georgia', 'IN': 'Indiana', 'IA': 'Iowa', 'OK': 'Oklahoma', 'AZ': 'Arizona', 'ID': 'Idaho', 'CT': 'Connecticut', 'ME': 'Maine', 'MD': 'Maryland', 'MA': 'Massachusetts', 'OH': 'Ohio', 'UT': 'Utah', 'MO': 'Missouri', 'MN': 'Minnesota', 'MI': 'Michigan', 'RI': 'Rhode Island', 'KS': 'Kansas', 'MT': 'Montana', 'MS': 'Mississippi', 'SC': 'South Carolina', 'KY': 'Kentucky', 'OR': 'Oregon', 'SD': 'South Dakota'}


def plotPermChoropleth (ebOrH1b, dataFilePath, outputPath):
    if (ebOrH1b == 'perm'):
        plotTitle = '<br>2016 EB-2/EB-3 Applicants by State'
        FullStateName = 'FullStateName'
        Abbr = 'State'
        applicants_count = 'applicants_count'
    elif (ebOrH1b == 'h1b'):
        plotTitle = '<br>2016 H1B Applicants by State'
        FullStateName = 'states'
        Abbr = 'abb'
        applicants_count = 'count_workers'


    df = pd.read_csv(dataFilePath)
    for col in df.columns:
        df[col] = df[col].astype(str)
    scl = [[0.0, 'rgb(242,240,247)'],[0.02, 'rgb(218,218,235)'],[0.03, 'rgb(188,189,220)'],\
                [0.05, 'rgb(158,154,200)'],[0.08, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]
    df['text'] = df[FullStateName] + '<br>' +\
                'Total Applicants: ' + df[applicants_count]
    data = [ dict(
            type='choropleth',
            hoverinfo = "text",
            colorscale = scl,
            autocolorscale = True,
            locations = df[Abbr],
            z = df[applicants_count].astype(float),
            locationmode = 'USA-states',
            text = df['text'],
            marker = dict(
                line = dict (
                    color = 'rgb(255,255,255)',
                    width = 2
                ) ),
            showscale = True,
            colorbar = dict(
                    thicknessmode = "pixels",
                    thickness = 10,
                    lenmode = "pixels",
                    len = 300
                )
            ) ]
    layout = dict(
            # title = "plotTitle",
            geo = dict(
                scope='usa',
                projection=dict( type='albers usa' ),
                showlakes = True,
                lakecolor = 'rgb(255, 255, 255)'),
            margin = go.Margin(
                        l=0,
                        r=0,
                        b=0,
                        t=0,
                        pad=0
                    )
                 )
    fig = dict( data=data, layout=layout )
    # py.iplot( fig, filename='d3-cloropleth-map' )
    plot(fig, filename = outputPath)
    # plotly.offline.plot(data, filename = 'basic-line.html')


def plotPermBarCharts (dataFilePath, outputPath) :
    for short_name in US_STATES:
        with open(dataFilePath + short_name + '.csv', 'rb') as csvfile:
            stateData = list(csv.reader(csvfile))
        darken_style = DarkenStyle('#ff8723', step = 20)
        custom_style = Style(
              tooltip_font_size = 18,
              legend_font_size = 13,
              value_font_size = 15,
              title_font_size = 18
              )
        bar_chart = pygal.HorizontalBar(
                legend_box_size = 10,
                hieght = 100,
                style = darken_style,
                print_values = True,
                margin = 20,
                # show_legend=False,
                legend_at_bottom=True,
                tooltip_fancy_mode=True,
                tooltip_border_radius=10
                )
        # bar_chart.title = 'Top 30 foreign-worker-friendly Companies in</br>' + US_STATE_SHORT_dic[short_name]
        topX = 20
        if (short_name == 'MO'):
            topX = 17
        for row in stateData[1:topX+1]:
            bar_chart.add(str(row[0]), float(row[1]), rounded_bars = 3)
        # bar_chart.render_in_browser()
        bar_chart.render_to_file(outputPath + short_name + '.svg')

def plotPermPeers(outputPath) :
    # Do you know your peers(people majoring in Computer-related subjects)?
    # What are their highest degree? (pie chart)
    # How long have they been graduated? (vertical bar chart)
    # How experienced are they in CS/CE field? (bar chart)
    # Where do they come from?
    with open('../output/queries/q1_1.csv', 'rb') as csvfile:
        degreeData = list(csv.reader(csvfile))
    # Bachelor's	Master's	Doctorate
    custom_style = Style(label_font_size=18, legend_font_size=25, title_font_size=28)
    pie_chart = pygal.Pie(inner_radius=.4, style=custom_style, legend_at_bottom=True)
    pie_chart.title = 'What are their highest degree?'
    pie_chart.add("Bachelor's", int(degreeData[1][0]))
    pie_chart.add("Master's", int(degreeData[1][1]))
    pie_chart.add("Doctorate", int(degreeData[1][2]))
    # pie_chart.render_in_browser()
    pie_chart.render_to_file(outputPath + 'highest_degrees.svg')

    with open('../output/queries/q1_2.csv', 'rb') as csvfile:
        gradYear_Count = list(csv.reader(csvfile))
    # Graduation_year   count
    custom_style = Style(label_font_size=18, legend_font_size=18, title_font_size=28)
    line_chart = pygal.Bar(width=1400, style=custom_style, legend_at_bottom=True)
    line_chart.title = 'How long have they been graduated?'
    line_chart.x_labels = [int(row[0]) for row in gradYear_Count[1:]]
    line_chart.add('Amount of Applicants', [int(row[1]) for row in gradYear_Count[1:]])
    # line_chart.render_in_browser()
    line_chart.render_to_file(outputPath + 'gradYear_Count.svg')

    with open('../output/viz/PERM_Peers/mon_Exp_Range_Count.csv', 'rb') as csvfile:
        monExp_Count = list(csv.reader(csvfile))
    # Months_of_Experience_Range  count
    custom_style = Style(label_font_size = 20, title_font_size=28)
    line_chart = pygal.Bar(style=custom_style, legend_at_bottom=True)
    line_chart.title = 'How many months of experience do they have?'
    line_chart.x_labels = [row[0] for row in monExp_Count[1:]]
    line_chart.add('Amount of Applicants', [float(row[1]) for row in monExp_Count[1:]])
    # line_chart.render_in_browser()
    line_chart.render_to_file(outputPath + 'monExp_Count.svg')

    #using plotly to plot geomap
    plotlyGeoMap('ctryAbbr_count_Plotly', 'whereTheyFrom')
    plotlyGeoMap('ctryAbbr_count_Plotly_NoIndia', 'whereTheyFrom_NoIndia')
    plotlyGeoMap('ctryAbbr_count_Plotly_NoIndiaChina', 'whereTheyFrom_NoIndiaChina')
    plotlyGeoMap('ctryAbbr_count_Plotly_NoIndiaChinaCanada', 'whereTheyFrom_NoIndiaChinaCanada')

    #using pygal to plot geomap
    # with open('../output/viz/PERM_Peers/ctryAbbr_count.csv', 'rb') as csvfile:
    #     abbr_count_list = list(csv.reader(csvfile))
    # abbr_count_dict = {}
    # for row in abbr_count_list[1:]:
    #     abbr_count_dict[row[0]] = int(row[1])
    #
    #
    # worldmap_chart = pygal.maps.world.World()
    # worldmap_chart.title = 'Where are they from?'
    # worldmap_chart.add('2016 Fiscal Year', abbr_count_dict)
    # worldmap_chart.render_in_browser()

def plotlyGeoMap(inputFile, outputFile):
    df = pd.read_csv('../output/viz/PERM_Peers/'+inputFile+'.csv')
    # abbrCountryName   count
    data = [ dict(
            type = 'choropleth',
            locations = df['abbr'],
            z = df['count'],
            text = df['countryName'],
            colorscale = [[0,"rgb(5, 10, 172)"],[0.15,"rgb(40, 60, 190)"],[0.3,"rgb(70, 100, 245)"],\
                [0.4,"rgb(90, 120, 245)"],[0.5,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
            autocolorscale = True,
            reversescale = False,
            marker = dict(
                line = dict (
                    color = 'rgb(180,180,180)',
                    width = 0.5
                ) ),
            colorbar = dict(
                autotick = False,
                tickprefix = '$',
                title = 'GDP<br>Billions US$'),
          ) ]
    layout = dict(
        title = 'Where are they from?',
        geo = dict(
            showframe = False,
            showcoastlines = False,
            projection = dict(
                type = 'Mercator'
            )
        )
    )
    fig = dict( data=data, layout=layout )
    plot(fig, validate=False, filename='../output/viz/PERM_Peers/'+outputFile+'.html' )

if __name__ == "__main__":

    if (len(sys.argv) > 1):
        if (sys.argv[1] == "perm"):
            plotPermChoropleth('perm', '../output/viz/PERM_Companies/_PERM_StateByCase.csv', '../output/viz/PERM_Companies/_PERM_Choropleth.html')
            plotPermBarCharts('../output/viz/PERM_Companies/', '../output/viz/PERM_Companies/svg/')
        elif (sys.argv[1] == "h1b"):
            plotPermChoropleth('h1b', '../output/viz/H1B_Companies/state_count_workers.csv', '../output/viz/H1B_Companies/_H1B_Choropleth.html')
            plotPermBarCharts('../output/viz/H1B_Companies/', '../output/viz/H1B_Companies/svg/')
        elif (sys.argv[1] == "peers"):
            plotPermPeers('../output/viz/PERM_Peers/')












pass
