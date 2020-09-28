#!/usr/bin/env python
# coding: utf-8

# In[66]:


# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv


# In[67]:


# Set the file name and path to where you have stored the data
filename = 'streamflow_week5.txt'
filepath = os.path.join('Documents\Has_Tools_git\homework-akahler03\data', filename)
print(os.getcwd())
print(filepath)


# In[68]:


#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)


# Hints - you will need the functions: describe, info, groupby, sort, head and tail.
# 

# In[69]:


last_jul=data[(data['year']==2019) & (data['month']==7)]
this_jul=data[(data['year']==2020) & (data['month']==7)]


# In[70]:


plt.plot(this_jul['day'], this_jul['flow'])
plt.xlabel('Days')
plt.ylabel('Flow (cfs)')
plt.title('Jul. 2020')
plt.show()

plt.plot(last_jul['day'], last_jul['flow'])
plt.plot(this_jul['day'], this_jul['flow'])
plt.xlabel('Days')
plt.ylabel('Flow (cfs)')
plt.title('July 2019, 2020(orange)')
plt.show()


# In[71]:


last_aug=data[(data['year']==2019) & (data['month']==8)]
this_aug=data[(data['year']==2020) & (data['month']==8)]


# In[72]:


plt.plot(this_aug['day'], this_aug['flow'])
plt.xlabel('Days')
plt.ylabel('Flow (cfs)')
plt.title('Aug. 2020')
plt.show()

plt.plot(last_aug['day'], last_aug['flow'])
plt.plot(this_aug['day'], this_aug['flow'])
#labelstr=2019
plt.xlabel('Days')
plt.ylabel('Flow (cfs)')
plt.title('August 2019(blue), 2020(orange)')
#plt.legend()
plt.show()


# In[ ]:





# In[73]:


last_sept=data[(data['year']==2019) & (data['month']==9)]
this_sept=data[(data['year']==2020) & (data['month']==9)]


# In[74]:


plt.plot(this_sept['day'], this_sept['flow'])
plt.xlabel('Days')
plt.ylabel('Flow (cfs)')
plt.title('September 2020')
plt.show()

plt.plot(last_sept['day'], last_sept['flow'])
plt.plot(this_sept['day'], this_sept['flow'])
labelstr=2019
plt.xlabel('Days')
plt.ylabel('Flow (cfs)')
plt.title('September 2019, 2020(orange)')
plt.legend()
plt.show()

#plt.xlabel('Days')
#plt.ylabel('Flow (cfs)')
#plt.title('September 2020')
#plt.show()


# Plotting weekly comparisons for Sept 2019 and 2020

# In[75]:


first_week19=data[(data['year']==2019) & (data['month']==9) & (data['day']<=7)]
first_week20=data[(data['year']==2020) & (data['month']==9) & (data['day']<=7)]


# In[76]:


plt.plot(first_week19['day'], first_week19['flow'])
plt.xlabel('Days')
plt.ylabel('Flow (cfs)')
plt.title('first week 2019')
plt.show()

plt.plot(first_week19['day'], first_week19['flow'])
plt.plot(first_week20['day'], first_week20['flow'])
plt.xlabel('Days')
plt.ylabel('Flow (cfs)')
plt.title('first week 2019, 2020 (orange)')
plt.show()


# In[77]:


second_week19=data[(data['year']==2019) & (data['month']==9) & (data['day']>7) & (data['day']<=14)]
second_week20=data[(data['year']==2020) & (data['month']==9) & (data['day']>7) & (data['day']<=14)]


# In[78]:


plt.plot(second_week19['day'], second_week19['flow'])
plt.xlabel('Days')
plt.ylabel('Flow (cfs)')
plt.title('second week 2019')
plt.show()

plt.plot(second_week19['day'], second_week19['flow'])
plt.plot(second_week20['day'], second_week20['flow'])
plt.xlabel('Days')
plt.ylabel('Flow (cfs)')
plt.title('second week 2019, 2020 (orange)')
plt.show()


# In[79]:


third_week19=data[(data['year']==2019) & (data['month']==9) & (data['day']>14) & (data['day']<=21)]
third_week20=data[(data['year']==2020) & (data['month']==9) & (data['day']>14) & (data['day']<=21)]


# In[80]:


plt.plot(third_week19['day'], third_week19['flow'])
plt.xlabel('Days')
plt.ylabel('Flow (cfs)')
plt.title('third week 2019')
plt.show()

plt.plot(third_week19['day'],third_week19['flow'])
plt.plot(third_week20['day'], third_week20['flow'])
plt.xlabel('Days')
plt.ylabel('Flow (cfs)')
plt.title('third week 2019, 2020 (orange)')
plt.show()


# In[81]:


fourth_week19=data[(data['year']==2019) & (data['month']==9) & (data['day']>21) & (data['day']<=26)]
fourth_week20=data[(data['year']==2020) & (data['month']==9) & (data['day']>21) & (data['day']<=26)]


# In[82]:


plt.plot(fourth_week19['day'], fourth_week19['flow'])
plt.xlabel('Days')
plt.ylabel('Flow (cfs)')
plt.title('fourth week 2019')
plt.show()

plt.plot(fourth_week19['day'],fourth_week19['flow'])
plt.plot(fourth_week20['day'], fourth_week20['flow'])
plt.xlabel('Days')
plt.ylabel('Flow (cfs)')
plt.title('fourth week 2019, 2020 (orange)')
plt.show()


# In[83]:


fifth_sept19=data[(data['year']==2019) & (data['month']==9) & (data['day']>21) & (data['day']<=30)]
first_oct19=data[(data['year']==2019) & (data['month']==10) & (data['day']<=7)]


# In[84]:


plt.plot(fifth_sept19['day'],fifth_sept19['flow'])


# In[85]:


plt.plot(first_oct19['day'],first_oct19['flow'])


# last_ytd=data[(data['year']==2019)]
# this_ytd=data[(data['year']==2020)]

# plt.plot(last_ytd['day'], last_ytd['flow'])
# plt.xlabel('Days')
# plt.ylabel('Flow (cfs)')
# plt.title('last_ytd')
# plt.show()
# 
# plt.plot(last_ytd['day'],last_ytd['flow'])
# plt.plot(this_ytd['day'], this_ytd['flow'])
# plt.xlabel('Days')
# plt.ylabel('Flow (cfs)')
# plt.title('this_ytd 2019, 2020 (orange)')
# plt.show()
# 
# print('Holy wow. Will fix later.')

# In[86]:


#Question 2: Summary of Flow min, max, mean, quartiles
data['flow'].describe()


# Question 2: Summary of flow by month

# In[87]:


#For only one month
#jan_flow=data[data['month']==1]

#To do all the months, by monthly flow
data.sort_values(by=['year','month'], inplace=True)


# In[88]:


test1=data[data.month==1].describe()  


# In[90]:


test1


# In[91]:


all_months=data.month.unique().tolist()


# Question 3

# In[92]:


#Question 3
for i in all_months:
    temp=data[data.month==i]
    print(i,temp.flow.describe())


# Question 4 Provide a table with the 5 highest and 5 lowest flow values for the period of record. Include the date,
# month and flow values in your summary

# In[102]:


data.sort_values(by=['flow'], inplace=True)


# In[103]:


#test_md=data.sort_values(by=['flow'], inplace=True)
#print(test_md.to_markdown())


# In[105]:


data.head()


# In[32]:


data.tail()


# In[33]:


#Another way

#first_five=data[:][0:5]
#last_five=data[:][-6:-1]
#highs_lows=pd.concat([first_five,last_five])


# In[34]:


#highs_lows


# Question 5 Find the highest and lowest flow values for every month of the year 
# (i.e. you will find 12 maxes and 12 mins) and report back what year these occurred in

# In[35]:



print(data.groupby('month')['flow'].nsmallest(1))
#for n in nfive:
  #  print(nfive.loc[i])
#for n in nfive.index:
   # print(nfive['year'].loc[n])
print(data.loc[5,'year'])
print(data.loc[783,'year'])
print(data.loc[83,'year'])
print(data.loc[10710,'year'])
print(data.loc[5620,'year'])
print(data.loc[8581,'year'])
print(data.loc[8582,'year'])
print(data.loc[11,'year'])
print(data.loc[11574,'year'])
print(data.loc[8677,'year'])
print(data.loc[10167,'year'])
print(data.loc[8735,'year'])


# In[36]:


print(data.groupby('month')['flow'].nlargest(1))
print(data.loc[1468,'year'])
print(data.loc[1511,'year'])
print(data.loc[2255,'year'])
print(data.loc[821,'year'])
print(data.loc[1246,'year'])
print(data.loc[1247,'year'])
print(data.loc[6420,'year'])
print(data.loc[1330,'year'])
print(data.loc[5742,'year'])
print(data.loc[7949,'year'])
print(data.loc[5805,'year'])
print(data.loc[5842,'year'])


# 54.31  Question 6: Provide a list of historical dates with flows that are within 10% of your week 1 forecast value. 
# If there are none than increase the %10 window until you have at leastone other value and report the date 
# and the new window you used

# In[65]:


data[(data['flow']>=54.31*.9) & (data['flow']<=54.31+54.31*.1)]


# EVERYTHING BELOW IS JUST TRYING THINGS OUT
# OR NOTES TO SAVE FOR LATER

# In[ ]:





# In[ ]:





# In[37]:


type(temp.flow.describe())


# In[38]:


#data[data.flow==maxi]


# In[42]:


#Create empty dataframe to store results of next cell maybe
#q5_mm=pd.DataFrame()


# In[43]:


#Try later

#all_months=data.month.unique().tolist()
#for i in all_months:
 #   temp=data[data.month==i]       #kind of like np.where
  #  mini=temp.flow.describe()[3]
   # maxi=temp.flow.describe()[7]
    #another1=temp[temp.flow==mini]
    #another2=temp[temp.flow==maxi]
    #frames=[another1,another2]
    #result=pd.concat(frames)
    #print(result)
    


# In[ ]:


#This will affect everything below

#dataframe.set_index("column")
#dataframe.loc[[value]]
#data.set_index("year")
#data.loc[[2019]]


# 
# 
# 
# data = data.set_index(['year'])
# print(data.loc['2019'])

# In[48]:


data.values


# In[49]:


#show the first four rows and three columns
data.iloc[:3,:2]


# In[50]:


#data.loc[data.density > 100, ['pop', 'density']]
data.loc[data.year>2018,['flow','year']]


# In[ ]:


#KEEP
#setting combined conditions

data.loc[(data['year'] >= 2018) & (data['month'] == 9)]


# In[52]:


data.loc[data['month']==(9)]


# In[53]:


year_2019=data.groupby(["month"])[["flow"]].min()


# In[54]:


year_2019


# In[57]:


data.sort_values(by='flow', ascending=True)

