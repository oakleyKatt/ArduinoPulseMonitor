#!/usr/bin/python

import numpy

class pulse_data():

    def __init__(self, data_clean, data_filtered1, data_filtered2, data_final, bpm, sample_period):
        self.data_clean = data_clean[:]
        self.data_filtered1 = data_filtered1[:]
        self.data_filtered2 = data_filtered2[:]
        self.data_final = data_final[:]
        self.bpm = bpm
        self.sample_period = sample_period
        self.set_axis()

    def set_axis(self):
        # Set plot zoom in axis
        n = len(self.data_final)
        buff = int(round(n/5))
        self.s_idx = numpy.linspace(0, n-buff, 5)
        self.e_idx = numpy.linspace(buff, n, 5)
                                                
