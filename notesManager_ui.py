from PySide2 import QtWidgets, QtCore, QtGui
from ui.fenetrePrincipale import Ui_fenetrePrincipale
import notesManager as nm
import os

CUR_DIR = os.path.dirname(__file__)
DATA_FOLDER = os.path.join(CUR_DIR, 'data')

class createurDeNote(QtWidgets.QWidget, Ui_fenetrePrincipale):
    def __init__(self):
        super(createurDeNote, self).__init__()

        self.setupUi(self)
        self.recupererNotes()
        self.setupConnections()
        self.show()

    def setupConnections(self):
        self.btn_creerNote.clicked.connect(self.creerNote)
        self.lw_listeDeNotes.itemClicked.connect(self.afficherLaNote)
        self.btn_mettreAJourNote.clicked.connect(self.mettreAjourLaNote)
        self.btn_supprimerNote.clicked.connect(self.supprimerNote)



    def creerNote(self):
        nomDeLaNote, ok = QtWidgets.QInputDialog.getText(self, 'creer une note', 'entrer le nom de la note')
        if not ok:
            return
        
        nm.creerNote(nomDeLaNote)
        self.recupererNotes()
    
    def recupererNoteSelectionnee(self):
        notesSelectionnees = self.lw_listeDeNotes.selectedItems()
        if not notesSelectionnees:
            return
        
        nomDeLaNote = notesSelectionnees[-1].text()
        cheminDeLaNote = os.path.join(DATA_FOLDER, nomDeLaNote + '.txt')
        return nomDeLaNote, cheminDeLaNote
    
    def afficherLaNote(self):
        print('afficher note')

    def mettreAjourLaNote(self):
        print('mettre a jour note')
        self.recupererNoteSelectionnee()

    def supprimerNote(self):
        nomDeLaNote, cheminDeLaNote = self.recupererNoteSelectionnee()
        nm.supprimerNote(nomDeLaNote)
        self.recupererNotes()

    def recupererNotes(self):
        self.lw_listeDeNotes.clear()
        notes = nm.recupererLesNotes()
        self.lw_listeDeNotes.addItems(notes)
       




app = QtWidgets.QApplication([])
nc = createurDeNote()
app.exec_()