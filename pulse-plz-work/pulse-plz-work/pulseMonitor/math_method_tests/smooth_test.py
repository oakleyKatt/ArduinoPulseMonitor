#!/usr/bin/python

from math_methods import *

x_raw = [line.rstrip('\n') for line in open('smooth_x.txt')]
print x_raw
print len(x_raw)

x = map(int, x_raw)
print x
print len(x)

# Test smooth() function - WORKS
#smx = smooth(x)
#print smx

# Test diff() function - WORKS
dx = diff(x)
print dx
