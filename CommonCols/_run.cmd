@cls
@setlocal enabledelayedexpansion
@rem 65001 UTF8, 1252 	West European Latin, 850 	Multilingual (Latin I), 437 	United States
@rem cscript.exe //U
@rem @CHCP 1252

@set homeDir=".\"
@rem @set sqlBin="C:\CAT_dskD\myTools\sqlite\sqlite3.exe"
@rem @set sqlHome="C:\RepoGit\BOxi\FRS_Inventory_DocUpdate"
@rem @set sqlDB=%sqlHome%\BO_inventories.sqlite
@rem @set pyBin="C:\CAT_dskD\myTools\Python\Python36\python.exe"
@set pyBin="D:\myTools\Python\Python36\python.exe"
@rem @set dataInHome="D:\BOXI\Liste_Docs_TtesCrs\data"
@rem @set dataInHome="D:\BOXI\Liste_Docs_TtesCrs\Data-FullClientOnly-ToutesCaisses"
@rem @set dataInPattern="Liste_Docs_*.csv"
@rem @set script=C:\RepoGit\Stata2Csv\CommonCols\CommonCols.py
@set script=D:\RepoS\Stata2Csv\CommonCols\CommonCols.py

@set list=ListeDesFichiersEntete.txt
@set outFile=D:\RepoS\Stata2Csv\CommonCols\CommonCols.txt

@echo GO !
%pyBin% %script% "%list%" "%outFile%"
