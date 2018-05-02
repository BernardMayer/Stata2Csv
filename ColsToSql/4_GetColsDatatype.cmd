@cls
@setlocal enabledelayedexpansion
@rem 65001 UTF8, 1252 	West European Latin, 850 	Multilingual (Latin I), 437 	United States
@rem cscript.exe //U
@rem @CHCP 1252

@echo "Determiner le type (technique) de donnees de chaque colonne du fichier."

@set pythonBin="C:\CAT_dskD\myTools\Python\Python36\python.exe"
@set ColsDatatypePgm="C:\RepoGit\Stata2Csv\ColsDataType\colsDataType.py"
@set csvFile="C:\Laurence\M1-S2\Datas_IN\3_compile.tmp.txt"
@set outFile="C:\Laurence\M1-S2\Datas_IN\4_ColsDatatypes.txt"

@echo "Concatenation des fichiers CSV"
cd C:\Laurence\M1-S2\Datas_IN\3_Export
@rem cd c:\Laurence\M1-S2\Datas_IN\3_Export
@rem dir *.csv /b
REM copy ^
REM indiv_2004q1.csv + ^
REM indiv_2004q2.csv + ^
REM indiv_2004q3.csv + ^
REM indiv_2004q4.csv + ^
REM indiv_2005q1.csv + ^
REM indiv_2005q2.csv + ^
REM indiv_2005q3.csv + ^
REM indiv_2005q4.csv + ^
REM indiv_2006q1.csv + ^
REM indiv_2006q2.csv + ^
REM indiv_2006q3.csv + ^
REM indiv_2006q4.csv + ^
REM indiv_2007q1.csv + ^
REM indiv_2007q2.csv + ^
REM indiv_2007q3.csv + ^
REM indiv_2007q4.csv + ^
REM indiv_2008q1.csv + ^
REM indiv_2008q2.csv + ^
REM indiv_2008q3.csv + ^
REM indiv_2008q4.csv + ^
REM indiv_2009q1.csv + ^
REM indiv_2009q2.csv + ^
REM indiv_2009q3.csv + ^
REM indiv_2009q4.csv + ^
REM indiv_2010q1.csv + ^
REM indiv_2010q2.csv + ^
REM indiv_2010q3.csv + ^
REM indiv_2010q4.csv + ^
REM indiv_2011q1.csv + ^
REM indiv_2011q2.csv + ^
REM indiv_2011q3.csv + ^
REM indiv_2011q4.csv + ^
REM indiv_2012q1.csv + ^
REM indiv_2012q2.csv + ^
REM indiv_2012q3.csv + ^
REM indiv_2012q4.csv + ^
REM indiv_2013q1.csv + ^
REM indiv_2013q2.csv + ^
REM indiv_2013q3.csv + ^
REM indiv_2013q4.csv + ^
REM indiv_2014q1.csv + ^
REM indiv_2014q2.csv + ^
REM indiv_2014q3.csv + ^
REM indiv_2014q4.csv + ^
REM indiv_2015q1.csv + ^
REM indiv_2015q2.csv + ^
REM indiv_2015q3.csv + ^
REM indiv_2015q4.csv + ^
REM indiv_2016q1.csv + ^
REM indiv_2016q2.csv + ^
REM indiv_2016q3.csv + ^
REM indiv_2016q4.csv ^
REM %csvFile%
cd ..

%pythonBin% %ColsDatatypePgm% %csvFile% %outFile%