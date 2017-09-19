import os
import sys
import time
import serial

#--- Commandes Hayes ---#
at_ttone = 'ATA0\r\n'

#--- Variables de travail ---#
cnx = 'null'
por = 'null'

#--- initialisation modem ---#
execfile("modem_init.py")

time.sleep(2)
# --- liaison serie --- #
ser = serial.Serial('/dev/ttyUSB0', 1200, timeout=2)

#--- Attente appel ---#
print 'En ecoute'
while not 'RING' in cnx:
	cnx = ser.read(ser.inWaiting())
	time.sleep(1)

#--- Envoi porteuse serveur ---#
print 'Envoi porteuse'
ser.write(at_ttone)

#--- Detection porteuse minitel ---#
print 'Connexion en cours'
while not 'CONN' in por:
	por = ser.read(ser.inWaiting())
	time.sleep(1)

#--- Affichage page acceuil ---#
print 'Connecte, Affichage page acceuil'
#os.system('/home/pi/minitel-server/test.sh')

data = sys.stdin.readlines()
print "Counted", len(data), "lines."

sys.exit(0)
