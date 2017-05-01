#!/usr/bin/python

import time, math, string
import RPi.GPIO as GPIO

#print("anything")
ltf_pin = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(ltf_pin, GPIO.IN)

f = open('pulseData.txt','w')
prog_start_time = time.time()
#print(prog_start_time+10000)

#c = 0
#while(c < 1000):
while(time.time() < prog_start_time+30):
    #print(time.time() - prog_start_time)
    n_cycles = 100
    pulses = 0
    start = time.time()
    while(time.time() < start+0.25):
        GPIO.wait_for_edge(ltf_pin, GPIO.FALLING)
        pulses += 1
#    for i in range(0,n_cycles):
#        GPIO.wait_for_edge(ltf_pin, GPIO.FALLING)

#    duration = time.time()-start
#    frequency = n_cycles / duration
    #print(frequency)
    #f.write(str(time.time() - prog_start_time))
    #f.write('\t')
    #f.write(str(duration))
    #f.write('\t')
    f.write(str(pulses) + '\n')
#    c += 1
f.close()
