#!/usr/bin/env python

#--- bibiliotheques ---#
import os
import sys
import time
import serial
import fonction

#--- commandes hayes ---#
at_ttone = 'ATA0\r\n'

#--------------------------------------------------------------------#
#----------------------------- Script -------------------------------#
#--------------------------------------------------------------------#

#--- haut de page ---#
os.system('clear')

print '***************************************************************'
print '********************* Serveur Minitel *************************'
print '***************************************************************'

while True:
	#--- initialisation des variables ---#
	tim = 0
	dcx = 0
	cnx = ''
	por = ''
	din = ''
	ctl = ''

	#--- initialisation modem ---#
	execfile("modem_init.py")
	time.sleep(0.5)

	# --- liaison serie --- #
	ser = serial.Serial('/dev/ttyUSB0', 1200, timeout=0)

	#--- attente appel ---#
	print 'Attente appel'
	while not 'RING' in cnx:
		cnx = ser.read(ser.inWaiting())
		time.sleep(1)

	#--- envoi porteuse serveur ---#
	print 'Envoi porteuse'
	ser.write(at_ttone)

	#--- detection porteuse minitel ---#
	print 'Connexion en cours'
	while not 'CONN' in por:
		por = ser.read(ser.inWaiting())
		time.sleep(1)

		#--- timer avant arret ---#
		if tim > 15:
			print 'Non connecte'
			ctl = False
			break

		else:
			tim = tim + 1

	#--- verification connexion ---#
	if ctl != False:

		#--- affichage pages ---#
		print 'Connecte, Affichage page acceuil'
		os.system('/home/pi/minitel-server/test.sh') 

		#--- timer avant deconnexion ---#
		while True:
			time.sleep(1)

			if dcx > 29:
				print 'Deconnexion'
				fonction.deconnexion()
				time.sleep(3)
				print 'Reinitialisation'
				break
			else:
				dcx = dcx + 1
				print dcx
	else:
		print 'Reinitialisation'
#--- fin ---#
