import os
import shutil  
import sys
import subprocess
import ffmpeg

folderList = ['rush_mp4', 'rush_mov']

class RangeFile:
    
    def __init__(self, chemin_dossier): # intialisation du chemin vers le dossier
        self.chemin_dossier =  chemin_dossier
        pass

    #Lance la conversion des fichiers MP4 en .MOV avec le codec Apple Prores_ks
    def VideoConvert(self):
        directory = self.chemin_dossier
        for vid in os.listdir(directory):
            if vid.endswith('.mp4'):
                fileName = " " + str(vid) + ".mov"
                print(fileName)
                print("DEBUT DE LA CONVERSION")
                finalConvert = "ffmpeg -i " + vid + " -c:v prores_ks" + " -preset" + " ultrafast" + " -profile:v 3" + " -c:a pcm_s16le" + fileName
                #ffmpeg -i input -c:v libx264 -preset ultrafast -crf 0 output.mkv
                subprocess.call(finalConvert, shell = True)
        
        for file in os.listdir(directory):
            print(file)
            if file.endswith(".mov"):
                actualName = str(file)
                print(actualName)
                deleteName = ".mp4"
                actualName = actualName.replace(deleteName, "")
                print(actualName)
                os.rename(file, actualName)
        
        for folder in folderList:
            if os.path.exists(os.path.join(directory, folder)):
                print("vous avez deja vos dossiers")
                pass
            else:
                os.mkdir(os.path.join(directory, folder))
                print(directory)
        
        for vid in os.listdir():
            if vid.endswith(".mov"):
                start_source = os.path.join(directory,vid)
                print(start_source)
                end_source = os.path.join(directory + '/rush_mov',vid)
                print(end_source)
                shutil.move(start_source, end_source)

            elif vid.endswith(".mp4"):
                start_source = os.path.join(directory,vid)
                end_source = os.path.join(directory + '/rush_mp4',vid)
                shutil.move(start_source, end_source)

print('Vos donnees sont pretes !')
