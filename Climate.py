import streamlit as st
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import pyttsx3 

plt.style.use('seaborn-darkgrid')
import plotly.graph_objs as go 
from plotly.offline import init_notebook_mode,iplot,plot
init_notebook_mode(connected=True)
import plotly.express as px




st.set_page_config(page_title = "Climate Change Dashboard",
                   page_icon = ":cloud:",
                   layout ="wide",
                   )

from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Main Menu", ["Home","About Us", "Countrywise temperature Change","Yearwise temperature scatter","Boxplot temperature Variation","Global Warming","Carbon dioxide emission boxplot", "Carbon dioxide emission worldwide", "Social Message"], 
        icons=['house', 'gear'], menu_icon="cast", default_index=0)
    selected
st.markdown("The dashboard is designed is to increase the awareness of people about climate change")
  
data =  pd.read_csv("C:/Users/AVISHEK/Documents/Final_Data.csv")
if selected == 'Home':
    from PIL import Image
    import base64
    st.image("https://i0.wp.com/forestrypedia.com/wp-content/uploads/2018/06/Climate-Change-1.jpg?resize=1024%2C576&ssl=1")
    engine = pyttsx3.init()
    engine.say("Hello, Welcome to Dataviz Web App By Avishek") 
    engine.say("Please visit the menu to see different visualizations") 
    engine.runAndWait()
if selected == 'About Us':
    st.write("This web app is developed by Avishek Das for second semester examination")
    from PIL import Image
    import base64
    img = Image.open("photo@formal.jpg")
    st.image(img)
    engine = pyttsx3.init()
    engine.say("This web app is developed by Avishek Das for second semester examination") 
    engine.runAndWait()
    
if selected == 'Social Message':
    from PIL import Image
    import base64
    st.video("https://www.youtube.com/watch?v=QlQ-MEZgRGY")


fig = go.Figure()
if selected == 'Countrywise temperature Change':
    fig = px.choropleth(data, locations="Country_Code",
                    color="temp_change",
                    hover_name="Country ",
                    animation_frame="Year",
                    title = "Change of temperature with time", color_continuous_scale=px.colors.sequential.PuRd)
    fig.update_layout(
    title_text = 'Change of temperature',
    title_x = 0.5,
    geo=dict(
        showframe = False,
        showcoastlines = False,
    ))
    fig.show()
    engine = pyttsx3.init()
    engine.say("This visualization shows the change of temperture worldwide from 2005 to 2019")
    engine.say("The deeper color locates countires with higher temperature changes")
    engine.runAndWait()
elif selected == 'Yearwise temperature scatter':
    fig = px.scatter(data, x="Year", y="temp_change",title="Overall scatter of temperature")
    fig.show()
    fig.show()
    engine = pyttsx3.init()
    engine.say("This visualization shows the scatter of temperture change over the years")
    engine.runAndWait()
elif selected == 'Boxplot temperature Variation':
    fig = px.box(data, x="Year",y="temp_change",hover_name="temp_change",title="Year-wise variation of temperature")
    fig.show()
    engine = pyttsx3.init()
    engine.say("This boxplot visualization shows the variation of temperture change over the years along its mean value")
    engine.runAndWait()
elif selected == 'Global Warming':
    data1 = pd.read_csv("C:/Users/AVISHEK/Documents/city_climate.csv")
    fig = px.choropleth(data1, locations="iso3",
                    color="Global Warming",
                    hover_name="City",
                    title = "Change of temperature with time", color_continuous_scale=px.colors.sequential.PuRd)
    fig.update_layout(
    title_text = 'Global Warming from 2004 to 2021',
    title_x = 0.5,
    geo=dict(
        showframe = False,
        showcoastlines = False,
    ))
    fig.show()
    engine = pyttsx3.init()
    engine.say("This map shows the cities that has recored highest global warming in between 2004 to 2021 along with respective percentages")
    engine.runAndWait()
elif selected == 'Carbon dioide emission boxplot':
    data2= pd.read_csv("C:/Users/AVISHEK/Documents/CO2_Emissions.csv")
    data2.reset_index(level=0, inplace=True)
    data3=data2.melt(id_vars=['Country Name'], var_name='Year').sort_values(by=['Year'])
    country_col=data3[data3['Country Name']!='World'].groupby(by=['Country Name']).max().sort_values(by=['value'], ascending=False).head(10).index.to_list() 
    country_col.extend(['India','China'])
    fig = px.box(data_frame=data3[data3['Country Name'].isin(country_col)], x='value', y='Country Name', color='Country Name', title='Variation of Carbon dioxide emission by top 12 countries')
    fig.show()
    engine = pyttsx3.init()
    engine.say("This visualization shows the top 12 countries that emits carbon dioxide in maximum amount ")
    engine.runAndWait()
elif selected == 'Carbon dioxide emission worldwide':
    data2= pd.read_csv("C:/Users/AVISHEK/Documents/CO2_Emissions.csv")
    data2.reset_index(level=0, inplace=True)
    data3=data2.melt(id_vars=['Country Name'], var_name='Year').sort_values(by=['Year'])
    fig = px.choropleth(data_frame=data3[data3['Country Name']!='World'], locationmode='country names',locations='Country Name', color='value', animation_frame='Year', title='Carbon dioxide Emission by Countries by Year',color_continuous_scale=px.colors.sequential.RdBu_r, range_color=(200, 0))
    fig.show()
    engine = pyttsx3.init()
    engine.say("This animated map shows carbon dioxide emission by different countries worldwide from 1960 to 2017")
    engine.runAndWait()
st.plotly_chart(fig,use_container_width=True)
