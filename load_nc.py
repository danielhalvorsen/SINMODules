import numpy as np
import netCDF4 #Eva


#Load data function

def load_nc (path):
    return netCDF4.Dataset(path)
