@cls
@setlocal enabledelayedexpansion
@rem 65001 UTF8, 1252 	West European Latin, 850 	Multilingual (Latin I), 437 	United States
@rem cscript.exe //U
@rem @CHCP 1252

@set homeDir=".\"
@rem @set sqlBin="C:\CAT_dskD\myTools\sqlite\sqlite3.exe"
@rem @set sqlHome="C:\RepoGit\BOxi\FRS_Inventory_DocUpdate"
@rem @set sqlDB=%sqlHome%\BO_inventories.sqlite
@set pyBin="C:\CAT_dskD\myTools\Python\Python36\python.exe"
@rem @set dataInHome="D:\BOXI\Liste_Docs_TtesCrs\data"
@rem @set dataInHome="D:\BOXI\Liste_Docs_TtesCrs\Data-FullClientOnly-ToutesCaisses"
@rem @set dataInPattern="Liste_Docs_*.csv"
@set script=colsDataType.py

@REM Compilation des fichiers inventaires des FRS en 1 seul
@rem @set datasIn="C:\CAT_dskD\_perso\Laurence\Echantillons\enquete.test.csv"
@set datasIn="C:\CAT_dskD\_perso\Laurence\Echantillons\enquete.conforme.csv"
@set datasOut="C:\CAT_dskD\_perso\Laurence\Echantillons\enquete.colsDataType.csv"

@echo Conformation du fichier CSV Stata
%pyBin% %script% %datasIn% %datasOut%
