# %%
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import geopandas as gpd
import fiona
from shapely.geometry import Point
import contextily as ctx

# %%
#  Gauges II USGS stream gauge dataset website:
# https://water.usgs.gov/GIS/metadata/usgswrd/XML/
# gagesII_Sept2011.xml#stdorder

# Reading in Gages II with geopandas
file = os.path.join('..\data', 'gagesII_9322_sept30_2011.shp')
gages = gpd.read_file(file)

# %%
# USA Rivers and Streams dataset website:
# https://hub.arcgis.com/datasets/esri::usa-rivers-and-streams/
# data?geometry=-126.415%2C30.380%2C-96.906%2C36.781&page=3

# Reading in USA Rivers and Streams with geopandas
file = os.path.join('..\data', '9ae73184-d43c-4ab8-940a-'\
    'c8687f61952f2020328-1-r9gw71.0odx9.shp')
usarivers = gpd.read_file(file)

# %% 
# Select AZ streamgages, rivers, and the Verde River
gages_AZ=gages[gages['STATE']=='AZ']
azrivers = usarivers[usarivers['State']=='AZ']
verde = azrivers.loc[azrivers.Name=='Verde River']

# Reproject all layers to match gages crs
reproject_verde = verde.to_crs(gages.crs)
reproject_azrivers = azrivers.to_crs(gages.crs)

# %%
# Map featuring the Verde River within the context of AZ rivers and gages
fig, ax =plt.subplots(figsize=(6,8))
reproject_verde.plot(ax=ax, color = 'b', zorder = 3, label = 'Verde River')
gages_AZ.plot(markersize=20, c = 'g', zorder = 2,
              ax=ax, label = 'AZ streamgages')
reproject_azrivers.plot(ax=ax, color = 'gray', zorder = 1, label = 'AZ rivers')
ax.legend()
plt.show()

# %%
