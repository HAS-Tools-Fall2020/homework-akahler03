# Start code for assignment 3
# this code sets up the lists you will need for your homework
# and provides some examples of operations that will be helpful to you

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week3.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)

# %%
# DON'T change this part -- this creates the lists you 
# should use for the rest of the assignment
# no need to worry about how this is being done now we will cover
# this in later sections. 

#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

#make lists of the data
flow = data.flow.values.tolist()
date = data.datetime.values.tolist()
year = data.year.values.tolist()
month = data.month.values.tolist()
day = data.day.values.tolist()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%
# Here is some starter code to illustrate some things you might like to do
# Modify this however you would like to do your homework. 
# From here on out you should use only the lists created in the last block:
# flow, date, yaer, month and day

# Calculating some basic properites
print(min(flow))
print(max(flow))
print(np.mean(flow))
print(np.std(flow))

#%%
# Making and empty list that I will use to store
# index values I'm interested in
ilist = []

# Loop over the length of the flow list
# and adding the index value to the ilist
# if it meets some criteria that I specify
for i in range(len(flow)):
        if flow [i] > 600 and month[i] == 7:
                ilist.append(i)

# see how many times the criteria was met by checking the length
# of the index list that was generated
print(len(ilist))
print(ilist)

#%%
##THIS IS THE ONE THIS IS THE ONE THIS IS THE ONE
import numpy as np
#week1=[flow[i] for i in range(len(year)) if year[i]>2015 and month[i]==9 \
 #       and 13<=day[i]<=19]
#FOR LIST OF THE INDECES YOU NEED:
index_of_days=[i for i in range(len(year)) if year[i]>2015 and month[i]==9 \
        and 13<=day[i]<=19]
list_years=[year[i] for i in index_of_days]
print(list_years)
week1_flow=[flow[i] for i in index_of_days]
print(week1_flow)
week1_mean=np.mean(week1_flow)
fore1=week1_mean*.86
print(fore1)
#%%
# REPEATING THE ABOVE FOR EACH WEEK OF SEMESTER
index_of_days=[i for i in range(len(year)) if year[i]>2015 and month[i]==12 \
        and 6<=day[i]<=12]
list_years=[year[i] for i in index_of_days]
print(list_years)
week1_flow=[flow[i] for i in index_of_days]
print(week1_flow)
week1_mean=np.mean(week1_flow)
fore1=week1_mean*.86
print(fore1)
#%% THIS IS THE THOUGHT FRAMEWORK FOR FUTURE LOOP OR LIST STATEMENT
week1=[flow[i] for i in range(len(year)) if flow[i]>46 and month[i]==9 \
        and 1<day[i]<8]
length_days1=(len(week1))
week2=[flow[i] for i in range(len(year)) if flow[i]>39 and month[i]==9 \
        and 1<day[i]<8]
length_days2=(len(week2))
week3=[flow[i] for i in range(len(year)) if flow[i]>78 and month[i]==9 \
        and 1<day[i]<8]
length_days3=(len(week3))
week4=[flow[i] for i in range(len(year)) if flow[i]>85 and month[i]==9 \
        and 1<day[i]<8]
length_days4=(len(week4))
print(length_days4)


total=(length_days1+ length_days2+length_days3+length_days4)
print(total)


#%%
week2=[flow[i] for i in range(len(year)) if year[i]<2010 and flow[i]>39 and month[i]==9]
length_days2=(len(week2))
length2=(length_days2/4)
print(length2)
week3=[flow[i] for i in range(len(year)) if year[i]<2010 and flow[i]>78 and month[i]==9]
length_days3=(len(week3))
length3=(length_days3/4)
print(length3)
week4=[flow[i] for i in range(len(year)) if year[i]<2010 and flow[i]>85 and month[i]==9]
length_days4=(len(week4))
length4=(length_days/4)
print(length4)
#%%
print(82.5+82.5+80+234)
print(479/4)

#%%
#WEEK ONE PREDICTION

print(list_years)
print(week1)
print(np.mean(week1))

#%%
#
#GOAL: TO FIND DAILY FLOW IN five_year_sept LIST
#five_year_daily=[five_year_daily[x] for x in range(len(year)) if ]

#for x in five_year_sept:
     #   print(flow[x])
#%%
#
#GOAL: TO SHOW DAILY VALUES IN SEPT 2019
for i in range(len(year)):
        if year[i]==2019 and month[i]==9 and day[i]<13:
                #print(flow[i])
        if flow[i]<90:
                print(day[i])
#%%
#TEST 1
for i in range(len(year)):
        if year[i]==2019 and month[i]==9 and flow[i]<60:
                print(day[i])
for i in range(len(year)):
        if year[i]==2019 and month[i]==9:
                print(flow[i])
#%%
for i in range(len(year)):
        if year[i]==2019 and month[i]==9 and day[i]<13 and flow[i]>60:
                print(day[i])

#%%
#
#GOAL: TO FIND DAILY VALUES OF THE FIVE_YEAR SEPTEMBERS
five_year_flow=[five_year[j]]

#%%
year_list=[y for y in range(len(year)) if year[y]>2015 and flow[y]>=100]
maxflow_5year=max([flow[j] for j in year_list])
print(maxflow_5year)
#%%
total_years=[year[z] for z in year_list]
print(len(list(set(total_years))))
#%%
month_list=[month[x] for x in year_list]
#%%


#%%
# Alternatively I could have  written the for loop I used 
# above to  create ilist like this
ilist2 = [i for i in range(len(flow)) if flow[i] > 600 and month[i]==7]
print(len(ilist2))

# Grabbing out the data that met the criteria
# This  subset of data is just the elements identified 
# in the ilist
subset = [flow[j] for j in ilist]
print(subset)
ilist==ilist2
# %%

#MY PRACTICE AND FORECAST CODE BELOW

# %%
# Making and empty list that I will use to store
# index values I'm interested in
ilist = []

# Loop over the length of the flow list
# and adding the index value to the ilist
# if it meets some criteria that I specify
for i in range(len(flow)):
        if  month[i] == 7 and flow[i]>100 and year[i] >=2015:
                ilist.append(i)
print(ilist)
flow_val=[flow[j] for j in ilist]

# see how many times the criteria was met by checking the length
# of the index list that was generated
print(len(ilist))
print(flow[9681])

#%%
# Alternatively I could have  written the for loop I used 
# above to  create ilist like this
ilist2 = [i for i in range(len(flow)) if flow[i] > 600 and month[i]==7]
print(len(ilist2))

# Grabbing out the data that met the criteria
# This  subset of data is just the elements identified 
# in the ilist
subset = [flow[j] for j in ilist]
# %%
