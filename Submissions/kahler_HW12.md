# Abigail Kahler
## Week 12 Written Assignment

### Forecast summary
This week I incorporated elements of the previous week's group forecast\
such as reading the streamflow data in log form. I am still amending\
the AR model forecast with various fudge factors to bring it down to\
more reasonable values. I didn't want to borrow my group's 16 week forecast\
because it is beyond my current skill and I want to solidify foundations.\
My 16 week forecast values are looped from a single starting value. I am\
having trouble indexing to identify a new starting flow value for each month.

### New dataset

* I chose NCEP reanalysis historical data for daily averaged air\
temperature because this source seemed more intuitive. I think precip\
would be more relevant to the model but wanted to explore other types\
than what we covered in class.\
* I used the suggested spatial bounds, 34N to 36N and 247E to 249E, and\
chose a temporal resolution corresponding to what I've found most useful\
with streamflow data: January 2019 through our current Saturday cutoff.

### Approach to extracting and aggregating it into something useful
This part gave me some trouble. I used what we covered in class and\
training materials to look at the metadata and orient myself with its\
structure. I wanted to separate the data into date ranges and feed it\
into a model, like we've done with streamflow, but ended up cheating\
by using large .head() and .tail() values to\
separate the years, but I don't think that's a useful form.
* After
exploring this, I converted it to a dataframe and practiced doing the\
same operations in that form. I think this difficulty is from my\
understanding of the 3D structure.

* I experimented with plot manipulations but my slicing was incorrect for\
a line plot. These are the same as the template provided, with the addition\
of background color and plotting the two years together as subplots.

* This was a satisfying week with the borrowed computer. I uninstalled and\
reinstalled all these programs on my laptop, to no avail, and will hopefully\
do a factory reset next weekend.

![](plot_week12.jpg)
