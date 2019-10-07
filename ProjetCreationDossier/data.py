from PySide2 import QtWidgets
from gen_file import Dossier


class App(QtWidgets.QWidget):
    def __init__(self): # initialisation des infos
        super().__init__() # permet d'initialiser QWidgets a l'interieur de la classe App
        self.resize(500,50)
        self.setWindowTitle("chargement dossier")
        self.setup_ui()
        self.setup_connections()
        self.setup_css()

    def setup_ui(self): # definition de l'interface
        self.layout = QtWidgets.QVBoxLayout(self) # crea du layout general

        self.chemin_acces = QtWidgets.QLineEdit("") # crea du champ texte pour le chemin d'acces
        self.nom_dossier = QtWidgets.QLineEdit("") # crea du champ texte pour le nom de dossier
        self.btn_creer = QtWidgets.QPushButton("creer votre dossier") # crea du titre de la fenetre

        self.layout.addWidget(self.chemin_acces) # integration des widgets dans le layout
        self.layout.addWidget(self.nom_dossier) # integration des widgets dans le layout
        self.layout.addWidget(self.btn_creer) # integration des widgets dans le layout
    
    def setup_connections(self):
        self.btn_creer.clicked.connect(self.creation_dossier) # connection du bouton a la fonction creation_dossier
    
    def creation_dossier(self):
        _chemin_acces = self.chemin_acces.text() # variable pour recuperer le texte dans le champ text
        _nom_dossier = self.nom_dossier.text() # variable pour recuperer le texte dans le champ text
        d = Dossier(_chemin_acces,_nom_dossier) # creation d'instance de dossier
        d.crea_dossier() # acces a la fonction crea dossier

    def setup_css(self): # fonction pour definir le style CSS de l'interface
        self.setStyleSheet("""
       
        """)

app = QtWidgets.QApplication([]) # definition variable pour la creation de l'application
windows = App() # definition de l'instance de la classe
windows.show() # affichage de la fenetre
app.exec_() # exectution de l'app