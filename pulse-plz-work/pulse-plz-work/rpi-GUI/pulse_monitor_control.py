#!/usr/bin/python

import numpy
from poll_sensor import *

sample_period = 30

data_raw = poll_for(sample_period)
print data_raw

# First entry in data is usually corrupted/incomplete
del data_raw[0]

# Clean raw data from Serial
data_th = 1000
# Remove outliers; data < threshold
x = data_raw[data_raw < data_th]

x_clean_file = open('x_clean_data.txt','w')
x_clean_file.write('\n'.join(x))


