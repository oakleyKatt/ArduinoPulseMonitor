#!/usr/bin/python

# Handles writing, loading, renaming, editing, etc. patient data files
class file_manager():

    def __init__(self):                                 # TO BE IMPLEMENTED
        # Populate with data files from Patient Data directory
        # list of filenames (for easy searching)
        pass

    # Writes patient data to specified filename
    # filename availability (should) be checked before passing it
    # but if not; add number to the end of it
    def save(self, filename, data):

        filename = filename + '.txt'
        data_file = open(filename, 'w')

        for i in range(len(data)):
            # Data written to .txt file
            data_file.write(str(data) + '\n')

        # Close data file
        data_file.close()

    def load(self, filename):
        # return data @ filename.txt
        pass

    # Checks database for matching filename
    # returns 0 if filename is taken
    # returns 1 if filename is available
    def check_filename(self, filename):                 # TO BE IMPLEMENTED

        return 1