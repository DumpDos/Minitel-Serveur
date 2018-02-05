#!/usr/bin/env python

#--- bibiliotheques ---#
import os
import sys
import serial
import time

# --- liaison serie --- #
ser = serial.Serial('/dev/ttyUSB0', 1200, timeout=2)

#--- commandes hayes ---#
at_reset = 'ATZ0\r\n'
at_v23md = 'ATFS27=16S28=0S10=30\r\n'
at_echod = 'ATF1M0\r\n'

# --- reset modem --- #
ser.write(at_reset)
time.sleep(0.2)

# --- reset modem --- #
ser.write(at_reset)
time.sleep(0.2)

# --- passage en v23 --- #
ser.write(at_v23md)
time.sleep(0.5)

# --- activer echo --- #
ser.write(at_echod) 
time.sleep(0.2)

#--- fermeture liaison serie  ---#
ser.close()
