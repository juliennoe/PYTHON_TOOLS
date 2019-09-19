import os


class Dossier:

    def __init__(self, chemin_acces, nom_dossier):
        self.chemin_acces = chemin_acces
        self.nom_dossier = nom_dossier
        
    def crea_dossier(self):
        dossier = os.path.join(self.chemin_acces, self.nom_dossier)
        os.mkdir(dossier)
        
