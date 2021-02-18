# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 15:12:45 2021

@author: A
"""
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib
import gdal
import os
import rasterio


#importing an shape file and plotting it
"""x = gpd.read_file(r'C:/Users/A/Documents/GitHub/3D-House-Project/files/DHMVII_vdc_k01.shp')
x.plot(color ='black')"""

# Geotif metadeta :
raster = gdal.Open('tiffile.tif')
y = raster.GetGeoTransform()
proj = raster.GetProjection()

# 
z = rasterio.open('tiffile.tif')
z.bound
