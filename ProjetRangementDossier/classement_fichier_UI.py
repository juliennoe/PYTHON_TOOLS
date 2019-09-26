from PySide2 import QtWidgets
import Classement_fichiers

class App(QtWidgets.QWidget): 
    
    def __init__(self): # initialisation 
        super(). __init__()
        self.setWindowTitle("Rangement dossiers")
        self.resize(900,50)
        self.setup_ui()
        self.setup_connection()
    
    def setup_ui(self): # definition de l'UI
    
        self.layout = QtWidgets.QHBoxLayout(self)

        self.label_chemin = QtWidgets.QLabel("le chemin de votre dossier")
        self.champ_chemin = QtWidgets.QLineEdit()

        self.btn_creer_chemin = QtWidgets.QPushButton("valider", self)

        self.layout.addWidget(self.label_chemin)
        self.layout.addWidget(self.champ_chemin)
        self.layout.addWidget(self.btn_creer_chemin)
    
    def setup_connection(self): # definition des connections
        self.btn_creer_chemin.clicked.connect(self.creation_dossier)
    

    def creation_dossier(self): # definition de la fonction attachée au bouton
        _chemin_dossier = self.champ_chemin.text()
        _crea_dossier = Classement_fichiers.RangeFile(_chemin_dossier)
        _crea_dossier.range_files()
        print("hello")

app = QtWidgets.QApplication([])
windows = App()
windows.show()
app.exec_()