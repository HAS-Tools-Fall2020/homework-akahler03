<<<<<<< Updated upstream
# Starter code for Homework 4

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week4.txt'
filepath = os.path.join('data', filename)
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

# Make a numpy array of this data
flow_data = data[['year', 'month','day', 'flow']].to_numpy()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%
# Question number 3
flow_count = np.sum((flow_data[:,3] > 47) & (flow_data[:,1]==9))
print(flow_count)
tot_possible=np.sum((flow_data[:,1]==9))
print(tot_possible)
# Calculate the average flow for these same criteria 
flow_mean = np.mean(flow_data[(flow_data[:,3] > 47) & (flow_data[:,1]==9),3])


print("Flow meets this critera", flow_count, " times")
print('And has an average value of', flow_mean, "when this is true")

# %%
# Question number 4a
flow_count = np.sum((flow_data[:,0]<=2000) & (flow_data[:,3] > 47) & (flow_data[:,1]==9))
print(flow_count)
tot_possible=np.sum((flow_data[:,0]<=2000) & (flow_data[:,1]==9))
print(tot_possible)
# Calculate the average flow for these same criteria 
flow_mean = np.mean(flow_data[(flow_data[:,3] > 47) & (flow_data[:,1]==9),3])
print("Flow meets this critera", flow_count, " times")
print('And has an average value of', flow_mean, "when this is true")

# %%
# Question number 4b
flow_count = np.sum((flow_data[:,0]>=2010) & (flow_data[:,3] > 47) & (flow_data[:,1]==9))
print(flow_count)
tot_possible=np.sum((flow_data[:,0]>=2010) & (flow_data[:,1]==9))
print(tot_possible)
# Calculate the average flow for these same criteria 
flow_mean = np.mean(flow_data[(flow_data[:,3] > 47) & (flow_data[:,1]==9),3])
print("Flow meets this critera", flow_count, " times")
print('And has an average value of', flow_mean, "when this is true")

#%%
##KEEP KEEP KEEP
firsthalf_sept=flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==9) & \
    (flow_data[:,2]>=20)]
plt.hist(firsthalf_sept[:,3])

#%%
#Sharing a cell plots the histograms together
#First week of September
# From 2015 on
septwk1_fiveyr=flow_data[(flow_data[:,0]>=2015) & (flow_data[:,1]==9) & \
    (flow_data[:,2]<=7)]
plt.hist(septwk1_fiveyr[:,3])

flow_count = np.sum((flow_data[:,0]>=2015) & (flow_data[:,1]==9) &\
     (flow_data[:,2]<=7))
# Calculate the average flow for these same criteria 
flow_mean = np.mean(flow_data[(flow_data[:,0]>=2019) & \
    (flow_data[:,1]==9),3])
print("Flow meets this critera", flow_count, " times since 2015")
print('And has an average value of', flow_mean, "when this is true")

#%%
#September from 2019 on
septwk1_oneyr=flow_data[(flow_data[:,0]>=2019) & (flow_data[:,1]==9) & \
    (flow_data[:,2]<=7)]
plt.hist(septwk1_oneyr[:,3])

flow_count = np.sum((flow_data[:,0]>=2019) & (flow_data[:,1]==9) &\
     (flow_data[:,2]<=7))
# Calculate the average flow for these same criteria 
flow_mean = np.mean((flow_data[:,0]>=2019) & (flow_data[:,1]==9) & \
    (flow_data[:,2]<=7))
flow_mean = np.mean(flow_data[(flow_data[:,0]>=2019) & \
    (flow_data[:,1]==9),3])

#%%
#First half of September
# From 2015 on
septwk2_fiveyr=flow_data[(flow_data[:,0]>=2015) & (flow_data[:,1]==9) & \
    (flow_data[:,2]<=19)]
plt.hist(septwk2_fiveyr[:,3])

#From 2019 on
septwk2_oneyr=flow_data[(flow_data[:,0]>=2019) & (flow_data[:,1]==9) & \
    (flow_data[:,2]<=19)]
plt.hist(septwk2_oneyr[:,3])

#Why is the mean value wrong?
flow_mean = np.mean((flow_data[:,0]>=2019) & (flow_data[:,1]==9) & \
    (flow_data[:,2]<=15))
print('Flow has an average value of', flow_mean)

#%%
#Semester Forecast
#To August 21st from 2015 on
augwk1_fiveyr=flow_data[(flow_data[:,0]>=2015) & (flow_data[:,1]==8) & \
    (flow_data[:,2]<=21)]
plt.hist(augwk1_fiveyr[:,3])
#From 2019 on
augwk1_oneyr=flow_data[(flow_data[:,0]>=2019) & (flow_data[:,1]==8) & \
    (flow_data[:,2]<=21)]
plt.hist(augwk1_oneyr[:,3])
#%%
#Semester: Week 4
semwk4=flow_data[(flow_data[:,0]==2018) & (flow_data[:,1]==9) & \
    (flow_data[:,2]<=21)]
plt.hist(semwk4[:,3])
#From 2019 
semwk4_oneyr=flow_data[(flow_data[:,0]==2019) & (flow_data[:,1]==9) & \
    (flow_data[:,2]<=21)]
plt.hist(semwk4_oneyr[:,3])

#%%
#Semester: Week 5
semwk5=flow_data[(flow_data[:,0]==2018) & (flow_data[:,1]==9) & \
    (flow_data[:,2]<=30)]
plt.hist(semwk5[:,3])
#From 2019
semwk5_oneyr=flow_data[(flow_data[:,0]==2019) & (flow_data[:,1]==9) & \
    (flow_data[:,2]<=30)]
plt.hist(semwk5_oneyr[:,3])

#%%
#Semester: Week 15
sem=flow_data[(flow_data[:,0]==2018) & (flow_data[:,1]==12) & \
    (flow_data[:,2]<=15)]
plt.hist(sem[:,3])
#%%
#From 2019
sem_oneyr=flow_data[(flow_data[:,0]==2019) & (flow_data[:,1]==12) & \
    (flow_data[:,2]<=15)]
plt.hist(sem_oneyr[:,3])

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
=======
# Starter code for Homework 4

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week4.txt'
filepath = os.path.join('data', filename)
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

# Make a numpy array of this data
flow_data = data[['year', 'month','day', 'flow']].to_numpy()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%
# Question number 3
flow_count = np.sum((flow_data[:,3] > 47) & (flow_data[:,1]==9))
print(flow_count)
tot_possible=np.sum((flow_data[:,1]==9))
print(tot_possible)
# Calculate the average flow for these same criteria 
flow_mean = np.mean(flow_data[(flow_data[:,3] > 47) & (flow_data[:,1]==9),3])


print("Flow meets this critera", flow_count, " times")
print('And has an average value of', flow_mean, "when this is true")

# %%
# Question number 4a
flow_count = np.sum((flow_data[:,0]<=2000) & (flow_data[:,3] > 47) & (flow_data[:,1]==9))
print(flow_count)
tot_possible=np.sum((flow_data[:,0]<=2000) & (flow_data[:,1]==9))
print(tot_possible)
# Calculate the average flow for these same criteria 
flow_mean = np.mean(flow_data[(flow_data[:,3] > 47) & (flow_data[:,1]==9),3])
print("Flow meets this critera", flow_count, " times")
print('And has an average value of', flow_mean, "when this is true")

# %%
# Question number 4b
flow_count = np.sum((flow_data[:,0]>=2010) & (flow_data[:,3] > 47) & (flow_data[:,1]==9))
print(flow_count)
tot_possible=np.sum((flow_data[:,0]>=2010) & (flow_data[:,1]==9))
print(tot_possible)
# Calculate the average flow for these same criteria 
flow_mean = np.mean(flow_data[(flow_data[:,3] > 47) & (flow_data[:,1]==9),3])
print("Flow meets this critera", flow_count, " times")
print('And has an average value of', flow_mean, "when this is true")

#%%
##KEEP KEEP KEEP
firsthalf_sept=flow_data[(flow_data[:,0]>=2010) & (flow_data[:,1]==9) & \
    (flow_data[:,2]>=20)]
plt.hist(firsthalf_sept[:,3])

#%%
#Sharing a cell plots the histograms together
#First week of September
# From 2015 on
septwk1_fiveyr=flow_data[(flow_data[:,0]>=2015) & (flow_data[:,1]==9) & \
    (flow_data[:,2]<=7)]
plt.hist(septwk1_fiveyr[:,3])

flow_count = np.sum((flow_data[:,0]>=2015) & (flow_data[:,1]==9) &\
     (flow_data[:,2]<=7))
# Calculate the average flow for these same criteria 
flow_mean = np.mean(flow_data[(flow_data[:,0]>=2019) & \
    (flow_data[:,1]==9),3])
print("Flow meets this critera", flow_count, " times since 2015")
print('And has an average value of', flow_mean, "when this is true")

#%%
#September from 2019 on
septwk1_oneyr=flow_data[(flow_data[:,0]>=2019) & (flow_data[:,1]==9) & \
    (flow_data[:,2]<=7)]
plt.hist(septwk1_oneyr[:,3])

flow_count = np.sum((flow_data[:,0]>=2019) & (flow_data[:,1]==9) &\
     (flow_data[:,2]<=7))
# Calculate the average flow for these same criteria 
flow_mean = np.mean((flow_data[:,0]>=2019) & (flow_data[:,1]==9) & \
    (flow_data[:,2]<=7))
flow_mean = np.mean(flow_data[(flow_data[:,0]>=2019) & \
    (flow_data[:,1]==9),3])

#%%
#First half of September
# From 2015 on
septwk2_fiveyr=flow_data[(flow_data[:,0]>=2015) & (flow_data[:,1]==9) & \
    (flow_data[:,2]<=19)]
plt.hist(septwk2_fiveyr[:,3])

#From 2019 on
septwk2_oneyr=flow_data[(flow_data[:,0]>=2019) & (flow_data[:,1]==9) & \
    (flow_data[:,2]<=19)]
plt.hist(septwk2_oneyr[:,3])

#Why is the mean value wrong?
flow_mean = np.mean((flow_data[:,0]>=2019) & (flow_data[:,1]==9) & \
    (flow_data[:,2]<=15))
print('Flow has an average value of', flow_mean)

#%%
#Semester Forecast
#To August 21st from 2015 on
augwk1_fiveyr=flow_data[(flow_data[:,0]>=2015) & (flow_data[:,1]==8) & \
    (flow_data[:,2]<=21)]
plt.hist(augwk1_fiveyr[:,3])
#From 2019 on
augwk1_oneyr=flow_data[(flow_data[:,0]>=2019) & (flow_data[:,1]==8) & \
    (flow_data[:,2]<=21)]
plt.hist(augwk1_oneyr[:,3])
#%%
#Semester: Week 4
semwk4=flow_data[(flow_data[:,0]==2018) & (flow_data[:,1]==9) & \
    (flow_data[:,2]<=21)]
plt.hist(semwk4[:,3])
#From 2019 
semwk4_oneyr=flow_data[(flow_data[:,0]==2019) & (flow_data[:,1]==9) & \
    (flow_data[:,2]<=21)]
plt.hist(semwk4_oneyr[:,3])

#%%
#Semester: Week 5
semwk5=flow_data[(flow_data[:,0]==2018) & (flow_data[:,1]==9) & \
    (flow_data[:,2]<=30)]
plt.hist(semwk5[:,3])
#From 2019
semwk5_oneyr=flow_data[(flow_data[:,0]==2019) & (flow_data[:,1]==9) & \
    (flow_data[:,2]<=30)]
plt.hist(semwk5_oneyr[:,3])

#%%
#Semester: Week 15
sem=flow_data[(flow_data[:,0]==2018) & (flow_data[:,1]==12) & \
    (flow_data[:,2]<=15)]
plt.hist(sem[:,3])
#%%
#From 2019
sem_oneyr=flow_data[(flow_data[:,0]==2019) & (flow_data[:,1]==12) & \
    (flow_data[:,2]<=15)]
plt.hist(sem_oneyr[:,3])

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
>>>>>>> Stashed changes
