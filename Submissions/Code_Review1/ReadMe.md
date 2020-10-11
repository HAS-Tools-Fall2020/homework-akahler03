# Abigail Kahler
# Week 7 Instructions for running forecast
\
I have included directional comments in each cell to explain its purpose and\
to instruct if it requires input. My new function starts in cell 48 and is\
utilized in the next cell. I would like to improve this section with a for loop\
but was having difficulty with setup. \
\
The flow comparison is followed by two line graphs that I use to help inform\
how I will shift my AR model forecast to be more realistic. I have chosen to\
focus my calculations on recent years and only Septembers and Octobers.\
\
**REAL Week One Forecast (cell 140):**

 67.81

**REAL Week Two Forecast (cell 143):**

 69.34

**Autoregressive model week one forecast (cell 128):**

 101.49

**Autoregressive model week two forecast (cell 134):**

 133
# Written Review: Questions to consider
\
**Is the script easy to read and understand?**

The script is easy to read. It follows a logical flow and clearly follows
the step from the previous cell. I found one typo that is small. In the print statement for the official week 2 forecast value it prints "Week one official forecast" and just needs to be changed to week two.

**Are variables and functions named descriptively when useful?**

 The variables and functions are named descriptively. One thought I had for last_sept and this_sept was to be even more specific and include actual year i.e. sept_2019 and sept_2020. This may fall out of PEP8 convention but would be more explicit in expressing the years being looked at. However, these names would have to change if the code was used in the future and you wanted to continue using this script.

**Are the comments helpful?**

 The comments are helpful and give clear, concise explanations for what is being done in the code.

**Can you run the script on your own easily?**

The script ran relatively easily. I had to change the os.path.join slightly. I am thinking this may be due to the OS and PC differences in syntax but am unsure. Other than this I was able to run the script without any issues.  

**Are the doc-strings useful?**

 the doc-string communicated what the function is doing and also stated the purpose of what it is made for.

**Does the code follow PEP8 style consistently?**

 The code follows PEP8 style. No errors were reported with the linter I have on in the background. All of the variables followed snake case throughout and followed appropriate convention style.

**If not are there specific instances where the script diverges from this style?**

As stated above, the style was consistent and did not diverge from the PEP8 style guidelines.  

**Is the code written succinctly and efficiently?**

 Yes.

**Are there superfluous code sections?**

There are no superfluous code sections. Everything in this code had a purpose and was  efficiently executed.  

**Is the use of functions appropriate?**\

The function included is appropriate, and intelligently returns a percentage  that helps the person running the script insight to how flow predictions can be adjusted to be more accurate.  

**Is the code written elegantly without decreasing readability?**\

Being a part of the class, it is written clear and in a way that is concise for the person running the code. I feel like there has to be some amount of insight with when running a code like this. the read.me doc may be the thing that would change if this were to be used by someone who is outside of this class and unfamiliar with the streamflow data we are using. Please feel free to reach out directly if you have any questions about my comments here. 

![](assets/ReadMe-ff0ecab3.png)\
\
**Readability:**\
3

**Style:**\
3

**Code Awesome:**\
3
