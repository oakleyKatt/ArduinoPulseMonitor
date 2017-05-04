#!/usr/bin/python

import serial, time, string
import numpy

# Setup serial connection- 9600 bit rate (bps)
ser = serial.Serial('/dev/ttyACM0',9600)

# Sensor data written to .txt file
data_file = open('pulseData.txt','w')

# Sensor data stored in array
sensor_data = []

# Sample period (seconds)
sample_period = 3
# Start time
prog_start_time = time.time()

while time.time() < prog_start_time+sample_period:
    # Read data in from Serial
    data = ser.readline()

    # Data written to .txt file
    data_file.write(str(data) + '\n')
    
    # Data stored in array
    sensor_data.append(int(data))

# Close .txt file
data_file.close()

print sensor_data
