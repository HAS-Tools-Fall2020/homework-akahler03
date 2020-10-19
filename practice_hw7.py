# Code to generate forecast using adjusting autoregressive model values

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime

# Set the file name and path to where you have stored the data
filename = 'streamflow_week7.txt'
filepath = os.path.join('homework-akahler03\data', filename)
print(os.getcwd())
print(filepath)


# %%
# Read the data into a pandas dataframe
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no', 'datetime',
                            'flow', 'code'],
                     parse_dates=['datetime']
                     )

# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).dayofweek
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# Aggregate flow values to weekly
flow_weekly = data.resample("W", on='datetime').mean()

# %%
# Building an autoregressive model
# Setting up arrays to be used for the model

flow_weekly['flow_tm1'] = flow_weekly['flow'].shift(1)
flow_weekly['flow_tm2'] = flow_weekly['flow'].shift(2)

# %%
# Selecting a date range of interest for detailed comparison.

last_sept = flow_weekly[(flow_weekly.year == 2019) & (flow_weekly.month == 9)]
this_sept = flow_weekly[(flow_weekly.year == 2020) & (flow_weekly.month == 9)]

# %%
# Creating a function to explore selected date range.


def flow_comparison(current, previous):
    """ This function determines the percentage decrease of flow values from
        historic to present, and is useful in adjusting forecast values.

        current - dataframe
        previous - dataframe

        It outputs a statement which is a useful supplement to looking at
        plots.
        """
    comp = (((current - previous)/previous) * 100).round(2)
    return print('change of', comp, 'percent')

# %%
# Utilizing the new function. It is helpful to have these numerical values
# while looking at the comparison plots.


flow_comparison(this_sept.flow[0], last_sept.flow[0])
flow_comparison(this_sept.flow[1], last_sept.flow[1])
flow_comparison(this_sept.flow[2], last_sept.flow[2])

# %%
# A plot to visualize October patterns

all_octobers = flow_weekly[flow_weekly.month == 10]

fig, ax = plt.subplots()
ax.plot(all_octobers.year, all_octobers.flow)
ax.set(title="All years October flow", xlabel='Date',
       ylabel="Weekly Avg Flow [cfs]")
ax.legend()
fig.show()

# %%
# This plot gives a visual of the trajectory we are on for this October

four_octobers = flow_weekly[(flow_weekly.year >= 2017) &
                            (flow_weekly.month == 10)]
fig, ax = plt.subplots()
ax.plot(four_octobers.year, four_octobers.flow)
ax.set(title="Four years of October flow", xlabel='Date',
       ylabel="Weekly Avg Flow [cfs]")
ax.legend()
fig.show()
# %%
# Jan 2015 through Jan 2018 for training, based on the relevance
# of recent history and the coefficient of determination.
train = flow_weekly['2017-01-01':'2019-01-01']
[['flow', 'flow_tm1', 'flow_tm2']]
test = flow_weekly['2019-01-01':'2020-10-03'][['flow', 'flow_tm1', 'flow_tm2']]

# %%
# Fitting a linear regression model using sklearn
model = LinearRegression()
x = train['flow_tm1'].values.reshape(-1, 1)
y = train['flow'].values
model.fit(x, y)

# This shows the results of the model calculations
r_sq = model.score(x, y)
print('coefficient of determination:', np.round(r_sq, 2))
print('intercept:', np.round(model.intercept_, 2))
print('slope:', np.round(model.coef_, 2))

# %%
# This predicts the model response for a  given flow value
q_pred_train = model.predict(train['flow_tm1'].values.reshape(-1, 1))
q_pred_test = model.predict(test['flow_tm1'].values.reshape(-1, 1))

# %%
# Use this flow value to make AR predictions for week 1 and week 2 forecasts
print(flow_weekly.tail(1))

# %%
# Enter the flow value shown in the above print statement
last_week_flow1 = 61.325
AR_one = model.intercept_ + model.coef_ * last_week_flow1
print('This is the AR model value for my week1 prediction:', AR_one.round(2))

# %%
# Enter the value predicted for AR_one
last_week_flow2 = 101.49
AR_two = model.intercept_ + model.coef_ * last_week_flow2
print('This is the AR model value for my week2 prediction:', AR_two.round(2))

# %%
# These will be the weekly flow values I would like to use for the
# forecast competition

week1 = model.intercept_ + model.coef_ * last_week_flow1*.3
print('Week one official forecast:', week1.round(2))
# %%
week2 = model.intercept_ + model.coef_ * week1*.3
print('Week one official forecast:', week2.round(2))

# %%
# Plotting training and observed flow from training start date

fig, ax = plt.subplots()
ax.plot(flow_weekly['flow'], color='green', label='full date range')
ax.plot(train['flow'], '2', color='red', label='training period')
ax.set(title="Observed Flow", xlabel='Date',
       ylabel="Weekly Avg Flow [cfs]",
       yscale='log', xlim=[datetime.date(2017, 1, 1),
                           datetime.date(2020, 10, 3)])
ax.legend()

# %%
# Line  plot comparison of predicted and observed flows
fig, ax = plt.subplots()
ax.plot(train['flow'], color='gray', linewidth=2, label='observed')
ax.plot(train.index, q_pred_train, color='blue', linestyle='--',
        label='simulated')
ax.set(title="Observed Flow", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
       yscale='log')
ax.legend()

# %%
# Scatter plot of t vs t-1 flow with normal axes
fig, ax = plt.subplots()
ax.scatter(train['flow_tm1'], train['flow'], marker='p',
           color='blueviolet', label='observations')
ax.set(xlabel='flow t-1', ylabel='flow t')
ax.plot(np.sort(train['flow_tm1']), np.sort(q_pred_train), label='AR model')
ax.legend()

plt.show()
