import os
import json
# base = r'/Users/noe/Desktop/creation_dossier.txt' METHODE POUR LIRE CHEMIN WINDOWS
# base = base.replace('\\','/') METHODE POUR LIRE CHEMIN WINDOWS

racine = '/Users/noe/Desktop/STRUCTURE' #DEFINITION DU DOSSIER RACINE
simple_json = '/Users/noe/Desktop/STRUCTURE/Documents/test.json' #DEFINITION DU LIEU DE STOCKAGE ET CREATION DU JSON

structure = { # CREATION DU DICTIONNAIRE

			'Musique':['rock','jazz','pop'],
			'Documents':['factures','travail','admin'],
			'Photos':['vacances','famille'],
			'Videos':['facebook','chats']	

			}

def VerifyPath(simple_json): # CREATION DE LA FONCTION AFIN DE LIRE LE JSON SI CELUI CI EST EXISTANT
	with open(simple_json, 'r') as f:
		structureActuelle = json.load(f)
		print('le fichier est deja la')
		print('voici la hierarchie du dossier')
	for key, values in structure.items():
		print('. {0}'.format(key))
		for value in values:
			print('---{0}'.format(value))
		print('='*25)


def CreaDossier(dossiers): # CREATION DE LA FONCTION POUR CREER DES DOSSIERS ET SOUS DOSSIER VIA PYTHON
	for key, values in dossiers.items():
		for value in values:
			dossier = '{0}/{1}/{2}'.format(racine,key,value)
			os.makedirs(dossier)
			print('creation du dossier {0}'.format(dossier))

def WriteJson(fichier_json,dictionnaire): # CREATION DE LA FONCTION POUR ECRIRE DANS LE JSON
	with open(simple_json,'w') as f:
		json.dump(structure, f, indent = 4)



if os.path.isfile(simple_json): # SI UN JSON EST DEJA PRESENT / JE PRINT LE JSON
	VerifyPath(simple_json)
else:
	CreaDossier(structure) # SINON JE CREER LA STRUCTURE
	WriteJson(simple_json,structure)