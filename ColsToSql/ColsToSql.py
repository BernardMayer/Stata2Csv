#!/python
# -*- coding: utf-8 -*-

### http://sametmax.com/lencoding-en-python-une-bonne-fois-pour-toute/
from __future__ import unicode_literals

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
FileInSep = ";"
FileInHeader = True
FileOutSep = TAB #";"
FileOutHeader = False
Verbose = True
nLineStart = 2
nLineStop = 0
posName = 0
posType = 7
posDecim = 5
posVarchar = 6

##  Detection nombre decimal
reDecim = re.compile("^-{0,1}\d*[.,]{1,1}\d*$")
reInt   = re.compile("^-{0,1}\d*$")
reVarchar = re.compile("[a-zA-Z]+")

#bShowIdentifier = os.getenv("dsXidentifier", False)

def ForgeInteger(name) :
    return name + " INTEGER,"

def ForgeDecimal(name, decim) :
    return name + " DECIMAL(" + decim + "),"

def ForgeVarchar(name, varchar) :
    return name + " VARCHAR(" + varchar + "),"

def ForgeUnknow(name) :
	return name + " VARCHAR(1),"



## fichier a traiter
me = sys.argv[0]
#args = sys.argv[1:]
if (len(sys.argv) != 3) :
    print(me + " : Pas le bon nombre de parametres.")
    print("Usage : " + me + " <Chemin et nom du fichier de description> <Chemin et nom du fichier en sortie>")
    quit()
else :
    datasIn  = sys.argv[1]
    datasOut = sys.argv[2]
    print("Analyse du fichier de description [" + datasIn + "]")

## Tests prealables
if (not os.path.exists(datasIn)) :
    print("Fichier [" + datasIn + "] introuvable")
    quit()
# if (not os.path.exists(datasOut)) :
    # print("Fichier [" + datasOut + "] introuvable")
    # quit()

## Creation du fichier de sortie
fDatasOut = open(datasOut, "w")
fDatasOutTmp = open(datasOut + ".tmp", "w")

    
    
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
nLine = 0
ddl   = "CREATE TABLE <nomTable>"
lCols = list()
#with open(datasIn, encoding='utf-8', mode='r') as fDatasIn :
with open(datasIn, mode='r') as fDatasIn :
    for line in fDatasIn.readlines() :
        nLine += 1
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
        if (nLine < nLineStart) :
            continue
        if (nLineStop > 0 and nLine > nLineStop) :
            break
        cols = line.split(FileInSep)
        ##  
        # empco;N;Y;N;N;0.0;3;V  
        # empcon;N;Y;Y;N;0.0;0;I 
        # empcp;Y;Y;N;N;0.0;0;?  
        # emphnh;N;Y;N;Y;1.1;0;D 
        # posName = 0
        # posType = 7
        # posDecim = 5
        # posVarchar = 6
        name = cols[posName].upper()
        type = cols[posType].upper()
        if (type == "I") :
            lCols.append(ForgeInteger(name))
        elif (type == "D") :
            decim = cols[posDecim]
            lCols.append(ForgeDecimal(name, decim))
        elif (type == "V") :
            varchar = cols[posVarchar]
            lCols.append(ForgeVarchar(name, varchar))
        elif (type == "?") :
            lCols.append(ForgeUnknow(name))

# Suppression des derniers caracteres (,\n)
lCols[-1] = lCols[-1][0:-1]
print("CREATE TABLE <nom de la table> (")
fDatasOut.write("CREATE TABLE <nom de la table> (\n")
for col in lCols:
    print(col)
    fDatasOut.write(col + "\n")
print(", PRIMARY KEY (<col>, <col>)")
fDatasOut.write(", PRIMARY KEY (<col>, <col>)\n")
print(")")
fDatasOut.write(")\n")
fDatasOut.close()