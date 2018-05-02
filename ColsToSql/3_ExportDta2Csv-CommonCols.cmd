@cls
@setlocal enabledelayedexpansion
@rem 65001 UTF8, 1252 	West European Latin, 850 	Multilingual (Latin I), 437 	United States
@rem cscript.exe //U
@rem @CHCP 1252

@echo "Export des colonnes communes des fichiers Stata"

@set stataBin="C:\Laurence\M1-S2\StataCorp Stata 14.2\stata.exe"
@set stataDoFile="C:\Laurence\M1-S2\Datas_IN\3_ExportDta2Csv-CommonCols.do.txt"

%stataBin% /b do %stataDoFile%

echo "Fin de l'export des colonnes communes"