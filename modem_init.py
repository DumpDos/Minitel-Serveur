import os
import sys
import serial
import time

# --- liaison serie --- #
ser = serial.Serial('/dev/ttyUSB0', 1200, timeout=2)

#os.system('/home/pi/minitel-server/serial_init.sh')

at_reset = 'ATZ0\r\n'
at_v23md = 'ATFS27=16S28=0\r\n'
at_ttone = 'ATA0\r\n'

# --- reset modem --- #
ser.write(at_reset)
time.sleep(1)

# --- reset modem --- #
ser.write(at_reset)
time.sleep(1)

# --- passage en v23 --- #
ser.write(at_v23md)
time.sleep(1)

# --- lancement ecoute --- #
ser.write(at_ttone)

ser.close()

