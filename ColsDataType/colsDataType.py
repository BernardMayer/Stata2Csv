#!/python
# -*- coding: utf-8 -*-

### http://sametmax.com/lencoding-en-python-une-bonne-fois-pour-toute/
from __future__ import unicode_literals

"""
Importer les extractions du FRS BO dans la base de donnees

(separateur est \t et non plus | )
##  CE	AWZEddzi5GZMnYKK70cB5J8	5151	FullClient	Liste des automates sans activite depuis 24H	Root Folder/Documents CACP/Direction Bancaire et Technologies	22/09/2016 13:40:40	22/09/2016 13:40:40
CREATE TABLE BO_DOCS_LISTE (
	CR_ID INTEGER NOT NULL,
	SI_ID INTEGER NOT NULL,
	SI_CUID TEXT NOT NULL,
	SI_NAME TEXT NOT NULL,
	SI_KIND TEXT,
	DOC_FOLDER TEXT,
	DT_CREATE TEXT,
	DT_MODIF TEXT NOT NULL
);
##  Quel est l'ordre des colonnes du fichier, par rapport aux colonnes de la table ?
##  Definir les colonnes de la table, dans l'ordre dans lequel elles se presentent dans le fichier.
##  chercher --> colsName = ("CR_ID", "SI_CUID", "SI_ID", "SI_KIND", "SI_NAME", "DOC_FOLDER", "DT_CREATE", "DT_MODIF")
"""

import cgitb
cgitb.enable(format='text')
import pyodbc
import sqlite3
import hashlib
import sys
import os
#import string
import pathlib
import argparse
import configparser
import re
#from collections import OrderedDict
import collections
import time
import datetime
import decimal
decimal.getcontext().prec = 2
TAB = '\t'
dtNow  = datetime.datetime.today()
tsNow = dtNow.timestamp()

##  
##  Les parametres de fonctionnement
##  
FileInSep = TAB #";"
FileInHeader = True
FileOutSep = TAB
FileOutHeader = False
Verbose = True


#bShowIdentifier = os.getenv("dsXidentifier", False)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    return False

## fichier a traiter
me = sys.argv[0]
#args = sys.argv[1:]
if (len(sys.argv) != 3) :
    print(me + " : Pas le bon nombre de parametres.")
    print("Usage : " + me + " <Chemin et nom du fichier en entree> <Chemin et nom du fichier en sortie>")
    quit()
else :
    datasIn  = sys.argv[1]
    datasOut = sys.argv[2]
    print("Analyse du fichier CSV Stata [" + datasIn + "]")

## Tests prealables
if (not os.path.exists(datasIn)) :
    print("Fichier [" + datasIn + "] introuvable")
    quit()
# if (not os.path.exists(datasOut)) :
    # print("Fichier [" + datasOut + "] introuvable")
    # quit()

## Creation du fichier de sortie
fDatasOut = open(datasOut, "w")


    
    
## TS ISO8601 epoch
iso8601 = time.strftime("%Y%m%d%H%M%S")
epoch = int(time.time())
DT = time.strftime("%Y-%m-%d %H:%M:%S")
# print(datetime.datetime.now().isoformat()) # 2017-10-31T10:52:02.101865
# print(time.strftime("%Y-%m-%d %H:%M:%S")) # 2017-10-31 10:52:02
# print(int(time.time())) # 1509443642
mTimeEpoch = int(os.path.getmtime(datasIn)) # format epoch
# print("mTimeEpoch : " + str(mTimeEpoch))
# print(datetime.datetime.utcfromtimestamp(mTimeEpoch)) # 2017-10-19 13:40:11
mTimeStruct = time.localtime(mTimeEpoch)
# print("mTimeStruct : " + str(mTimeStruct)) # mTimeLocal : time.struct_time(tm_year=2017, tm_mon=10, tm_mday=19, tm_hour=15, tm_min=40, tm_sec=11, tm_wday=3, tm_yday=292, tm_isdst=1)
mTimeIso = time.strftime("%Y%m%d%H%M%S", mTimeStruct)
# print("mTimeIso : " + mTimeIso)

## Debut du traitement
lCols = list()
if (True) :
# try :
    nLine = 0
    #with open(datasIn, encoding='utf-8', mode='r') as fDatasIn :
    with open(datasIn, mode='r') as fDatasIn :
        for line in fDatasIn.readlines() :
            if (False) :
                print("Ligne :", nLine, "\t\t", line)
            ##  Verification / conformation de la ligne
            line = line.rstrip()
            if (line == "") :
                continue
            # if (line[0:1] == "-" or line[0:1] == "'" or line[0:1] == "#") :
                # continue
            # On attend un code alphanumerique comme premier caractere
            # La compilation des fichiers en 1 seul ajoute 1 derniere ligne constituee du caractere \x1a ou \x1e ou \xe9
            # if (not line[0:1].isalnum()) : 
                # continue 
            nLine += 1
            cols = line.split(FileInSep)
            if (nLine == 1) :
                # Initialisation de la structure de donnees
                nCols = len(cols) # 428
                for c in cols :
                    lCols.append({"name":None, "areEmpty":"Y", "areNull":"N", "varchar":0, "areInt":"N", "areFloat":"N", "decimal":"0.0"})
            # Faire test de numero de ligne
            if (FileInHeader and nLine == 1) : 
                # On analyse la premiere ligne, c'est le header
                # chaque item de cols contient le nom de la colonne
                for k, v in enumerate(cols) :
                    lCols[k]["name"] = v
                continue
            for k, c in enumerate(cols) :
                ##  Analyse de la ligne
                lenC = len(c)
                # L'ensemble des cellules de la colonne est NULL la colonne est declaree EMPTY
                if (lCols[k]["areEmpty"] == "Y" and lenC != 0) :
                    lCols[k]["areEmpty"] = "N"
                # Une seule cellule a NULL et la colonne reste DEFINITIVEMENT comme nulle
                if (lCols[k]["areNull"] == "N" and lenC == 0) :
                    lCols[k]["areNull"] = "Y"
                elif (lCols[k]["areInt"] == "N" and c.isdigit() and lCols[k]["areFloat"] != "Y") :  
                    lCols[k]["areInt"] = "Y"
                elif (lCols[k]["areFloat"] == "N" and not c.isdigit() and is_number(c)) : # 
                    lCols[k]["areFloat"] = "Y"
                    lCols[k]["areInt"] = "N"
                    # quel gabarit de decimal ? decimal(radix.decimal)
                    try :
                        (radix, decim) = c.split(".")
                        (radixMax, decimMax) = lCols[k]["decimal"].split(".")
                        #print("c[" + c + "] radix=[" + radix + "] decim[" + decim + "]", radix.isdigit(), decim.isdigit())
                        if (radix.isdigit() and decim.isdigit()) :
                            radixMax = max(int(radixMax), len(radix))
                            decimMax = max(int(decimMax), len(decim))
                            #print("radixMax=[" + str(radixMax) + "] decimMax[" + str(decimMax) + "]")
                            lCols[k]["decimal"] = str(radixMax) + "." + str(decimMax)
                    except :
                        pass
                #elif (lenC >= 2 and c[0] == '"' and c[-1] == '"') : 
                else :
                    if (lCols[k]["areInt"] == "Y" or lCols[k]["areFloat"] == "Y") :
                        lCols[k]["varchar"] = "0"
                    else :
                        lCols[k]["varchar"] = max(lCols[k]["varchar"], lenC)
    
    fDatasOut.write("Analyse des " + str(nCols) + " colonnes de " + str(nLine) + " lignes" + "\n")
    fDatasOut.write("name" + FileOutSep + "areEmpty" + FileOutSep + "areNull" + FileOutSep + "areInt" + FileOutSep + "areFloat" + FileOutSep + "decimal" + FileOutSep + "varchar" + "\n")
    for d in lCols :
        #print(d)
        fDatasOut.write(d["name"] + FileOutSep + d["areEmpty"] + FileOutSep + d["areNull"] + FileOutSep + d["areInt"] + FileOutSep + d["areFloat"] + FileOutSep + str(d["decimal"]) + FileOutSep + str(d["varchar"]) + "\n")
            
    ## FIN
    print("Analyse des " + str(nCols) + " colonnes de " + str(nLine) + " lignes")
# except Exception as e :
    # db.rollback()
    # print("Pb avec import de [" + datasIn + "]")
    # print(e)
fDatasOut.close()