 EXERCISE 1: 
#1a.  Create a 3X3 matrix with values ranging from 2-10  


#1.b  Make a matrix with all of the even values from 2-32


# 1.c Make a matrix with all of the even values from 2-32
# But this time have the values arrange along columns rather than rows

# BONUS:
# Create the same 3x3 matrix with value ranging from 2-10 as you did 
# in part a but this time do so by combining one 3X1 matrix and one 1X3 matrix
#%%
import numpy as np
one_a = np.array([(2,3,4),(5,6,7),(8,9,10)])
#%%
QUESTIONS 1 a

# %%
print(np.array(range(2,11,1).reshape(3,3))

# %%
Ex_1= np.array([(2,3,4),(5,6,7),(8,9,10)])
print(Ex_1)
#%%
x=np.arange(2,11).reshape(3,3)
# %%
#QUESTION 1b
x=np.reshape(np.arange(2,33,2),(4,4))
print(x)
# %%
Ex_2= np.array(2,34,2)
print (Ex_2)

#%%
#1. Get the largest integer that is less than or equal to the division
# of the inputs x1 and x2 where x1 is all the integers from 1-10 and x2=1.3
x1=np.array(range(1,11))
print(x1)
x2=1.3
x3=x1//x2
print(x3)
print(max(x3))


#%%
# 2. given an array x1=[0, 4, 37,17] and a second array with the values
# x2=[1.2, 3, 4.6, 7] return x1/x2 rounded to two decimal places

#%%
# 3. Create a 10 by 100 matrix with 1000 random numbers and report the 
# average and standard deviation across the entire matrix and 
# for each of the 10 rows. Round your answer to  two decimal places




# %%
