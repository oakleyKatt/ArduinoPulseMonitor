#!/usr/bin/python

from pulse_data import *

class patient():

    def __init__(self, name):
        self.name = name

    # "File" as in directory
    def setDirectoryName(self,dir_name):
        self.dir_name = dir_name

    def setPulseData(self, data):
        pass
