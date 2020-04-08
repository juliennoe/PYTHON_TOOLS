from PySide2 import QtWidgets
import _videoConverterFunction
import sys

class App(QtWidgets.QWidget): 
    
    def __init__(self): # initialisation 
        super(). __init__()
        self.setWindowTitle("Conversion fichiers H264 > Apple pro res 422 HQ")
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
        self.btn_creer_chemin.clicked.connect(self.conversion_videos)
    

    def conversion_videos(self): # definition de la fonction attachee au bouton
        _chemin_dossier = self.champ_chemin.text()
        _crea_dossier = _videoConverterFunction.RangeFile(_chemin_dossier)
        _crea_dossier.VideoConvert()
 
        print("FIN DE LA CONVERSION")
        sys.exit(0)
  

app = QtWidgets.QApplication([])
windows = App()
windows.show()
app.exec_()