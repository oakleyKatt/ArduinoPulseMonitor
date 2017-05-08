#!/usr/bin/python
import time

def poll_for(sample_period, patient_name):

    time.sleep(sample_period)
    data_raw = [line.rstrip('\n') for line in open('pulseData50.txt')]

    return data_raw
