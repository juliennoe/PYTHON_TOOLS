import os
import json

dictionnaire = {

"1" : {
    "prenom" : "julien",
    "age" : 29,
    "profession" : "developpeur",
    "adresse" : "laval"
    },

"2" : {
    "prenom" : "antoine",
    "age" : 29,
    "profession" : "veolia",
    "adresse" : "le mans"
    },

"3" : {
    "prenom" : "theo",
    "age" : 19,
    "profession" : "coiffeur",
    "adresse" : "mayenne"
    }
}

print(dictionnaire["3"]["adresse"])

dossier_parent = os.path.dirname(__file__)
fichier_referant = os.path.join(dossier_parent,'file_json.json')

with open(fichier_referant, 'w') as f:
    json.dump(dictionnaire,f,indent=4)

