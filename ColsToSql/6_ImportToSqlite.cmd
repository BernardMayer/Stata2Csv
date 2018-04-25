@cls
@setlocal enabledelayedexpansion
@rem 65001 UTF8, 1252 	West European Latin, 850 	Multilingual (Latin I), 437 	United States
@rem cscript.exe //U
@rem @CHCP 1252

@echo "Importer chacun des fichiers dans 1 base sqlite."

@set sqliteBin="C:\CAT_dskD\myTools\sqlite\sqlite3.exe"
@set db="C:\Laurence\M1-S2\Stata.sqlite"
@set dotCmdFile="C:\Laurence\M1-S2\Datas_IN\6_ImportToSqlite.dotCmd.txt"

%sqliteBin% %db% < %dotCmdFile%

@echo "Fin de l'import"