import os
import json

dossiers = ['pierre','paul','jacques'] # CREATION DU TABLEAU DES DOSSIERS

chemin = '/Users/noe/Desktop/TEST' # CREATION DU CHEMIN REFERANT

fichier_json = '/Users/noe/Desktop/TEST/simple_json.json' # CREATION DU CHEMIN OU SERA STOCKER LE JSON

dictionnaire = { # CREATION D'UN DICTIONNAIRE
				"name":"julien",
				"age": 10,
				"taille": 1.37
				}


def VerifyJson(fichier_json):
	with open (fichier_json, 'r') as f:
		dictionnaireVerif = json.load(f)
		print('le fichier est deja la')


def SimpeFodler(): # CREATION DES DOSSIERS A PARTIR DU chemin DEFINI
	for dossier in dossiers:
		print(dossier)
	 	os.chdir(chemin)
	 	os.makedirs(dossier)


def WriteJson(fichier_json,dictionnaire): # ECRITURE DANS LE FICHIER JSON
	with open(fichier_json,'w') as f:
		json.dump(dictionnaire, f, indent =4)
		print('correct!')


if os.path.isfile(fichier_json): # SI UN JSON EST DEJA PRESENT / JE PRINT LE JSON
	VerifyJson(fichier_json)
else:
	SimpeFodler()
	WriteJson(fichier_json,dictionnaire)