# Stata2Csv
Conformer les fichiers .csv de Stata
------------------------------------
Le separateur est le caractere (;)
Les fichiers ne contiennent pas de guillemets doubles.
Ainsi, pour distinguer les valeurs nulles des chaines vides,
respectivement ;; et ;""; dans le cas des csv, 
Stata le peuplera par ;NA; et ;;

# ColsDataType
Analyser un fichier texte, avec separateur
------------------------------------------
Connaitre les types (physiques) de donnees 
afin de preparer un import en base de donnees.

# CommonCols
Designer un ensemble de fichiers texte, avec separateur.
A partir de leurs entetes, contenues sur leur premiere ligne,
fournir la liste des entetes communes a l'ensemble des fichiers.
