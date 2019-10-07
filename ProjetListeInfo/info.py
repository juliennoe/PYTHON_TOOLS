import os
import json

chemin_dossier = os.path.dirname(__file__)
chemin_info = os.path.join(chemin_dossier,"data","info.json")
print(chemin_info)

def get_infos():
    infos_cle = []

    with open(chemin_info, "r") as f:
        infos_liste = json.load(f)

    for element in infos_liste:
        infos_cle.append(Info(element))
    
    return(infos_cle)
 
class Info:
    def __init__(self, entrer_info):
        self.entrer_info = entrer_info.title()

    def __str__(self):
        return self.entrer_info
    
    def _load_infos(self):
        with open(chemin_info,'r') as f:
            return json.load(f)
            
    def _set_infos(self, entrer_info):
        with open(chemin_info,'w') as f:
            json.dump(entrer_info, f, indent=4)

    def _add_infos(self):
        infos = self._load_infos()
        if self.entrer_info not in infos:
            infos.append(self.entrer_info)
            self._set_infos(infos)
            print('vous ajouter une info')
            return True
        else:
            print('deja la')
            return False

    def _remove_infos(self):
        infos = self._load_infos()
        if self.entrer_info in infos:
            infos.remove(self.entrer_info)
            self._set_infos(infos)
            print("vous retirer une info")
            return True
        else:
            print("cette info nexiste pas")
            return False

print(get_infos())