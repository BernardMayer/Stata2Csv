@cls
@setlocal enabledelayedexpansion
@rem 65001 UTF8, 1252 	West European Latin, 850 	Multilingual (Latin I), 437 	United States
@rem cscript.exe //U
@rem @CHCP 1252

@echo "Recherche des variables communes a l'ensemble des fichiers Stata"

@set pythonBin="C:\CAT_dskD\myTools\Python\Python36\python.exe"
@set CommonColsPgm="C:\RepoGit\Stata2Csv\CommonCols\CommonCols.py"
@set list="C:\Laurence\M1-S2\Datas_IN\1_ListeDesFichiersEntete.txt"
@set outFile="C:\Laurence\M1-S2\Datas_IN\2_CommonCols.txt"

%pythonBin% %CommonColsPgm% %list% %outFile%