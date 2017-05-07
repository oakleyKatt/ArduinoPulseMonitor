#!/usr/bin/python

from poll_sensor_norm import *

user_input = raw_input("start")

while(int(user_input)):
    ans = poll_for(1)
    user_input = raw_input("go?")
