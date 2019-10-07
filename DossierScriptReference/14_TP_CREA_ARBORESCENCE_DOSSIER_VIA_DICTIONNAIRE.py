import os

dossiers =  { # DEFINITION DU DICTIONNAIRE ET DÉFINITION DANS VALEURS DES CLÉS DANS UN TABLEAU

        "Films": ["le seigneur des anneaux",
                  "harry potter",
                  "avengers"],

        "Employes":["paul",
                    "pierre",
                    "jacques"],

        "Exercices":["les_variables",
                     "les boucles",
                     "les_fonctions"]
    
    }

dossier_parent = "C:\\Users\\Julien Noé\\OneDrive\\0_Bureau\\y_" # CREATION DE LA VARIABLE CHEMIN PARENT

for key, value in dossiers.items():# PREMIERE BOUCLES POUR RENTRER DANS LES ITEMS DU DICTIONNAIRE POUR ACCÉDER AUX CLÉS ET AUX VALEURS
    print(f'{key}{value}')
    
    for dossier in value: # ACCES AUX VALEURS

        concatenation = os.path.join(dossier_parent, key, dossier) # CONCATENATION DU CHEMIN D'ACCES

        os.makedirs(concatenation) # CREATION DE L'ARBORESCENCE

