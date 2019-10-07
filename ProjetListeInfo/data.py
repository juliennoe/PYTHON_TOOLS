from PySide2 import QtWidgets
from info import get_infos
from info import Info

class App(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.setup_ui()
        self.load_infos()
        self.setup_connections()

    def setup_ui(self):

        self.layout = QtWidgets.QVBoxLayout(self)

        self.champ_ajout = QtWidgets.QLineEdit()
        self.btn_ajouter = QtWidgets.QPushButton("ajouter une info")
        self.champ_listes =  QtWidgets.QListWidget()
        self.champ_listes.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_supprimer = QtWidgets.QPushButton("supprimer une info")

        self.layout.addWidget(self.champ_ajout)
        self.layout.addWidget(self.btn_ajouter)
        self.layout.addWidget(self.champ_listes)
        self.layout.addWidget(self.btn_supprimer)
    
    def load_infos(self):
     
        infos_liste = get_infos()

        for element in infos_liste:
            self.champ_listes.addItem(element.entrer_info)
            print(element.entrer_info)
        
    def setup_connections(self):
        self.btn_ajouter.clicked.connect(self.add_info)
        self.btn_supprimer.clicked.connect(self.remove_info)
        self.champ_ajout.returnPressed.connect(self.add_info)

    def add_info(self):
        info_texte = self.champ_ajout.text()
        if not info_texte:
            return False
        
        i = Info(entrer_info=info_texte)
        resultat = i._add_infos()
        if resultat:
            self.champ_listes.addItem(i.entrer_info)
            self.champ_ajout.setText("")

    def remove_info(self):
        for selected_item in self.champ_listes.selectedItems():
            i = Info(selected_item.text())
            i._remove_infos()
            self.champ_listes.takeItem(self.champ_listes.row(selected_item))


app = QtWidgets.QApplication([])
windows = App()
windows.show()
app.exec_()