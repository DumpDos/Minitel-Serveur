#!/usr/bin/env python

#--- bibiliotheques ---#
import serial
import time

# --- liaison serie --- #
ser = serial.Serial('/dev/ttyUSB0', 1200, timeout=2)

#--- commandes hayes ---#
at_start = 'AT\r\n'
at_reset = 'ATZ\r\n'
at_escap = 'ATE1\r\n'
at_facto = 'AT&F1\r\n'
at_memor = 'AT+MEA\r\n'
at_messa = 'AT&W\r\n'

# --- demmarage --- #
ser.write(at_start)
time.sleep(1)

# --- mode escape --- #
ser.write(at_escap)
time.sleep(1)

# --- etat usine --- #
ser.write(at_facto)
time.sleep(1)

# --- effacement memoire --- #
ser.write(at_memor)
time.sleep(1)

# --- effacement message --- #
ser.write(at_messa)
time.sleep(1)

# --- reset --- #
ser.write(at_reset)
time.sleep(1)

#--- fermeture liaison serie ---#
ser.close()

#--- sortie script ---#
sys.exit(0)

