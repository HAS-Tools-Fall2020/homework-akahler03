# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 14:48:24 2020

@author: Dell Latitude E6430
"""

import os
import matplotlib.pyplot as plt
import geopandas as gpd
import earthpy as et

# %%
# Get data and set working directory
data = et.data.get_data('spatial-vector-lidar')
os.chdir(os.path.join(et.io.HOME, 'earth-analytics'))
Downloading from https://ndownloader.figshare.com/files/12459464
Extracted output to /root/earth-analytics/data/spatial-vector-lidar/.