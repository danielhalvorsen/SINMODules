import numpy as np
from netCDF4 import Dataset
import matplotlib as plt  # cian
import pandas as pd  # cian



def load_nc_file(filepath):
    filestruct = Dataset(filepath,'r')
    return filestruct
  




























def eva(bio):
    bio[np.where(bio=9.9692100e+36)]=np.nan
    return bio
