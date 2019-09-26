import os
import json
import logging
 
user_ref = {} # definition du dictionnaire
     
chemin_dossier = os.path.dirname(__file__) # concatenation du chemin de dossier
chemin_json = os.path.join(chemin_dossier,"user.json") # concatenation du chemin de dossier

if os.path.exists(chemin_json): # verification sil le fichier existe
    logging.warning("votre fichier existe déjà")
else :
    with open(chemin_json, 'w') as json_file:
        json.dump(user_ref, json_file)
        logging.warning("vous venez de créer votre fichier")

class UI: # creation de la class
    def __init__(self, user_id, nom, prenom, photo): # initialisation des elements necessaires
        self.user_id = user_id
        self.nom = nom.title()
        self.prenom = prenom.title()
        self.photo = photo

    def load_database(self): # lecture du fichier json
        with open(chemin_json,'r') as f:
             return json.load(f)
    
    def write_json(self, user_ref): # ecriture du fichier json
        with open(chemin_json,"w") as f:
            json.dump(user_ref, f, indent=4)
           
    def write_database(self): # definition des nouvelles valeurs via le dictionnaire et les noms de la fonction init
        
        user_ref = self.load_database()
        user_ref[self.user_id] = {"nom": self.nom, "prenom": self.prenom, "photo": self.photo}
        self.write_json(user_ref)
        print("tu as ajouter un profil")
           
    def change_key(self, new_key, old_key): # permet de changer une clé dans le dictionnaire
        user_ref = self.load_database()
        user_ref[new_key] = user_ref.pop(old_key)
        self.write_json(user_ref)
        print("tu as modifier ton profil")

    def modify_key(self, first_key, second_key, new_item):
        user_ref = self.load_database()
        user_ref[first_key][second_key] = new_item
        self.write_json(user_ref)
        print("tu as modifier un item")

    
    def remove_key(self, delete_key): # permet de retirer une clé d'un dictionnaire
        user_ref = self.load_database()
        del user_ref[delete_key]
        self.write_json(user_ref)
        print("tu as supprimer ton profil")

u = UI("id06", "catherine", "noe", "pict")
#u.write_database()
#u.change_key("id00", "prenom","default","none")
#u.remove_key("id06")









