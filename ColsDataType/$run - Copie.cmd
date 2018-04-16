@cls
@setlocal enabledelayedexpansion
@rem 65001 UTF8, 1252 	West European Latin, 850 	Multilingual (Latin I), 437 	United States
@rem cscript.exe //U
@rem @CHCP 1252

@set homeDir="C:\Laurence\M1-S2\Datas_IN"
@rem @set sqlBin="C:\CAT_dskD\myTools\sqlite\sqlite3.exe"
@rem @set sqlHome="C:\RepoGit\BOxi\FRS_Inventory_DocUpdate"
@rem @set sqlDB=%sqlHome%\BO_inventories.sqlite
@set pyBin="C:\CAT_dskD\myTools\Python\Python36\python.exe"
@rem @set dataInHome="D:\BOXI\Liste_Docs_TtesCrs\data"
@rem @set dataInHome="D:\BOXI\Liste_Docs_TtesCrs\Data-FullClientOnly-ToutesCaisses"
@rem @set dataInPattern="Liste_Docs_*.csv"
@set script=C:\RepoGit\Stata2Csv\ColsDataType\colsDataType.py

@REM Compilation des fichiers inventaires des FRS en 1 seul
@rem @set datasIn="C:\CAT_dskD\_perso\Laurence\Echantillons\enquete.test.csv"
REM @set datasIn="C:\CAT_dskD\_perso\Laurence\Echantillons\enquete.conforme.csv"
REM @set datasOut="C:\CAT_dskD\_perso\Laurence\Echantillons\enquete.colsDataType.csv"

REM set f=C:\Laurence\M1-S2\Datas_IN\indiv_2011q1-extrait
set f=%homeDir%\indiv_2011q1
@set datasIn="%f%.csv"
@set datasOut="%f%.colsDataType.csv"
@echo Analyse du fichier CSV Stata
rem %pyBin% %script% %datasIn% %datasOut% 

set f=%homeDir%\indiv_2012q4
%pyBin% %script% %f%.csv %f%.colsDataType.csv
pause
exit

set f=%homeDir%\indiv_2011q2
%pyBin% %script% %f%.csv %f%.colsDataType.csv
set f=%homeDir%\indiv_2011q3
%pyBin% %script% %f%.csv %f%.colsDataType.csv
set f=%homeDir%\indiv_2011q4
%pyBin% %script% %f%.csv %f%.colsDataType.csv
set f=%homeDir%\indiv_2012q1
%pyBin% %script% %f%.csv %f%.colsDataType.csv
set f=%homeDir%\indiv_2012q2
%pyBin% %script% %f%.csv %f%.colsDataType.csv
set f=%homeDir%\indiv_2012q3
%pyBin% %script% %f%.csv %f%.colsDataType.csv
set f=%homeDir%\indiv_2012q4
%pyBin% %script% %f%.csv %f%.colsDataType.csv
set f=%homeDir%\indiv_2013q1
%pyBin% %script% %f%.csv %f%.colsDataType.csv
set f=%homeDir%\indiv_2013q2
%pyBin% %script% %f%.csv %f%.colsDataType.csv
set f=%homeDir%\indiv_2013q3
%pyBin% %script% %f%.csv %f%.colsDataType.csv
set f=%homeDir%\indiv_2013q4
%pyBin% %script% %f%.csv %f%.colsDataType.csv
set f=%homeDir%\indiv_2014q1
%pyBin% %script% %f%.csv %f%.colsDataType.csv
set f=%homeDir%\indiv_2014q2
%pyBin% %script% %f%.csv %f%.colsDataType.csv
set f=%homeDir%\indiv_2014q3
%pyBin% %script% %f%.csv %f%.colsDataType.csv
set f=%homeDir%\indiv_2014q4
%pyBin% %script% %f%.csv %f%.colsDataType.csv
set f=%homeDir%\indiv_2015q1
%pyBin% %script% %f%.csv %f%.colsDataType.csv
set f=%homeDir%\indiv_2015q2
%pyBin% %script% %f%.csv %f%.colsDataType.csv
set f=%homeDir%\indiv_2015q3
%pyBin% %script% %f%.csv %f%.colsDataType.csv
set f=%homeDir%\indiv_2015q4
%pyBin% %script% %f%.csv %f%.colsDataType.csv
set f=%homeDir%\indiv_2016q1
%pyBin% %script% %f%.csv %f%.colsDataType.csv
set f=%homeDir%\indiv_2016q2
%pyBin% %script% %f%.csv %f%.colsDataType.csv
set f=%homeDir%\indiv_2016q3
%pyBin% %script% %f%.csv %f%.colsDataType.csv
set f=%homeDir%\indiv_2016q4
%pyBin% %script% %f%.csv %f%.colsDataType.csv
