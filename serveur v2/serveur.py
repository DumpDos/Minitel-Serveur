#!/usr/bin/python 
# coding: utf-8

import os
import sys
import time
import serial
import pynitel
import modules

#--- commandes hayes ---#
at_ttone = 'ATA0\r\n'

#--------------------------------------------------------------------#
#----------------------------- Script -------------------------------#
#--------------------------------------------------------------------#

def init():
    if len(sys.argv) > 2:
        (code) = (sys.argv[1])
    else:
        (code)=('')
    return(code)

def page_code():
    while True:
    	pynitel.home()
    	pynitel.xdraw('pages/page_code.vdt')
    	pynitel.bip()
    	(choix,touche) = pynitel.input_key(0, 1, 0, data='')
    	pynitel.cursor(False)
    	if touche == pynitel.sommaire:
	    break


def page_mitterrand():
     while True:
        pynitel.home()
        pynitel.xdraw('pages/mitterrand.vdt')
        pynitel.bip()
        (choix,touche) = pynitel.input_key(0, 1, 0, data='')
        pynitel.cursor(False)
        if touche == pynitel.sommaire:
            break

def page_info():
    
    touche = pynitel.repetition

    while True:
        pynitel.cursor(False)
	
	if touche == pynitel.repetition:
	   pynitel.home()
	   pynitel.xdraw('pages/page_info_0.vdt')
        (choix,touche) = pynitel.input_key(0, 1, 0, data='')	
	if touche == pynitel.suite:
	   pynitel.home()
           pynitel.xdraw('pages/page_info_1.vdt')

        if touche == pynitel.sommaire:
            break

def page_metar():

    touche = pynitel.repetition

    while True:

        if touche == pynitel.repetition:
           pynitel.home()
           pynitel.xdraw('pages/page_metar.vdt')
        
	(oaci_code,touche) = pynitel.input(14, 19, 4, data='')
        
	if touche == pynitel.envoi:
	   (metar) = modules.metar(oaci_code)
	   pynitel._del(17,10)
	   pynitel._del(18,0)
	   pynitel.pos(17,10)
	   
	   pynitel._print(metar)

        if touche == pynitel.sommaire:
            break
	
def page_jeux():

    touche = pynitel.repetition

    while True:

        if touche == pynitel.repetition:
           pynitel.home()
           pynitel.xdraw('pages/page_jeux.vdt')
        
	(jeux_code,touche) = pynitel.input(14, 19, 4, data='')
        
	if touche == pynitel.envoi:
		
	   if jeux_code == "DES":   
	      pynitel.xdraw('pages/page_jeux_des.vdt')
	      (jeux_nb,touche) = pynitel.input(14, 19, 4, data='')
	      (result_des) = modules.jeux_des(nb)

        if touche == pynitel.sommaire:
            break
	
def page_menu(code):

    touche = pynitel.repetition

    while True:
        # affichage initial ou répétition
        if touche == pynitel.repetition:
      	   pynitel.home()
           pynitel.xdraw('pages/page_acceuil.vdt')
	    		
	(code,touche) = pynitel.input(15, 8, 31, data='')
	print code
        if touche != pynitel.repetition:
            break 
    return (touche, code)


def recherche(code):
    "Effectue une recherche"
	
    if 'MITTERRAND' in code:
        print 'Affichage page mitterrand'
        page_mitterrand()

    elif 'CODE' in code:
        print 'Affichage page code'
        page_code()

    elif 'INFO' in code: 
	print 'Affichage page info'
        page_info()

    elif 'METAR' in code:
	print 'Affichage page metar'
	page_metar()
    
    elif 'JEUX' in code:
	print 'Affichage page jeux'
	page_jeux()

    else:
        pynitel.message(0, 1, 3, "Aucun service trouvé")
	
def serveur():
    (code) = init()
    while True:
    	(touche, code) = page_menu(code)
	
    	if touche == pynitel.envoi:
            pynitel.cursor(False)
            pynitel.pos(0,1)
            pynitel.flash()
            pynitel._print('Recherche... ')
	    recherche(code,)		
            code = ''
	
	if touche == pynitel.guide:
	    page_code()
	    code = ''
	
	if touche == pynitel.connexionfin:
	    pynitel.home()
	    pynitel.cursor(False)
            pynitel.pos(0,1)
            pynitel._print('Déconnexion')
	    pynitel.end()
	    break

#--------------------------------------------------------------------#
#----------------------------- Script -------------------------------#
#--------------------------------------------------------------------#

os.system('clear')

print '\033[34m***************************************************************'
print '*********************\033[31m Serveur Minitel \033[34m*************************'
print '*********************\033[33m  09 72 631 751  \033[34m*************************'
print '***************************************************************'

while True:
	#--- initialisation des variables ---#
	cnx = ''
	por = ''
	ctl = ''
	tim = 0
	#--- initialisation modem ---#
	print '\033[33mInitialisation'
	execfile("modem_init.py")
	time.sleep(0.5)

	# --- liaison serie --- #
	pynitel.conn = serial.Serial('/dev/ttyUSB0', 1200, parity=serial.PARITY_EVEN, bytesize=7, timeout=2)

	#--- attente appel ---#
	print '\033[32mAttente appel'
	while not 'RING' in cnx:
		cnx = pynitel.conn.read(pynitel.conn.inWaiting())
		time.sleep(1)

	#--- envoi porteuse serveur ---#
	print '\033[33mEnvoi porteuse'
	pynitel.conn.write(at_ttone)

	#--- detection porteuse minitel ---#
	print '\033[33mConnexion en cours'
	while not 'CONN' in por:
		por = pynitel.conn.read(pynitel.conn.inWaiting())
		time.sleep(1)

		#--- timer avant arret ---#
		if tim > 30:
			print '\033[31mNon connecté'
			ctl = False
			break

		else:
			tim = tim + 1

	#--- verification connexion ---#
	if ctl != False:

		#--- affichage pages ---#
		print '\033[32mConnecté, Affichage page acceuil'
		serveur()
		print '\033[33mDéconnexion'
		time.sleep(6)
	else:
		print '\033[33mRéinitialisation'
#--- fin ---#
