#!/usr/bin/env python

#--- bibiliotheques ---#
import serial 
import time

#--- liaison serie ---#
ser = serial.Serial('/dev/ttyUSB0', 1200, timeout=0)

#--- fonctions  ---#

#--- effacer ecran ---#
def efface_ecran():
	ser.write("\x0C")

#--- deconnexion modem minitel ---#
def deconnexion():
	ser.write("\x1B")
	time.sleep(1)
	ser.write("\x39")
	time.sleep(1)
	ser.write("\x67")