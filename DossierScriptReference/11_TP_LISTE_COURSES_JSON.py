# -*- coding: utf-8 -*-
import os
import json

dossier_courant = os.path.dirname(__file__) # definition du chemin vers le dossier 
chemin_liste = os.path.join(dossier_courant, "liste.json") # récupération du chemin du dossier et ajout du nom du fichier
print(chemin_liste)

if os.path.exists(chemin_liste): # si le chemin existe
    with open(chemin_liste, "r") as f: # ouverture et lecture du fichier json
        liste_de_courses = json.load(f) # passation des infos du json dans la liste de courses
else:
    liste_de_courses = [] # sinon création de la liste de courses
affichage = """
Choisissez une option:
\t1: Ajouter un élément
\t2: Enlever un élément 
\t3: Afficher la liste
\t4: Vider la liste
\t5: Terminer
"""

option = "0" # set l'option a zero

while option != "5": 
    option = input(affichage)
    if option == "1":
        item_a_ajouter = input("Entrez le nom de l'élément à ajouter: ")
        liste_de_courses.append(item_a_ajouter) # APPEND
    elif option == "2":
        item_a_retirer = input("Entrez le nom de l'élément à enlever: ")
        if item_a_retirer in liste_de_courses:
            liste_de_courses.remove(item_a_retirer) # REMOVE
    elif option == "3":
        if liste_de_courses:
            print("\n".join(liste_de_courses))
        else:
            print("La liste ne contient aucun élément.")
    elif option == "4":
        liste_de_courses.clear() # CLEAR

with open(chemin_liste, "w") as f:
    json.dump(liste_de_courses, f, indent=4)