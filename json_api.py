# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 17:32:19 2020

@author: Dell Latitude E6430
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import json 
import urllib.request as req
import urllib
# %%

mytoken = '1e85cbb5763f4db39d33ab9ca6cb55a9'
url = "https://api.synopticdata.com/v2/stations/timeseries?&token=\
        1e85cbb5763f4db39d33ab9ca6cb55a9&start=202010171201&end=202010251201&timeformat=\
        %Y%m%d&obtimezone=local&units=english&output=json&country=us&state=AZ&county=Yavapai"
base_url = "https://api.synopticdata.com/v2/stations/timeseries"
# This is a dictionary. Watch for the curly brackets.
args = {
    'start': '201810010000', 
    'end': '202010240000',
    'obtimezone': 'UTC',
    'vars': 'air_temp',
    'stids': 'QVDA3',
    'units': 'temp|F,precip|mm',
    'token': mytoken} 
# %%
apiString = urllib.parse.urlencode(args)
print(apiString)
fullUrl = base_url + '?' + apiString
print(fullUrl)

# %%
# This creates a dictionary 
response = req.urlopen(fullUrl)
responseDict = json.loads(response.read())

#Keys shows you the main elements of your dictionary
responseDict.keys()
responseDict['UNITS']
#Each key in the dictionary can link to differnt data structures
#For example 'UNITS is another dictionary'
type(responseDict['UNITS'])
responseDict['UNITS'].keys()
responseDict['UNITS']['position']

#where as STATION is a list 
type(responseDict['STATION'])
responseDict['STATION']
# If we grab the first element of the list that is a dictionary
type(responseDict['STATION'][0])
# And these are its keys
responseDict['STATION'][0].keys()

# %%
# We can get to the data we want like this: 
dateTime = responseDict['STATION'][0]['OBSERVATIONS']['date_time']
airT = responseDict['STATION'][0]['OBSERVATIONS']['air_temp_set_1']

# Combine this into a pandas dataframe
data = pd.DataFrame({'Temperature': airT}, index=pd.to_datetime(dateTime))

# Now convert this to daily data using resample
data_daily = data.resample('D').mean()
# Convert to weekly values
data_weekly = data.resample('W').mean()

# %%
data_weekly.loc['2018-10-07']
