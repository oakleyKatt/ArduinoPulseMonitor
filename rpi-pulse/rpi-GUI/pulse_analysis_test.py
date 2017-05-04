#!/usr/bin/python

import numpy
from math_methods import *

## INIT
#data_raw = [line.rstrip('\n') for line in open('pulseData50.txt')]
data_raw = [line.rstrip('\n') for line in open('pulseData50.txt')]
#print data_raw
#print "data_raw[45:70]"
#print data_raw[45:70]
#print data_raw

# First entry in data is usually corrupted/incomplete
del data_raw[0]
#print "data_raw"
#print data_raw
#print "data_raw[45:70]"
#print data_raw[45:70]

## Clean raw data from Serial

# Clear any NaN values
#x = x[~numpy.isnan(x)]

## NO NaN VALUES PRESENT (PRESUMEDLY) -- IMPLEMENT LATER IF ISSUE ARRISES
#data_raw = data_raw[data_raw != 'NaN']
#data_raw.remove('NaN')
#num_nan = data_raw.count('NaN')
#print num_nan
#while num_nan > 1:
#    data_raw.remove('Nan')
#    num_nan -= 1
#print data_raw

# data_raw is list {strings}
#print int(data_raw[0])+int(data_raw[1])
# vvv this seemed to work on the RPi ZERO- so don't delete till tested
#x = map(int, data_raw)
#x = map(int, data_raw)
#print x
# vvv for now cast data_raw --> int() this way
x = []
for i in range(len(data_raw)):
    x.append(float(data_raw[i]))
#print "x: "
#print x
#print "x[45:70]"
#print x[45:70]
# Remove outliers; data < threshold
data_th = 1000.0
# vvv supposed to work - doesn't in pycharm
#x = x[x < data_th]
#data = data_raw[data_raw < data_th]
# vvv do it this way for now
x_clean = []
for i in range(len(x)):
    if x[i] > data_th:
        x_clean.append(x[i])
#print "x_clean: "
#print x_clean
#print "x_clean[45:70]"
#print x_clean[45:70]

### CONFIRMED WORKS TO HERE ###

##### WHOLE SIGNAL ANALYSIS WORKS FOR [pulseData50.txt] #####

# seconds
sample_period = 30
## end INIT

## Signal Analysis

# Signal Conditioning
smx0 = smooth(x_clean)
smx0_file = open('smx0_data.txt','w')
for i in range(len(smx0)):
    smx0_file.write(str(smx0[i]) + '\n')
smx1 = smooth(smx0)
smx1_file = open('smx1_data.txt','w')
for i in range(len(smx1)):
    smx1_file.write(str(smx1[i]) + '\n')

#print x
xd = diff(x_clean)
xd_file = open('xd_data.txt','w')
for i in range(len(xd)):
    xd_file.write(str(xd[i]) + '\n')
fx = smooth(xd)


xd0 = diff(smx0)
xd0_file = open('xd0_data.txt','w')
for i in range(len(xd0)):
    xd0_file.write(str(xd0[i]) + '\n')
fx0 = smooth(xd0)

xd1 = diff(smx1)
xd1_file = open('xd1_data.txt','w')
for i in range(len(xd1)):
    xd1_file.write(str(xd1[i]) + '\n')
fx1 = smooth(xd1)

fx_file = open('fx_data.txt','w')
for i in range(len(fx)):
    fx_file.write(str(fx[i]) + '\n')
#fx_file.write('\n'.join(str(fx)))
fx0_file = open('fx0_data.txt','w')
for i in range(len(fx0)):
    fx0_file.write(str(fx0[i]) + '\n')
#fx0_file.write('\n'.join(str(fx0)))
fx1_file = open('fx1_data.txt','w')
for i in range(len(fx1)):
    fx1_file.write(str(fx1[i]) + '\n')
#fx1_file.write('\n'.join(str(fx1)))


# Find peaks
peaks = findpeaks(fx1)
peaks_file = open('peaks_data.txt','w')
for i in range(len(peaks)):
    peaks_file.write(str(peaks[i]) + '\n')
sample_period = 60
print bpm(peaks, sample_period)