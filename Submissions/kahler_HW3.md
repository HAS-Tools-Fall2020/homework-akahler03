Abigail Kahler
Homework 3 Written Assignment
Due 09/14/2020

The variables flow, year, month, and day are all lists with length 11576.
Flow is composed of floats because of the decimals values, while year, month, and day are integers.

The historical September daily flow was greater than each weekly prediction an average of 170 times from 1989 to 2020.
My predictions are under historical values 73% of the time.

Before the year 2000, there are 138 occurrences above my prediction, showing them to be under 89% of the time.
After 2010, the historical values are over my predictions 52 times, equivalent to 42% of the time. 
The decrease in under predicting should represent a drying trend in the past ten years, however, my number of total overage occurrences does not seem right with the
total possibilities within that time range. I will need to explore and check this by creating a better code that is not just manual math. Then I would like to plot my predictions
against historical averages per the conditions above to visualize the results.

Daily flow typically decreases in the second half of September as monsoon flows end.

FORECAST METHODS SUMMARY
I narrowed the focus of my data to be within the last four years for drought trend and looked at the flow data manually week by week. Doing it manually is not really coding but I spent the bulk of my time and brain power exploring for loops vs. list comprehension. In the end, I went with lists but once I got the code below to
work I wasn't sure where to go next without trying to use for loops on top of this code. I took the mean of weekly data and multiplied it by an arbitrary .86 as a nod to the low values this year. This forecast is unrefined and not
based on good methods. Next week, depending on the techniques we are learning, I will add in automation and also set it to evaluate more criteria.

FORECAST CODE
#week1=[flow[i] for i in range(len(year)) if year[i]>2015 and month[i]==9 \
 #       and 13<=day[i]<=19]
#FOR LIST OF THE INDECES YOU NEED (unbracketed i = index value):
index_of_days=[i for i in range(len(year)) if year[i]>2015 and month[i]==9 \
        and 13<=day[i]<=19]
#TO PULL VALUES CORRESPONDING TO THE INDEX CREATED ABOVE (use brackets with i):
list_years=[year[i] for i in index_of_days]
print(list_years)
week1_flow=[flow[i] for i in index_of_days]
print(week1_flow)
week1_mean=np.mean(week1_flow)
fore1=week1_mean*.86
print(fore1)

#%%
flow_greater=[flow[i] for i in range(len(year)) if flow[i]>89.3678 and month
[i]==9]
print(len(flow_greater))

#%% THIS MATH IS ONLY THE THOUGHT FRAMEWORK FOR FUTURE LOOP OR LIST STATEMENT
week1=[flow[i] for i in range(len(year)) if flow[i]>46 and month[i]==9]
length_days1=(len(week1))
length1=(length_days1/4)
print(length1)
week2=[flow[i] for i in range(len(year)) if flow[i]>39 and month[i]==9]
length_days2=(len(week2))
length2=(length_days2/4)
print(length2)
week3=[flow[i] for i in range(len(year)) if flow[i]>78 and month[i]==9]
length_days3=(len(week3))
length3=(length_days3/4)
print(length3)
week4=[flow[i] for i in range(len(year)) if flow[i]>85 and month[i]==9]
length_days4=(len(week4))
length4=(length_days/4)
print(length4)
