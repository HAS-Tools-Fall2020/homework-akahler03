
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
import forecast_functions as ff

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
end = '2020-11-14'

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
# Dry years for training model
train = flow_weekly_log['2017-01-01':'2019-01-01'][['flow', 'flow_tm1']]

# Fitting the model
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
# Identify starting value for model prediction
start_val = flow_weekly.flow[-1]
# starting value in natural log (needed for regression)
start_val_ln = np.log(start_val)
# create two week forecast (saved in natural log)
# set adjusting value for forecast

first_forecast = single_forecast(model, start_val_ln)

# %%
# Beginning loop with proper form
# Building entire 16 week forecast from one starting value
adjust = 1.01
sixteen_week_forecast = np.zeros(16)
for i in range(16):
    print('week',i)
    sixteen_week_forecast[i] = single_forecast(model, first_forecast * adjust)
    first_forecast = sixteen_week_forecast[i]

# %%
# Goal: let each month's prediction have their own starting value
# Issues using datetime index to identify starting flow value
adjust = 1.01
sixteen_week_forecast = np.zeros(16)
for i in range(16):
    print('week',i)
    start_date = flow_weekly[(flow_weekly.year == '2019') & (flow_weekly.month == 8) &
                  (flow_weekly.day == 11)].flow
    sixteen_week_forecast[i] = single_forecast(model, start_date.flow * adjust)
    first_forecast = sixteen_week_forecast[i]

# "start_val" in the first loop is a numpy float, and works
# "start_date" in this loop is a numpy float, but does not work. KeyError '2019-08-01'









# %%
# REDUNDANT WAY
#sixteen_week_forecast = np.zeros(16)
for i in range(1):
    print('week',[i])
    sixteen_week_forecast[i] = single_forecast(model, first_forecast * adjust)
    for j in range (16):
          print('week', [j])
          sixteen_week_forecast[j] = single_forecast(model, sixteen_week_forecast[j-1]*adjust)




# %%
    adjust = 1.03
    print('week', [i+1])
    two_week_forecast[1] = single_forecast(model, two_week_forecast[0] * adjust)




# %%
# Sixteen week forecast calculations
# Set value
adjust = 1.1

# Each month starts with the same date value of previous year input into the
# prediction equation and reduced by the informed value adjust
start_aug16 = flow_weekly.loc['2019-08-15':'2019-08-15'].flow.values
one_16 = single_forecast(model, start_val_ln)
two_16 = single_forecast(model, one_16*adjust).round(2)
print(one_16, two_16)
# %%
# This is a work in progress to streamline and clarify 16 week forecast
start = ["2019-08-01", '2019-09-01', '2019-09-07']
stop = ["2019-08-21", '2019-09-01', '2019-09-07']
i = 0
start_temp = flow_weekly.loc[start[i]:stop[i]].flow.values
one_temp = (model.intercept_ + model.coef_ * start_temp*adjust).round(2)
two_temp = (model.intercept_ + model.coef_ * one_temp*adjust).round(2)
print(one_temp, two_temp)


# %%
# Starting value for each month is the same week of the previous year
# The calculation for each output includes an estimated adjustment
adjust = 1.2
start_sept16 = flow_weekly.loc['2019-09-01':'2019-09-07'].flow.values
three_16 = (model.intercept_ + model.coef_ * start_sept16*adjust).round(2)
four_16 = (model.intercept_ + model.coef_ * three_16*adjust).round(2)
five_16 = (model.intercept_ + model.coef_ * four_16*adjust).round(2)
six_16 = (model.intercept_ + model.coef_ * five_16*adjust).round(2)

# Increasing the percent reduction to reflect lower October values
# This is a new month, with a starting value taken from the same week of the
# previous year
#adjust = 1
start_oct16 = flow_weekly.loc['2019-10-01':'2019-10-07'].flow.values
seven_16 = (model.intercept_ + model.coef_ * start_oct16*adjust).round(2)
eight_16 = (model.intercept_ + model.coef_ * seven_16*adjust).round(2)
nine_16 = (model.intercept_ + model.coef_ * eight_16*adjust).round(2)
ten_16 = (model.intercept_ + model.coef_ * nine_16*adjust).round(2)

# Reducing the percent reduction in anticipation of a return to seasonal norms
# for November
#adjust = 1
start_nov16 = flow_weekly.loc['2019-11-01':'2019-11-07'].flow.values
eleven_16 = (model.intercept_ + model.coef_ * start_nov16*adjust).round(2)
twelve_16 = (model.intercept_ + model.coef_ * eleven_16*adjust).round(2)
thirteen_16 = (model.intercept_ + model.coef_ * twelve_16*adjust).round(2)
fourteen_16 = (model.intercept_ + model.coef_ * thirteen_16*adjust).round(2)

start_dec16 = np.log(flow_weekly.loc['2019-12-01':'2019-12-07'].flow.values)
fifteen_16 = (model.intercept_ + model.coef_ * start_dec16*adjust).round(2)
sixteen_16 = (model.intercept_ + model.coef_ * fifteen_16*adjust).round(2)

print('one:', one_16, 'two:', two_16, 'three:', three_16, 'four:', four_16,
      'five:', five_16, 'six:', six_16, 'seven:', seven_16, 'eight:', eight_16,
      'nine:', nine_16, 'ten:', ten_16, 'eleven:', eleven_16, 'twelve:',
      twelve_16, 'thirteen:', thirteen_16, 'fourteen:', fourteen_16, 'fifteen:',
      fifteen_16, 'sixteen:', sixteen_16)

# %%
