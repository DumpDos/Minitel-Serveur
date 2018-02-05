#!/usr/bin/python
# coding: utf-8

import urllib
from bs4 import BeautifulSoup


def metar(oaci_code):
    

    # déclaration variables
    url = "https://aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&stationString=%s&hoursBeforeNow=0.5" % oaci_code

    # récupération metar
    if oaci_code:
    
       page_xml = urllib.urlopen(url)
       page_var = BeautifulSoup(page_xml.read(), "lxml")
       var = page_var.find('data').text

       if not oaci_code in var:
   
           metar_var = "Aucune information disponible pour ce terrain"

       else:
           
           metar_var = page_var.find('raw_text').text
    
    else:
	
          metar_var = "Aucune information disponible pour ce terrain"

    return (metar_var)
