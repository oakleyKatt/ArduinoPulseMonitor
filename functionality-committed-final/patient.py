#!/usr/bin/python

from pulse_data import *

class patient():

    def __init__(self, name):
        self.name = name

    # "File" as in directory
    def setDirectoryName(self,dir_name):
        self.dir_name = dir_name

    def setName(self, name):
        self.name = name

    def setPulseData(self, data):
        self.my_pulse_data = pulse_data(data.data_clean, data.data_filtered1, data.data_filtered2, data.data_final, data.bpm, data.sample_period)
