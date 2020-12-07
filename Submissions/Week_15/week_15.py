
# %%
import pandas as pd
import numpy as np
import os as os
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

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
    # Input start and end dates
site = '09506000'
start = '1990-01-01'
# Last date available for 16 week forecast
end = '2020-12-07'

url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=" + \
      site + "&referred_module=sw&period=&begin_date=" + start + \
      "&end_date=" + end
data = pd.read_table(url, skiprows=30, names=['agency_cd', 'site_no',
                                              'datetime', 'flow', 'code'],
                     parse_dates=['datetime'])

data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).dayofweek
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# Aggregate flow values to weekly
flow_weekly = data.resample("W", on='datetime').mean()

# Set flow_weekly to natural log
flow_weekly_log = np.log(flow_weekly)
flow_weekly_log['flow_tm1'] = flow_weekly_log['flow'].shift(1)

# %%
train = flow_weekly_log['2017-01-01':'2019-01-01'][['flow', 'flow_tm1']]
model = LinearRegression()
x = train['flow_tm1'].values.reshape(-1, 1)
y = train['flow'].values
model.fit(x, y)

r_sq = model.score(x, y)
#print('coefficient of determination:', np.round(r_sq, 2))

# %%
# Starting value
start_val = flow_weekly.flow[-3]

# starting value in natural log (needed for regression)
start_val_ln = np.log(start_val)

# create two week forecast (saved in natural log)
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

