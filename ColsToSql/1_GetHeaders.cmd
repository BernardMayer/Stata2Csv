@cls
@setlocal enabledelayedexpansion
@rem 65001 UTF8, 1252 	West European Latin, 850 	Multilingual (Latin I), 437 	United States
@rem cscript.exe //U
@rem @CHCP 1252

@echo "Export de la 1ere ligne (entete) des fichiers Stata"

@set stataBin="C:\Laurence\M1-S2\StataCorp Stata 14.2\stata.exe"
@set stataDoFile="C:\Laurence\M1-S2\Datas_IN\1_ExportDtaHeader.do.txt"

%stataBin% /b do %stataDoFile%

echo "Fin de la recuperation des entetes"