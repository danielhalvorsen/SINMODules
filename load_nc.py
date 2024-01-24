import numpy as np
from netCDF4 import Dataset
import matplotlib as plt  # cian
import pandas as pd  # cian



def load_nc_file(filepath):
    filestruct = Dataset(filepath,'r')
    return filestruct
  








def read_poly():
    import geopandas as gpd
    shape = gpd.read_file(shp_file)
    return
