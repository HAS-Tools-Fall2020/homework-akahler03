# Code to generate forecast using adjusting autoregressive model values

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime
import json 
import urllib.request as req
import urllib

# %%

# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).dayofweek
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# Aggregate flow values to weekly
flow_weekly = data.resample("W", on='datetime').mean()

# %%
# ADDING NEW DATA FROM API
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
data2 = pd.DataFrame({'Temperature': airT}, index=pd.to_datetime(dateTime))

# Now convert this to daily data using resample
data2_daily = data2.resample('D').mean()
# Convert to weekly values
data2_weekly = data2.resample('W').mean()

# %%
# Plot temps
temp_test = data2_weekly.Temperature[:]
fig, ax = plt.subplots()
ax.plot(all_octobers.year, all_octobers.flow)
ax.set(title="All years October flow", xlabel='Date',
       ylabel="Weekly Avg Flow [cfs]")
ax.legend()
fig.show()


all_octobers = flow_weekly[flow_weekly.month == 10]
fig, ax = plt.subplots()
ax.plot(all_octobers.year, all_octobers.flow)
ax.set(title="All years October flow", xlabel='Date',
       ylabel="Weekly Avg Flow [cfs]")
ax.legend()
fig.show()

# %%
# Building an autoregressive model
# Setting up arrays to be used for the model
flow_weekly['flow_tm1'] = flow_weekly['flow'].shift(1)
flow_weekly['flow_tm2'] = flow_weekly['flow'].shift(2)

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
    print('change of', comp, 'percent')
    return comp


# %%
# Selecting a date range of interest for detailed comparison.
oct_2019 = flow_weekly[(flow_weekly.year == 2019) & (flow_weekly.month == 10) & (flow_weekly.day <= 17)]
oct_2020 = flow_weekly[(flow_weekly.year == 2020) & (flow_weekly.month == 9) & (flow_weekly.day <= 17)]

# Utilizing the new function to inform the percent decrease chosen for my
# forecast calculations
week1 = flow_comparison(oct_2020.flow[0], oct_2019.flow[0])
week2 = flow_comparison(oct_2020.flow[1], oct_2019.flow[1])
week3 = flow_comparison(oct_2020.flow[2], oct_2019.flow[2])

# %%
# A plot to represent Octobers of entire date range
all_octobers = flow_weekly[flow_weekly.month == 10]
fig, ax = plt.subplots()
ax.plot(all_octobers.year, all_octobers.flow)
ax.set(title="All years October flow", xlabel='Date',
       ylabel="Weekly Avg Flow [cfs]")
ax.legend()
fig.show()

# %%
# Jan 2017 through Jan 2019 for training, based on the relevance
# of recent history and the coefficient of determination produced
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
# Using the most recent shifted flow value as a starting point for 
# autoregressive one and two week forecast values
start_val = flow_weekly.flow_tm1.tail(1)

AR_one = (model.intercept_ + model.coef_ * start_val).round(2).values
print(AR_one, 'is the AR model value for my one week prediction')
AR_two = (model.intercept_ + model.coef_ * AR_one).round(2)
print(AR_two, 'is the AR model value for my two week prediction')

# %%
# Calculations for my official one and two week predictions
decrease_by = .25
one_week = ((model.intercept_ + model.coef_ * start_val*decrease_by)-2).round(2).values
two_week = ((model.intercept_ + model.coef_ * one_week*decrease_by)-2).round(2)
print('One week official forecast:', one_week,'Two week official forecast:', two_week)
# %%
# Sixteen week forecast calculations
# Utilize function to evaluate percent decrease 
aug_2019 = flow_weekly['2019-08-01':'2019-08-21']
aug_2020 = flow_weekly['2020-08-01':'2020-08-21']
aug_one = flow_comparison(aug_2020.flow[0], aug_2019.flow[0])
aug_two = flow_comparison(aug_2020.flow[1], aug_2019.flow[1])
aug_three = flow_comparison(aug_2020.flow[2], aug_2019.flow[2])

# %%
# Set value
decrease_by = .37

# Each month starts with the same date value of previous year input into the
# prediction equation and reduced by the informed value decrease_by
start_aug16 = flow_weekly.loc['2019-08-15':'2019-08-15'].flow.values
one_16 = (model.intercept_ + model.coef_ * start_aug16*decrease_by).round(2)
two_16 = (model.intercept_ + model.coef_ * one_16*decrease_by).round(2)

# %%
# This is the beginning of creating a loop to streamline the 16 week forecast,
# with a function to calculate each value
start = ["2019-08-01", '2019-09-01', '2019-09-07']
stop = ["2019-08-21", '2019-09-01', '2019-09-07']
i = 0
start_temp = flow_weekly.loc[start[i]:stop[i]].flow.values
one_temp = (model.intercept_ + model.coef_ * start_temp*decrease_by).round(2)
two_temp = (model.intercept_ + model.coef_ * one_temp*decrease_by).round(2)
print(one_temp, two_temp)


# %%
start_sept16 = flow_weekly.loc['2019-09-01':'2019-09-07'].flow.values
three_16 = (model.intercept_ + model.coef_ * start_sept16*decrease_by).round(2)
four_16 = (model.intercept_ + model.coef_ * three_16*decrease_by).round(2)
five_16 = (model.intercept_ + model.coef_ * four_16*decrease_by).round(2)
six_16 = (model.intercept_ + model.coef_ * five_16*decrease_by).round(2)

# Reducing further to accomodate downward trend in recent Octobers
decrease_by = .20
start_oct16 = flow_weekly.loc['2019-10-01':'2019-10-07'].flow.values
seven_16 = (model.intercept_ + model.coef_ * start_oct16*decrease_by).round(2)
eight_16 = (model.intercept_ + model.coef_ * seven_16*decrease_by).round(2)
nine_16 = (model.intercept_ + model.coef_ * eight_16*decrease_by).round(2)
ten_16 = (model.intercept_ + model.coef_ * nine_16*decrease_by).round(2)

# Adjusting in anticipation of a return to seasonal norms
decrease_by = .35
start_nov16 = flow_weekly.loc['2019-11-01':'2019-11-07'].flow.values
eleven_16 = (model.intercept_ + model.coef_ * start_nov16*decrease_by).round(2)
twelve_16 = (model.intercept_ + model.coef_ * eleven_16*decrease_by).round(2)
thirteen_16 = (model.intercept_ + model.coef_ * twelve_16*decrease_by).round(2)
fourteen_16 = (model.intercept_ + model.coef_ * thirteen_16*decrease_by).round(2)

decrease_by = .40
start_dec16 = flow_weekly.loc['2019-12-01':'2019-12-07'].flow.values
fifteen_16 = (model.intercept_ + model.coef_ * start_dec16*decrease_by).round(2)
sixteen_16 = (model.intercept_ + model.coef_ * fifteen_16*decrease_by).round(2)

# %%
print('one:', one_16, 'two:', two_16, 'three:', three_16, 'four:', four_16,
      'five:', five_16, 'six:', six_16, 'seven:', seven_16, 'eight:', eight_16,
      'nine:', nine_16, 'ten:', ten_16, 'eleven:', eleven_16, 'twelve:',
      twelve_16, 'thirteen:', thirteen_16, 'fourteen:', fourteen_16, 'fifteen:',
      fifteen_16, 'sixteen:', sixteen_16)

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
