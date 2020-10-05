#%%
import os
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np
import earthpy as et
# %%
#set url to a variable
wk5_data_url="https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=09506000&referred_module=sw&period=&begin_date=1989-01-01&end_date=2020-09-23"

#%%
#download file from url
#et.data.get_data(url=wk5_data_url#)

# %%
#FROM WEEK 4
# Set the file name and path to where you have stored the data
data = 'streamflow_week5.txt'
filepath = os.path.join('data', data)
print(os.getcwd())
print(filepath)

# %%
#Import data from .csv file (training materials)
#why doesn't this work?
#wk5=pd.read_csv(filename)
# %%
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'])
# %%
