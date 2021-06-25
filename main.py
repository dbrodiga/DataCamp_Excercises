import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import calendar

seattle_weather = pd.read_csv('DataCamp M5/seattle_weather.csv')

#seattle_weather['MONTH'] = pd.to_datetime(seattle_weather['DATE'], format='%b')
seattle_weather['MONTH'] = seattle_weather['DATE'].calendar.month_abbr