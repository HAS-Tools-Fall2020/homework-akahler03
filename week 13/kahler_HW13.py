
# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import rioxarray
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import seaborn as sns
import geopandas as gpd
import fiona
import shapely
from netCDF4 import Dataset
from sklearn.linear_model import LinearRegression

# %%
# Net CDF file historical time series
# https://towardsdatascience.com/handling-netcdf-files-using-xarray-for-absolute-beginners-111a8ab4463f
data_path = os.path.join('../data',
                         'tempdailyave_NECP.nc')
# Read in the dataset as an x-array
dataset = xr.open_dataset(data_path)

# %%
# Focusing on just the temp values
airtemp = dataset['air']

# Slicing data for graphing one point
lat = dataset["air"]["lat"].values[0]
lon = dataset["air"]["lon"].values[0]
time = dataset['air']['time'].values[0]
print("Long, Lat values:", lon, lat)
first_point = dataset["air"].sel(lat=lat,lon=lon) #time=['2019-09-01', '2019-11-12'])
year_2020 = first_point.tail(320)
year_2019 = first_point.head(362)

# %%
year_2019.plot.line()
year_2020.plot.line()

# %%
# Timeseries plot to compare year trends
f, ax = plt.subplots(figsize=(12, 6))
ax.set_facecolor('lavender')
year_2019.plot.line(hue='lat',
                    marker="d",
                    ax=ax,
                    color="white",
                    markerfacecolor="white",
                    markeredgecolor="black",)
ax.set(title="2019 Air Temp for Single Lat / Lon Location")

f, ax = plt.subplots(figsize=(12, 6))
ax.set_facecolor('lavender')
year_2020.plot.line(hue='lat',
                    marker="d",
                    ax=ax,
                    color="white",
                    markerfacecolor="white",
                    markeredgecolor="black",)
ax.set(title="2020 Air Temp for Single Lat / Lon Location")

# %%
#Convert to dataframe
first_point_df = first_point.to_dataframe()

# %%
year_19 = first_point_df['2019-01-01' : '2019-12-31']
year_20 = first_point_df['2020-01-01' : '2020-12-31']

# %%
# These temps are too low to be accurate
max19 = year_19.air.max()
print('max temp 2019 range', (((max19 - 273.15) * (9/5)) + 32).round(2))
max20 = year_20.air.max()
print('max temp 2020 range',((max20 - 273.15) * (9/5) + 32).round(2))

# %%
# Input start and end dates
site = '09506000'
start = '1990-01-01'
end = '2020-08-21'

url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=" + \
      site + "&referred_module=sw&period=&begin_date=" + start + \
      "&end_date=" + end
data = pd.read_table(url, skiprows=30, names=['agency_cd', 'site_no',
                                              'datetime', 'flow', 'code'],
                     parse_dates=['datetime'])

# %%
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).dayofweek
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# Aggregate flow values to weekly
flow_weekly = data.resample("W", on='datetime').mean()

# %%
# Set flow_weekly to natural log
flow_weekly_log = np.log(flow_weekly)
flow_weekly_log['flow_tm1'] = flow_weekly_log['flow'].shift(1)

# %%
# Select years for training and fit the model
train = flow_weekly_log['2017-01-01':'2019-01-01'][['flow', 'flow_tm1']]
model = LinearRegression()
x = train['flow_tm1'].values.reshape(-1, 1)
y = train['flow'].values
model.fit(x, y)

r_sq = model.score(x, y)
print('coefficient of determination:', np.round(r_sq, 2))

# %%
def single_forecast(model, x):
    """Function performing the forecast calculation, where
        model = model used to generate prediction
            (must be a log to log scale autoregression)
        x = starting value of streamflow, can be integer or float
            (input must be in natural log scale!)

        returns: a prediction
            (note the prediction is returned in natural log scale)
            (however, the result is printed in nonlog scale)
    """
    # makes a prediction (in log space)
    prediction = (model.intercept_ + model.coef_ * x)
    # prints a prediction (in arithmetic space)
    print('forecast value', np.exp(prediction).round(2))
    # returns prediction (in log space)
    return prediction

# %%
# Starting value for model prediction
start_val = flow_weekly.flow[-3]
# starting value in natural log (needed for regression)
start_val_ln = np.log(start_val)
# create two week forecast (saved in natural log)
# set adjusting value for forecast
adjust = 1.05
print('one week')
first_forecast = single_forecast(model, start_val_ln*adjust)
print('two week')
second_forecast = single_forecast(model, first_forecast*adjust)

# %%
adjust = 1.0
sixteen_week_forecast = np.zeros(4)
for i in range(4):
    print('week',i+1)
    sixteen_week_forecast[i] = single_forecast(model, first_forecast * adjust)
    first_forecast = sixteen_week_forecast[i]
adjust = 1.01
sixteen_week_forecast2 = np.zeros(4)
for i in range(4):
    print('week',i+5)
    sixteen_week_forecast2[i] = single_forecast(model, first_forecast * adjust)
    first_forecast = sixteen_week_forecast2[i]
adjust = 1.03
sixteen_week_forecast3 = np.zeros(4)
for i in range(4):
    print('week',i+9)
    sixteen_week_forecast3[i] = single_forecast(model, first_forecast * adjust)
    first_forecast = sixteen_week_forecast3[i]
adjust = 1.02
sixteen_week_forecast4 = np.zeros(4)
for i in range(4):
    print('week',i+13)
    sixteen_week_forecast4[i] = single_forecast(model, first_forecast * adjust)
    first_forecast = sixteen_week_forecast4[i]


# %%
