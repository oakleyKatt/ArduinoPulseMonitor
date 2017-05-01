#!/usr/bin/python

import serial
import struct

ser = serial.Serial('/dev/ttyACM0',9600)
s = [0]
while 1:
    print ser.readline()
    #    read_serial = ser.readline()
#    s[0] = struct.unpack("h",read_serial)
 #   s[0] = str(int(ser.readline(),16))
 #   print s[0]
 #   print read_serial
