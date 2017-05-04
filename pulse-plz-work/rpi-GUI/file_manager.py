#!/usr/bin/python

import os
from pulse_data import *
from patient import *

# Handles writing, loading, renaming, editing, etc. patient data files
class file_manager():

    def __init__(self):                                 # TO BE IMPLEMENTED
        # Populate with data files from Patient Data directory
        # list of filenames (for easy searching)
        self.id = 1
        self.dir_path = os.getcwd() + "/Patient_Files"
        # Load Patient Directory Paths
        self.patient_dir_path = [x[0] for x in os.walk(self.dir_path)]
        # First path is current working directory - not a Patient Directory
        # Separate Patient Directory Names from their paths
        self.patient_dir_names = []
        for i in range(1,len(self.patient_dir_path)):
            self.patient_dir_names.append(os.path.basename(os.path.normpath(self.patient_dir_path[i])))
        print self.patient_dir_names
        

    def new_patient(self, patient):
        pass

    def load_patient(self, name):
        pass

    # Update File Manager's Patient Directory path and name lists
    def update_dir(self):
        # Load Patient Directory Paths
        self.patient_dir_path = [x[0] for x in os.walk(self.dir_path)]
        # First path is current working directory - not a Patient Directory
        # Separate Patient Directory Names from their paths
        self.patient_dir_names = []
        for i in range(1,len(self.patient_dir_path)):
            self.patient_dir_names.append(os.path.basename(os.path.normpath(self.patient_dir_path[i])))
        print self.patient_dir_names

    # name @param shoudl be formatted before passed
    def save_all_data(self, name, this_pulse_data):
        # Check if name exists in database
        if self.check_name(name) == 1:
            print "Directory name not taken"
            # Create directory for new Patient
            os.makedirs(os.getcwd() + "/Patient_Files/" + name)
            print os.getcwd()+"/"+name
            self.update_dir()
            # Get last entry from Patient Directory Path list
            n = self.patient_dir_names.index(name)+1
            self.save(self.patient_dir_path[n],"data_clean",this_pulse_data.data_clean)
            self.save(self.patient_dir_path[n],"data_filtered1",this_pulse_data.data_filtered1)
            self.save(self.patient_dir_path[n],"data_filtered2",this_pulse_data.data_filtered2)
            self.save(self.patient_dir_path[n],"data_final",this_pulse_data.data_final)
            # Save Test Information (bpm, sample_period)
            data_info = [this_pulse_data.bpm, this_pulse_data.sample_period]
            self.save(self.patient_dir_path[n],"data_info",data_info)
        else:
            print "Directory already exists"


    # Writes patient data to specified filename
    # filename availability (should) be checked before passing it
    # but if not; add number to the end of it
    def save(self, path, filename, data):
        
        filename = filename + '.txt'
        fullpath = path + '/' + filename
        data_file = open(fullpath, 'w')

        for i in range(len(data)):
            # Data written to .txt file
            data_file.write(str(data[i]) + '\n')
        print filename + "Saved to: " +fullpath
        # Close data file
        data_file.close()

    # Take information from Patient Directory of the specified name
    # Load .txt files into appropriate pulse_data @params during intialization
    # Patient name choosen from list of Patient Directory names supplied by
    # the file_manager --> assume no incorrect directory name
    def load_all_data(self, name):
        n = self.patient_dir_names.index(name)+1
        # Load data_clean file
        data_clean = self.load(self.patient_dir_path[n]+'/data_clean.txt')
        # Load data_filtered1 file
        data_filtered1 = self.load(self.patient_dir_path[n]+'/data_filtered1.txt')
        # Load data_filtered2 file
        data_filtered2 = self.load(self.patient_dir_path[n]+'/data_filtered2.txt')
        # Load data_final file
        data_final = self.load(self.patient_dir_path[n]+'/data_final.txt')
        # Load data_info file
        data_info = self.load(self.patient_dir_path[n]+'/data_info.txt')
        bpm_val = data_info[0]
        sample_period = data_info[1]
        return pulse_data(data_clean, data_filtered1, data_filtered2, data_final, bpm_val, sample_period)

    # Take information from .txt file and format into list
    def load(self, fullpath):
        return [line.rstrip('\n') for line in open(fullpath)]

    # Checks database for matching Patient Directory
    # returns 0 if Patient Directory name is taken
    # returns 1 if Patient Directory is available
    # name @param is NOT formatted when passed
    def check_name(self, name):
        print "-----"
        dir_name = name.replace(" ","_")
        print name
        print dir_name == self.patient_dir_names[0]
        print self.patient_dir_names.count(dir_name)
        if self.patient_dir_names.count(dir_name) > 0:
            return 0
        return 1
