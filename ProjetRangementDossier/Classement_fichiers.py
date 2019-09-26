import os
import shutil

liste_file = os.listdir
Liste_extension = (".jpg",".jpeg")

class RangeFile:

    def __init__(self, chemin_dossier): # intialisation du chemin vers le dossier
        self.chemin_dossier =  chemin_dossier
        pass

    def range_files(self):

        for file in liste_file(self.chemin_dossier): # parcouru des fichiers dans le dossier

            if file.endswith(Liste_extension): # si le fichier fini par .jpeg .jpg

                dossier_final = os.path.join(self.chemin_dossier,"dossier_jpeg")
            
                if os.path.exists(dossier_final):
                    pass
                else:
                    os.mkdir(dossier_final) # creation du dossier "dossier_jpeg"
    
                start_source = os.path.join(self.chemin_dossier,file)
                print(start_source)
                end_source = os.path.join(dossier_final, file)
                print(end_source)

                shutil.move(start_source, end_source) # deplacement du fichier d'un point A a un point B
    
            elif file.endswith(".png"): # si le fichier fini par .png
    
                dossier_final = os.path.join(self.chemin_dossier,"dossier_png")
                if os.path.exists(dossier_final):
                    pass
                else:
                    os.mkdir(dossier_final) # creation du dossier "dossier_png"
    
                start_source = os.path.join(self.chemin_dossier,file)
                print(start_source)
                end_source = os.path.join(dossier_final, file)
                print(end_source)

                shutil.move(start_source, end_source) # deplacement du fichier d'un point A a un point B
    
            elif file.endswith(".psd"): # si le fichier fini par .psd
        
                dossier_final = os.path.join(self.chemin_dossier,"dossier_psd")
                if os.path.exists(dossier_final):
                    pass
                else:
                    os.mkdir(dossier_final)  # creation du dossier "dossier_psd"
    
                start_source = os.path.join(self.chemin_dossier,file)
                print(start_source)
                end_source = os.path.join(dossier_final, file)
                print(end_source)

                shutil.move(start_source, end_source) # deplacement du fichier d'un point A a un point B
           
            elif file.endswith(".txt"):
                dossier_final = os.path.join(self.chemin_dossier,"dossier_text")
                if os.path.exists(dossier_final):
                    pass
                else:
                    os.mkdir(dossier_final)
    
                start_source = os.path.join(self.chemin_dossier,file)
                print(start_source)
                end_source = os.path.join(dossier_final, file)
                print(end_source)

                shutil.move(start_source, end_source) # deplacement du fichier d'un point A a un point B
        


