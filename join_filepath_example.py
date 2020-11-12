# 1) Load in your streamflow timeseries from your data folder like this: 

# %%
import matplotlib as plt
import pandas as pd

# %%
filename = 'streamflow_week1.txt'
filepath = os.path.join('data', filename) #'data/streamflow_week1.txt'
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'],
                     parse_dates=['datetime'], index_col='datetime'
                     )
#Return the strea

# %%
Return the streamflow January 10-12 as many ways as you can

# %%
