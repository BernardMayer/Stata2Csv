@cls
@setlocal enabledelayedexpansion
@rem 65001 UTF8, 1252 	West European Latin, 850 	Multilingual (Latin I), 437 	United States
@rem cscript.exe //U
@rem @CHCP 1252

@echo "Exporter dans 1 fichier les lignes acteu6 = 1 pour 242 variables."

@set sqliteBin="C:\CAT_dskD\myTools\sqlite\sqlite3.exe"
@set db="C:\Laurence\M1-S2\Stata.sqlite"
@set dotCmdFile="C:\Laurence\M1-S2\Datas_OUT\12_ExportFromSqlite.dotCmd.txt"
@set outFile="C:\Laurence\M1-S2\Datas_OUT\acteu6_1-242vars.csv"

%sqliteBin% %db% < %dotCmdFile% > %outFile%

@echo "Fin de l'export"