import os
from glob import glob

CUR_DIR = os.path.dirname(__file__)
DATA_FOLDER = os.path.join(CUR_DIR, 'data')

def creerNote(nomDeLaNote, contenu=''):
    cheminDeLaNote = os.path.join(DATA_FOLDER,nomDeLaNote + '.txt')
    print(cheminDeLaNote)

    with open(cheminDeLaNote, 'w') as f:
        f.write(contenu)
    
    if os.path.isfile(cheminDeLaNote):
        print('la note {cheminDeLaNote} a bien été créer')

def supprimerNote(nomDeLaNote):
    cheminDeLaNote = os.path.join(DATA_FOLDER,nomDeLaNote + '.txt')
    if os.path.exists(cheminDeLaNote):
        os.remove(cheminDeLaNote)
        print('la note {cheminDeLaNote} a été supprimé')
    else:
        print('la note {cheminDeLaNote} n\'existe pas')

def recupererLesNotes():
    notes = glob(DATA_FOLDER + '/*.txt')
    notes = [os.path.splitext(os.path.split(n)[-1])[0] for n in notes]
    return notes

creerNote('PremiereNote', ' je suis chez ce cher serge')
#supprimerNote('PremiereNote')
recupererLesNotes()