#!/usr/bin/python

from math_methods import *
from pulse_data import *

def pulse_analysis(data_raw, sample_period):

    del data_raw[0]

    x = []
    for i in range(len(data_raw)):
        x.append(float(data_raw[i]))

    data_th = 1000.0

    x_clean = []
    for i in range(len(x)):
        if x[i] > data_th:
            x_clean.append(x[i])

    smx0 = smooth(x_clean)
    smx1 = smooth(smx0)

    xd = diff(x_clean)
    fx = smooth(xd)

    xd0 = diff(smx0)
    fx0 = smooth(xd0)

    xd1 = diff(smx1)
    fx1 = smooth(xd1)

    bpm_val = bpm(findpeaks(fx1), sample_period)

    data = pulse_data(x_clean, fx, fx0, fx1, bpm_val, sample_period)
    #return fx1
    return data
