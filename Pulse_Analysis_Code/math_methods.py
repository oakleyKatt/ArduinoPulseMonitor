#!/usr/bin/python

import numpy as np

def smooth(x):
    n = len(x)
    ans = []
    ans.append(float(x[0]))
    ans.append(float((x[0]+x[1]+x[2])/3.0))
    for i in range(2,n-2):
        ans.append(float(np.sum(x[i-2:i+3])/5.0))
    ans.append(float((x[n-3]+x[n-2]+x[n-1])/3.0))
    ans.append(float(x[n-1]))
    return ans

def diff(x):
    n = len(x)
    ans = []
    for i in range(n-1):
        ans.append(x[i+1]-x[i])
    return ans

def findpeaks(x):
    n = len(x)
    ans = []
    for i in range(1,n-1):
        if x[i] > x[i-1] and x[i] > x[i+1]:
            ans.append(i)
    return ans

def bpm(peaks, sample_period):
    return (len(peaks)*60)/sample_period