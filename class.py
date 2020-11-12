# 1) Load in your streamflow timeseries from your data folder like this: 
filename = 'streamflow_week1.txt'
filepath = os.path.join('../../data', streamflow_wk3.txt)
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'],
                     parse_dates=['datetime'], index_col='datetime'
                     )
Return the strea

# %%
Return the streamflow January 10-12 as many ways as you can

# %%
