#!/python
# -*- coding: utf-8 -*-

### http://sametmax.com/lencoding-en-python-une-bonne-fois-pour-toute/
from __future__ import unicode_literals, print_function

"""

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
# FileOutSep = TAB
# FileOutSep = "\n"
FileOutSep = " "   # STATA attend une espace comme separateur
FileOutHeader = False
Verbose = True

#bShowIdentifier = os.getenv("dsXidentifier", False)

def mode_XCYF() :
    #print(zeList)
    ## On fabrique un ensemble de tout les entetes connus
    setUnionAll = set()
    setUnionAll = zeList[0]['ensemble']
    for k, d in enumerate(zeList[1:]) :
        #print(zeList[k]["file"], FileOutSep.join(sorted(zeList[k]["ensemble"]))[0:177]) #[0:77]
        setUnionAll = setUnionAll.union(zeList[k]['ensemble'])
    # print("setUnionAll :", str(setUnionAll)[0:123])
    setUnionAll = sorted(setUnionAll)
    # print("setUnionAll :", str(setUnionAll)[0:123])
    # print("len(setUnionAll) :", len(setUnionAll))
    

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
    print(me + " : Pas le bon nombre de parametres :-( !", file=sys.stderr)
    print("Usage : " + me + " <Fichier contenant la liste des fichiers a examiner> <Fichier en sortie>", file=sys.stderr)
    quit()
else :
    fList   = sys.argv[1]
    outFile = sys.argv[2]
    

## Tests prealables
if (not os.path.exists(fList)) :
    print("Fichier [" + fList + "] introuvable", file=sys.stderr)
    quit()
# if (not os.path.exists(datasOut)) :
    # print("Fichier [" + datasOut + "] introuvable")
    # quit()

## Creation du fichier de sortie
try :
    fDatasOut = open(outFile, "w")
except :
    print("Pb a la creation du fichier de sortie ! FIN !", file=sys.stderr)
    quit()

    
    
## TS ISO8601 epoch
iso8601 = time.strftime("%Y%m%d%H%M%S")
epoch = int(time.time())
DT = time.strftime("%Y-%m-%d %H:%M:%S")
# print(datetime.datetime.now().isoformat()) # 2017-10-31T10:52:02.101865
# print(time.strftime("%Y-%m-%d %H:%M:%S")) # 2017-10-31 10:52:02
# print(int(time.time())) # 1509443642
mTimeEpoch = int(os.path.getmtime(fList)) # format epoch
# print("mTimeEpoch : " + str(mTimeEpoch))
# print(datetime.datetime.utcfromtimestamp(mTimeEpoch)) # 2017-10-19 13:40:11
mTimeStruct = time.localtime(mTimeEpoch)
# print("mTimeStruct : " + str(mTimeStruct)) # mTimeLocal : time.struct_time(tm_year=2017, tm_mon=10, tm_mday=19, tm_hour=15, tm_min=40, tm_sec=11, tm_wday=3, tm_yday=292, tm_isdst=1)
mTimeIso = time.strftime("%Y%m%d%H%M%S", mTimeStruct)
# print("mTimeIso : " + mTimeIso)

## Debut du traitement

##  Lecture de la liste pour la mettre dans ... une liste de dico
zeList = list()
print("Lecture du fichier liste [" + fList + "]", file=sys.stderr)
with open(fList, 'r') as ofList :
    for sFichier in ofList.readlines() :
        ##  Verification / conformation de la ligne ((presence EOL)
        sFichier = sFichier.rstrip()
        if (sFichier == "" or sFichier[0:1] == "#") :
            continue
        #print("sFichier :", sFichier)
        if (not os.path.exists(sFichier)) :
            print("Fichier [" + sFichier + "] introuvable", file=sys.stderr)
        else :
            d = dict()
            d['file'] = sFichier
            zeList.append(d)
print("La liste est lue", file=sys.stderr)
ofList.close()
zeListLen = len(zeList)
if (zeListLen < 2) :
    print("il n'y a pas assez de fichiers dans la liste ! FIN !", file=sys.stderr)
    exit()

##  Lecture de la premiere ligne de chaque fichier de la liste
print("Extraction des 1ere lignes", file=sys.stderr)
for d in zeList :
    with open(d['file'], 'r') as hFile :
        line = hFile.readline()
        if (line == "") :
            print("Fichier [" + d['file'] + "] vide ? --> retrait de la liste !", file=sys.stderr)
            d['valid'] = 0
        else :
            #print("line :", line)
            d['line'] = line
            d['tokens'] = re.split("\W", line)
            d['ensemble'] = set(d['tokens'])
            # si zero, alors fichier vide...
            d['valid'] = len(d['ensemble'])
    hFile.close()    
#print(zeList)        

##   Intersection des ensembles
if (zeList[0]['valid'] == 0) :
    print("Ce serait sympa si le premier fichier n'etait pas vide ! FIN !", file=sys.stderr)
    exit()
setZero = zeList[0]['ensemble']
for k, d in enumerate(zeList[1:]) :
    #print("k :", k, " d :", d)
    if (d['valid'] > 0) : 
        setZero = setZero.intersection(d['ensemble'])
# print(FileOutSep.join(sorted(setZero)))
fDatasOut.write(FileOutSep.join(sorted(setZero)))
fDatasOut.close()

##  Mode <None>, XCYF, 
mode = os.getenv('CommonCols_mode', "").upper()
print("mode :", mode)
if (mode == "XCYF") :
    ret = mode_XCYF()
elif (mode == "XFYC") :
    pass
    # print("2")
else :
    pass
    # print("3")

##Fin de traitement
print("Fin de traitement", file=sys.stderr)

exit()


if (True) :
# try :
    nLine = 0
    with open(datasIn, 'r') as fDatasIn :
        for line in fDatasIn.readlines() :
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
                    lCols.append({"name":None, "areNull":"N", "varchar":0, "areInt":"N", "areFloat":"N", "decimal":"0.0"})
            # Faire test de numero de ligne
            if (FileInHeader and nLine == 1) : 
                # On analyse la premiere ligne, c'est le header
                # chaque item de cols contient le nom de la colonne
                for k, v in enumerate(cols) :
                    lCols[k]["name"] = v
                continue
            for k, c in enumerate(cols) :
                ##  Analyse de la ligne
                # Une seule cellule a NULL et la colonne reste DEFINITIVEMENT comme nulle
                lenC = len(c)
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
    fDatasOut.write("name" + FileOutSep + "areNull" + FileOutSep + "areInt" + FileOutSep + "areFloat" + FileOutSep + "decimal" + FileOutSep + "varchar" + "\n")
    for d in lCols :
        #print(d)
        fDatasOut.write(d["name"] + FileOutSep + d["areNull"] + FileOutSep + d["areInt"] + FileOutSep + d["areFloat"] + FileOutSep + str(d["decimal"]) + FileOutSep + str(d["varchar"]) + "\n")
            
    ## FIN
    print("Analyse des " + str(nCols) + " colonnes de " + str(nLine) + " lignes")
# except Exception as e :
    # db.rollback()
    # print("Pb avec import de [" + datasIn + "]")
    # print(e)
fDatasOut.close()