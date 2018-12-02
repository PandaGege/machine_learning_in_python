# coding:utf8


import pandas as pd
import numpy as np


rocksVmines = pd.read_csv('./sonar.all-data', header=None, prefix="V")

dataRow2 = rocksVmines.iloc[0:208,1]
dataRow3 = rocksVmines.iloc[0:208,2]


print dataRow2
