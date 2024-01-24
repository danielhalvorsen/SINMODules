import numpy as np
from netCDF4 import Dataset

def load_nc_file(filepath):
    filestruct = Dataset(filepath,'r')
    return filestruct