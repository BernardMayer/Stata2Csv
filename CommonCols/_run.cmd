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
@rem @set pyBin="D:\myTools\Python\Python36\python.exe"
@rem @set dataInHome="D:\BOXI\Liste_Docs_TtesCrs\data"
@rem @set dataInHome="D:\BOXI\Liste_Docs_TtesCrs\Data-FullClientOnly-ToutesCaisses"
@rem @set dataInPattern="Liste_Docs_*.csv"
@set script=C:\RepoGit\Stata2Csv\CommonCols\CommonCols.py
@rem @set script=D:\RepoS\Stata2Csv\CommonCols\CommonCols.py

@set list=C:\Laurence\M1-S2\Datas_IN\ListeDesFichiersEntete.txt
@set outFile=C:\Laurence\M1-S2\Datas_IN\CommonCols.txt
@rem @set outFile=D:\RepoS\Stata2Csv\CommonCols\CommonCols.txt
@rem X porte les colonnes, Y porte les noms de fichiers
@rem mode = <rien>, XCYF, XFYC
@set CommonCols_mode=

@echo GO !
%pyBin% %script% "%list%" "%outFile%"
