from bokeh.models.widgets import MultiSelect, Div
from bokeh.application.handlers import FunctionHandler
from bokeh.application import Application
from bokeh.layouts import column, row, widgetbox
from bokeh.plotting import figure, show, output_file, output_notebook
from bokeh.tile_providers import CARTODBPOSITRON
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.layouts import gridplot, widgetbox
from bokeh.models.widgets import DataTable, TableColumn
import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
from math import pi
from bokeh.io import curdoc

pd.set_option('display.max_columns', 500)

DATA_FOLDER = '../data/'

edges_csv = 'panama_papers.edges.csv'
intermediary_csv = 'panama_papers.nodes.intermediary.csv' # company or individuals
address_csv = 'panama_papers.nodes.address.csv'
officer_csv = 'panama_papers.nodes.officer.csv'
entity_csv = 'panama_papers.nodes.entity.csv' # tax heaven companies

# Importing the Panama Papers data into DataFrames
df_edges_raw = pd.read_csv(DATA_FOLDER + edges_csv,low_memory=False)
df_address_raw = pd.read_csv(DATA_FOLDER + address_csv,low_memory=False)
df_entity_raw = pd.read_csv(DATA_FOLDER + entity_csv,low_memory=False)
df_intermediary_raw = pd.read_csv(DATA_FOLDER + intermediary_csv,low_memory=False)
df_officier_raw = pd.read_csv(DATA_FOLDER + officer_csv,low_memory=False)

# part 2: calculating effect on home country wrt tax

GDP_tot = 'API_NY.GDP.MKTP.CD_DS2_en_csv_v2_10224782.csv'
corp_tax_rate = 'corp_tax_rate.csv'
business_country = 'business_country.csv'

GDP_tot_raw_df=pd.read_csv(DATA_FOLDER + GDP_tot,skiprows=4,low_memory=False)[['Country Name', '2015']]
corp_tax_rate_df = pd.read_csv(DATA_FOLDER + corp_tax_rate)[['Location', '2015']]
business_country_df = pd.read_csv(DATA_FOLDER + business_country)

# merging corp tax table with GDP table
m1 = corp_tax_rate_df.merge(GDP_tot_raw_df, left_on='Location',
                            right_on='Country Name', how='inner')

# merging m1 with number of businesses table
m2 = m1.merge(business_country_df, left_on='Location',
             right_on='Country Name', how='inner')
m2 = m2[['Location', '2015_x', '2015_y', 'Number of Businesses']]
m2.columns = ['Location', '2015 Corp Tax Rate % of GDP', '2015 GDP', 'Number of Businesses']

# calculating corporate tax revenue
m2['Corporate Tax Revenue'] = m2['2015 Corp Tax Rate % of GDP'] * m2['2015 GDP'] / 100

# calculating avg corp tax paid per business
m2['Avg tax per business'] = m2['Corporate Tax Revenue'] / m2['Number of Businesses']

# merge m2 with countries grouped by count of entries in Panama Papers
country_entries = pd.DataFrame(df_entity_raw.countries.value_counts()).reset_index()
country_entries.columns = ['Location', 'Count in PP']
country_entries.loc[country_entries['Location'] == 'South Korea', 'Location'] = 'Korea, Rep.'
m3 = m2.merge(country_entries, on='Location', how='inner')

# calculate potential tax evasion
m3['Potential Tax Lost'] = m3['Avg tax per business'] * m3['Count in PP']
m3['Potential Real Corporate Tax Revenue'] = m3['Potential Tax Lost'] + m3['Corporate Tax Revenue']
m3['% Tax Lost'] = m3['Potential Tax Lost'] / m3['Corporate Tax Revenue'] * 100

def make_dataset(countries):
    # select the relevant canton
    df = m3.loc[m3['Location'].isin(countries)]
    df = df[['Location', 'Corporate Tax Revenue', 'Potential Tax Lost',
            'Potential Real Corporate Tax Revenue', '% Tax Lost']]
    #df = df[['Location', 'Potential Tax Lost']]

    #ICD.display(df)
    return ColumnDataSource(df), df

def make_plot(src, df):
    max_height = max(df['Potential Real Corporate Tax Revenue'])
    p = figure(plot_width=500, plot_height=800, y_range=(0,max_height*1.5))
    N = df.shape[0]

    ind = np.arange(N)
    width = 0.3

    d = {}
    countries = list(df.Location)

    for i in ind:
        j = str(i+width)
        d[j] = countries[i]

    yvals1 = list(df['Corporate Tax Revenue'])
    p.vbar(x=ind, width=width, top=yvals1, bottom=0,
           color='red', legend='Corporate Tax Revenue')

    yvals2 = list(df['Potential Real Corporate Tax Revenue'])
    p.vbar(x=ind+width, width=width, top=yvals2,
           color='blue', legend='Potential Real Corporate Tax Revenue')

    p.xaxis.axis_label = 'Countries'
    p.yaxis.axis_label = 'Dollars (USD)'
    p.xaxis.ticker = [i + width for i in ind]
    p.xaxis.major_label_overrides = d
    p.xaxis.major_label_orientation = pi/2
    p.legend.label_text_font_size = "12px"

    return p

def update(attr, old, new):
    countries = multi_select.value
    src, df = make_dataset(countries)
    p = make_plot(src, df)
    text = get_stats(df)
    div = Div(text=text, width=200, height=100)
    controls = widgetbox(multi_select, div)
    layout.children[0] = controls
    layout.children[1] = p

def get_stats(df):
    most_tax_lost = df.loc[df['Potential Tax Lost'].idxmax()]
    most_tax_lost_as_perc = df.loc[df['% Tax Lost'].idxmax()]
    c_tax = most_tax_lost['Location']
    c_tax_perc = most_tax_lost_as_perc['Location']
    text = """
    <b>%s</b> has the most potential corporate tax lost by value at %s.<br><br>
    <b>%s</b> has the most potential corporate tax lost by percentage at %s.
    """ % (c_tax, '${:,.0f}'.format(most_tax_lost['Potential Tax Lost']),
           c_tax_perc, '{:,.2f}%'.format(most_tax_lost_as_perc['% Tax Lost']))
    return text

country_lst = [(x, x) for x in m3.Location]
multi_select = MultiSelect(title="Options", value=['Switzerland', 'Turkey', 'United Kingdom'],
                           options=country_lst)
multi_select.on_change('value', update)
multi_select.size = 35

countries = multi_select.value
src, df = make_dataset(countries)
p = make_plot(src, df)

text = get_stats(df)
div = Div(text=text, width=200, height=100)
controls = widgetbox(multi_select, div)

layout = row([controls, p])
curdoc().add_root(layout)
