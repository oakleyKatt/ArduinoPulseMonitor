#!/usr/bin/python

class pulse_data():

    def __init__(self, data_clean, data_filtered1, data_filtered2, data_final, bpm):
        self.data_clean = data_clean[:]
        self.data_filtered1 = data_filtered1[:]
        self.data_filtered2 = data_filtered2[:]
        self.data_final = data_final[:]
        self.bpm = bpm
