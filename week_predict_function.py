# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 10:42:32 2020

@author: Dell Latitude E6430
"""
# %%
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime
import json 
import urllib.request as req
import urllib
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# %%
def week_predict(start_val, percent_change):
    """This function will return a one-week forecast value using the
       coefficient of determination and model intercept with the user inputs.
       
       start_val - array
       percent_change - float
       
       It returns a single numpy array forecast value for an individual week.
       """
    one_week = ((model.intercept_ + model.coef_* start_val * percent_change)-2).round(2)
    print('forecast value', one_week)
    return one_week