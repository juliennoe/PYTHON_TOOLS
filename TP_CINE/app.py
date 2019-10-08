from PySide2 import QtWidgets
import movie  

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.resize(270,500)
        self.setup_ui()
        self.populate_movies()

    def setup_ui(self):

        #1#DEFINIR LE LAYOUT
        self.layout = QtWidgets.QVBoxLayout(self)
        #2#DEFINIR LES BOUTONS
        self.btn_ajouter = QtWidgets.QPushButton("ajouter des films")
        self.btn_supprimer = QtWidgets.QPushButton("supprimer des films")
        self.champ_film = QtWidgets.QLineEdit()
        self.champ_liste = QtWidgets.QListWidget()
        #3#AJOUTER LES BOUTONS DANS LE LAYOUT
        self.layout.addWidget(self.champ_film)
        self.layout.addWidget(self.btn_ajouter)
        self.layout.addWidget(self.champ_liste)
        self.layout.addWidget(self.btn_supprimer)

    def populate_movies(self):
        liste_film = movie.get_movies()

        for films in liste_film:
            self.champ_liste.addItem(films)

app = QtWidgets.QApplication([])
windows = App()
windows.show()
app.exec_()