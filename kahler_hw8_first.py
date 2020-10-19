# Code to generate forecast using adjusting autoregressive model values

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime
import pandas as pd

# %%
# Set the file name and path to where you have stored the data
filename = 'streamflow_week8.txt'
filepath = os.path.join('homework-akahler03\data', filename)
# do ../ to get up to correct directory
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
flow_weekly['flow_tm3'] = flow_weekly['flow'].shift(3)

# %%
data.describe
flow_weekly.describe
flow_weekly.head()
# %%
# Find quartiles of Octobers in range
oct_2019 = flow_weekly.flow['2019-10-01' : '2019-10-17'].quantile([0.25,0.5,0.75])
oct_2020 = flow_weekly.flow['2020-10-01' : '2020-10-17'].quantile([0.25,0.5,0.75])

#%%
# Quantiles for analysis by week
#Plotting the histogram
plt.hist(semwk4[:,3], bins = mybins)
plt.title('Streamflow')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')

# Get the quantiles of flow
# Two different approaches ---  you should get the same answer
# just using the flow column
flow_quants1 = np.quantile(semwk4[:,3], q=[0,0.1, 0.5, 0.9])
print('Method one flow quantiles:', flow_quants1)

# %%
# This kind of works, could take to office hours
# Lag 2020 by two timesteps
# Could take quartiles of each year and use to adjust AR predictions


jun_oct2020 = flow_weekly['flow_tm2']['2020-06-01' : '2020-10-17'].values
jun_oct2019 = flow_weekly.flow['2019-06-01' : '2019-10-12'].values
len(jun_oct2019)
len(jun_oct2020)
jun_oct20_quant = flow_weekly['flow_tm2']['2020-06-01' : '2020-10-17'].quantile([0.25,0.5,0.75])
jun_oct19_quant = flow_weekly.flow['2019-06-01' : '2019-10-12'].quantile([0.25,0.5,0.75])

fig, ax = plt.subplots()
ax.plot(jun_oct2020, color= 'green', label='June-Oct 2020')
ax.plot(jun_oct2019, color='red', label='June-Oct 2019')
ax.set(title="June 1st through Oct. 17th", xlabel='data point', 
        ylabel="Weekly Avg Flow [cfs]")
ax.legend()



# %%
# Office hours: ask about linestyle and transparency

mybins = 10
plt.hist(jun_oct2020, bins = mybins)
plt.hist(jun_oct2019, bins = mybins)
plt.title('2019 and 2020 June through October flow')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')

# %%

# Hold this thought -  is there a better way to reference/identify these dates?
# Write a function to return flow values and comparisons?
oct_2018 = flow_weekly[(flow_weekly.year == 2019) & (flow_weekly.month == 9)]
this_sept = flow_weekly[(flow_weekly.year == 2020) & (flow_weekly.month == 9)]


# %%
# OLD
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
# Office hours loop?

flow_comparison(this_sept.flow[0], last_sept.flow[0])
flow_comparison(this_sept.flow[1], last_sept.flow[1])
flow_comparison(this_sept.flow[2], last_sept.flow[2])

for i in (jun_oct2020):
    flow_comparison(jun_oct2020[i], jun_oct2019[i])

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
# Jan 2015 through Jan 2018 for training, based on the relevance
# of recent history and the coefficient of determination.
#train = flow_weekly['2017-01-01':'2019-01-01']
#[['flow', 'flow_tm1', 'flow_tm2']]
#test = flow_weekly['2019-01-01':'2020-10-03'][['flow', 'flow_tm1', 'flow_tm2']]

# %%
train = flow_weekly['2017-01-01':'2019-01-01']
[['flow','flow_tm1','flow_tm2']]
test = flow_weekly['2019-01-01':'2020-10-17'][['flow', 'flow_tm1', 'flow_tm2']]

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
