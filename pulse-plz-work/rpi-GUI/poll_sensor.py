#!/usr/bin/python

import serial, time, string
import numpy


# poll Serial for sensor data over sample_period (sec.)
def poll_for(sample_period, patient_name):
    # Setup serial connection- 9600 bit rate (bps)
    ser = serial.Serial('/dev/ttyACM0', 9600)

    # Sensor data written to .txt file
#    patient_name.replace(" ", "_")
#    filename = patient_name + 'RAW.txt'
#    data_file = open(filename, 'w')

    # Sensor data stored in array
    sensor_data = []

    # Start time
    prog_start_time = time.time()

    while time.time() < prog_start_time + sample_period:
        # Read data (hex) in from Serial
        #        data = ser.readline().strip().strip('\x00')
        data = int(ser.readline(), 16)

#        print_str = time.time() + " < " +prog_start_time+sample_period
#        print print_str
#        print int(data)

        # Data written to .txt file
#        data_file.write(str(data) + '\n')

        # Data stored in array
        sensor_data.append(int(data))

    # Close .txt file
 #   data_file.close()

    # print sensor_data
    return sensor_data
