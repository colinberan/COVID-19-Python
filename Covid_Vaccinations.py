#Analysis of COVID-19 World Vaccination Progress (https://www.kaggle.com/gpreda/covid-world-vaccination-progress)
#Script by Colin Beran

import numpy as np
import pandas as pd
from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.express as px


#Import .csv file
df = pd.read_csv("E:/Users/Colin/Documents/Data Science/Data Sets/country_vaccinations.csv")
df

#Start by filtering data down to total vaccinations for each country.
#Also interested in "date" to check how recent this information is.

recent_date = df['date'].max()

df_total_vaccinations = df.groupby(by=['country'])[['date', 'total_vaccinations']].max().reset_index()
df_total_vaccinations_top20 = df_total_vaccinations.sort_values(by=['total_vaccinations'], ascending = False).iloc[0:20].reset_index(drop=True)

#Plot of total vaccinations for top 20 most vaccinated countries as of most recent update.
trace1 = go.Bar(
            x = df_total_vaccinations_top20['country'], 
            y = df_total_vaccinations_top20['total_vaccinations'])
layout = dict(title={
            'text': "COVID-19 Vaccinations as of " + str(recent_date),
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
            xaxis_title="Country",
            yaxis_title="Vaccination Count")
fig = go.Figure(data = trace1, layout = layout)

iplot(fig)

#Let's see the same data, but globally.
trace2 = go.Choropleth(
            locations = df_total_vaccinations['country'],
            locationmode='country names',
            z = df_total_vaccinations['total_vaccinations'],
            text = df_total_vaccinations['country'])
layout = dict(title={
            'text': "Global COVID-19 Vaccinations as of " + str(recent_date),
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},)
fig2 = go.Figure(data = trace2, layout = layout)

iplot(fig2)

#See how top 20 countries are doing in terms of percentage of people vaccinated
df_percent_vacc = df.groupby(by=['country'])[['date', 'people_vaccinated_per_hundred']].max().reset_index()
df_percent_vacc_top20 = df_percent_vacc.sort_values(by=['people_vaccinated_per_hundred'], ascending = False).iloc[0:20].reset_index(drop=True)

trace3 = go.Bar(
            x = df_percent_vacc_top20['people_vaccinated_per_hundred'],
            y = df_percent_vacc_top20['country'],
            orientation = 'h')
layout = dict(title={
            'text': "COVID-19 Vaccination by Percentage of Population as of " + str(recent_date),
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
            xaxis_title="Percentage of Population",
            yaxis_title="Country",
            yaxis = dict(autorange='reversed'))
fig3 = go.Figure(data = trace3, layout = layout)

iplot(fig3)

#Again, same data but globally.
trace4 = go.Choropleth(
            locations = df_percent_vacc['country'],
            locationmode='country names',
            z = df_percent_vacc['people_vaccinated_per_hundred'],
            text = df_percent_vacc['country'])
layout = dict(title={
            'text': "COVID-19 Vaccination by Percentage of Population as of " + str(recent_date),
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
fig4 = go.Figure(data = trace4, layout = layout)

plot(fig4)