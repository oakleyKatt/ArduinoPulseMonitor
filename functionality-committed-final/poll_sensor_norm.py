#!/usr/bin/python

import serial, time, string
import numpy
import struct

from Tkinter import *
#from Tkinter import ttk

# poll Serial for sensor data over sample_period (sec.)
def poll_for(sample_period):
    # Progressbar display window
    pb_window = Tk()
    pb_window.title("Measurement progressbar")
    pb_window_width = 400
    pb_window_height = 50
    
    # Progressbar - ttk
#    pb = ttk.Progressbar(pb_window, orient='horizontal', length=400, mode='determinate')
#    pb.pack()
    
    # Progressbar canvas
    pb_canvas = Canvas(pb_window, width=400, height=50)
    pb_canvas.pack()
    # Draw starting position of progressbar
    pb_canvas.create_rectangle(0, 0, 1, 50, fill='red')
    # Call progressbar window loop that doesn't block (rest of code)
    pb_window.update_idletasks()

    # Setup serial connection- 9600 bit rate (bps)
    ser = serial.Serial('/dev/ttyACM0',9600)

    # Sensor data written to .txt file
    data_file = open('pulseData.txt','w')

    # Sensor data stored in array
    sensor_data = []

    # Start time
    prog_start_time = time.time()
    
    # Count used to implement steady-state
    num_pts = 0
    
    # Time buffer for steady-state
    ss_buffer = 5

    # Total measurement time
    total_time = prog_start_time+sample_period+ss_buffer

    while time.time() < total_time:
        # Read data (hex) in from Serial
        bad_data_flag = 0
        try:
            data = int(ser.readline(), 16)
        except ValueError:
            print "bad serial data ignored"
            data = 0

        # Data written to .txt file
        data_file.write(str(data) + '\n')

        # Data stored in list
        sensor_data.append(data)

        # Increment measurement progressbar
        pb_val = (total_time-time.time())/(sample_period+ss_buffer)
        pb_canvas.delete('all')
        pb_canvas.create_rectangle(0, 0, 400-round(pb_val*400), 50, fill='red')
        pb_window.update()

    # Close .txt file
    data_file.close()

    # Close measurement progressbar window
    pb_window.destroy()

    return sensor_data[100:len(sensor_data)]
