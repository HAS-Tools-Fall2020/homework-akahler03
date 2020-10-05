# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 16:19:28 2020

@author: Dell Latitude E6430
"""
#%%
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-whitegrid')

#%%
#SIMPLE LINE PLOTS
fig = plt.figure()
ax = plt.axes()
x=np.linspace(0,10,1000)
ax.plot(x,np.sin(x));

#%%
#OR let figure and axes be created in background
plt.plot(x,np.sin(x));

#%%
#Single figure, multiple lines
plt.plot(x,np.sin(x))
plt.plot(x,np.cos(x));

#%%
#Link to simple line plots bookmarked in browser
#next: SCATTER PLOTS
#%%
x = np.linspace(0, 10, 30)
y = np.sin(x)

#The third argument is the type of symbol
plt.plot(x, y, 'o', color='black');

#%%
#Examples of markers
rng = np.random.RandomState(0)
for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
    plt.plot(rng.rand(5), rng.rand(5), marker,
             label="marker='{0}'".format(marker))
plt.legend(numpoints=1)
plt.xlim(0, 1.8);

#%%
#Combination
plt.plot(x, y, '-ok');

#%%
plt.plot(x, y, '-p', color='gray',
         markersize=15, linewidth=4,
         markerfacecolor='white',
         markeredgecolor='gray',
         markeredgewidth=2)
plt.ylim(-1.2, 1.2);

#%%
#BASIC ERROR BARS
x=np.linspace(0,10,50)
dy=.8
y=np.sin(x)+dy*np.random.randn(50)

plt.errorbar(x,y,yerr=dy, fmt='.k')

#%%
#ERRORBARS LIGHTER THAN POINTS
plt.errorbar(x, y, yerr=dy, fmt='o', color='black',
             ecolor='lightgray', elinewidth=3, capsize=0)
#%%
#CONTINUOUS ERRORS

from sklearn.gaussian_process import GaussianProcess

# define the model and draw some data
model = lambda x: x * np.sin(x)
xdata = np.array([1, 3, 5, 6, 8])
ydata = model(xdata)

# Compute the Gaussian process fit
gp = GaussianProcess(corr='cubic', theta0=1e-2, thetaL=1e-4, thetaU=1E-1,
                     random_start=100)
gp.fit(xdata[:, np.newaxis], ydata)

xfit = np.linspace(0, 10, 1000)
yfit, MSE = gp.predict(xfit[:, np.newaxis], eval_MSE=True)
dyfit = 2 * np.sqrt(MSE)  # 2*sigma ~ 95% confidence region