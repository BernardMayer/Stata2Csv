@cls
@setlocal enabledelayedexpansion
@rem 65001 UTF8, 1252 	West European Latin, 850 	Multilingual (Latin I), 437 	United States
@rem cscript.exe //U
@rem @CHCP 1252

@echo "Determiner le type (technique) de donnees de chaque colonne du fichier."

@set pythonBin="C:\CAT_dskD\myTools\Python\Python36\python.exe"
@set ColsDatatypePgm="C:\RepoGit\Stata2Csv\ColsDataType\colsDataType.py"
@set ColsToSqlPgm="C:\Laurence\M1-S2\Datas_IN\ColsToSql.py"
@set DescriptionFile="C:\Laurence\M1-S2\Datas_IN\4_ColsDatatypes.txt"
@set outFile="C:\Laurence\M1-S2\Datas_IN\5_ColsToSql.sql.txt"


%pythonBin% %ColsToSqlPgm% %DescriptionFile% %outFile%