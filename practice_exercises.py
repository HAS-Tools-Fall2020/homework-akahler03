# %%
precip_by_location=[46.23,'inches','New York City']
precip_by_location[0]=20.23
precip_by_location.insert(0,1)
# %%
precip_by_location[3]='Boulder'
precip_by_location.append('Colorado')
# %%
list_of_lists=[[1,2,3],[8,9,10]]
list_of_lists[0]
type(list_of_lists[0])
type(list_of_lists)
# %%
list_of_lists[1][1]
# %%
march_precip=1.85
in_to_mm=25.4
march_precip_mm=march_precip*in_to_mm

# %%
annual_avg_precip_nyc=42.65
dec_avg_precip_nyc=3.58
annual_avg_precip_nyc+=dec_avg_precip_nyc

# %%
#Modify operations to return True
relational=3<=2
relational=3>=2
identity=(4 is 3)
identity=(4 is not 3)
# %%
#Ch. 5 Exercises
#Create Lists from Data
boulder_precip_months=["jan","feb","mar","apr","may","june","july","aug","sept","oct","nov","dec"]
boulder_precip_inches=[.70,.75,1.85,2.93,3.05,2.02,1.93,1.62,1.84,1.31,1.39,.84]

# %%
inch_to_mm=25.4
boulder_precip_mm=boulder_precip_inches.copy()


# %%
len(boulder_precip_mm)

# %%
boulder_precip_mm=[i*inch_to_mm for i in boulder_precip_mm]

# %%
#Challenge 3: Create a List of Lists
all_boulder_data=[[boulder_precip_months],[boulder_precip_mm]]
#all_boulder_data=[boulder_precip_months,boulder_precip_mm]

# %%
#Challenge 4: Plot Data in List of Lists
import matplotlib.pyplot as plt 
# Plot monthly precipitation values
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(boulder_precip_months, 
       boulder_precip_mm, 
       color="aqua")
ax.set(title="Annual Boulder Precipitation",
       xlabel="Months", 
       ylabel="Precip (mm)")
plt.show()


# %%
#CH 17 Lesson 1, Conditionals
x=10
if x==10:
       print("x is equal to 10")
else:
       print("x has a value of",x,"which is not equal to 10")
# %%
#Check paths using conditional statements
# Import necessary packages
import os
import numpy as np
import earthpy as et
# Avg monthly precip (inches) of Boulder, CO for 1-d array
avg_month_precip_url = 'https://ndownloader.figshare.com/files/12565616'
et.data.get_data(url=avg_month_precip_url)
'/root/earth-analytics/data/earthpy-downloads/avg-monthly-precip.txt'
# %%
