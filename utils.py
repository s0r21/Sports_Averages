# Directory & File Name Function
def create_directory(directory_name, file_name):
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, directory_name)
    filename = os.path.join(path, file_name)
    if not os.path.exists(path):
        os.mkdir(path)
    return(filename)

# Loading the packages in the project
import pandas as pd
import numpy as np
import openpyxl
import time
from datetime import date
import os
t = 3 # this is for the time delay for rate limiter. Basically, stating that it's going to wait 3 seconds
    # seconds before running the next line
# import matplotlib
# import pmdarima.arima as arma
