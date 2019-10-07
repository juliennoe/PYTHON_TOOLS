import json


chemin = "/Users/noe/Desktop/python/creation_dossier.txt"
chemin_json = "/Users/noe/Desktop/python/fichier_json.json"
#texte = input('votre texte ici')
"""
with open(chemin,'r') as f:
    contenu = f.read().splitlines()
    print(contenu)


with open(chemin,'w') as f:
    f.write('hello world')


with open(chemin,'a') as f:
    f.write('\nguten tag')



with open(chemin_json,'w') as f:
   json.dump('bonjour',f)



with open(chemin_json,'w') as f:
   json.dump(list(range(10)),f, indent=4)
"""

with open(chemin_json,'r') as f:
   liste_json = json.load(f)
   print(liste_json)