from PySide2 import QtWidgets
from UI_api_v2 import UI

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("vos paramètres")
        self.resize(500,500)
        self.setup_ui()
        self.setup_connection()
    
    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)

        self.label_creation = QtWidgets.QLabel("CREER VOTRE PROFIL")
        self.label_id = QtWidgets.QLabel("pseudo")
        self.champ_id = QtWidgets.QLineEdit()
        self.label_nom = QtWidgets.QLabel("nom")
        self.champ_nom = QtWidgets.QLineEdit()
        self.label_prenom = QtWidgets.QLabel("prenom")
        self.champ_prenom = QtWidgets.QLineEdit()
        self.label_photo = QtWidgets.QLabel("photo")
        self.champ_photo = QtWidgets.QLineEdit()
        self.btn_creer = QtWidgets.QPushButton("valider")

        self.label_modify = QtWidgets.QLabel("MODIFIER VOTRE PSEUDO")
        self.champ_old_key = QtWidgets.QLineEdit("votre pseudo actuel")
        self.champ_new_key = QtWidgets.QLineEdit("votre nouveau actuel")
        self.label_modify_item = QtWidgets.QLabel("MODIFIER VOS INFORMATIONS")
        self.champ_modify_item_user = QtWidgets.QLineEdit("votre pseudo actuel")
        self.champ_modify_item = QtWidgets.QLineEdit("l'element que vous souhaitez modifier")
        self.champ_new_item = QtWidgets.QLineEdit("nouvel élement")
        self.btn_modifier = QtWidgets.QPushButton("modifier pseudo")
        self.btn_modifier_item = QtWidgets.QPushButton("modifier item")

        self.label_remove = QtWidgets.QLabel("SUPPRIMER VOTRE PROFIL")
        self.champ_remove = QtWidgets.QLineEdit("votre pseudo")
        self.btn_supprimer = QtWidgets.QPushButton("supprimer")

        self.layout.addWidget(self.label_creation)
        self.layout.addWidget(self.label_id)
        self.layout.addWidget(self.champ_id)
        self.layout.addWidget(self.label_nom)
        self.layout.addWidget(self.champ_nom)
        self.layout.addWidget(self.label_prenom)
        self.layout.addWidget(self.champ_prenom)
        self.layout.addWidget(self.label_photo)
        self.layout.addWidget(self.champ_photo)
        self.layout.addWidget(self.btn_creer)

        self.layout.addWidget(self.label_modify)
        self.layout.addWidget(self.champ_old_key)
        self.layout.addWidget(self.champ_new_key)
        self.layout.addWidget(self.btn_modifier)
        self.layout.addWidget(self.label_modify_item)
        self.layout.addWidget(self.champ_modify_item_user)
        self.layout.addWidget(self.champ_modify_item)
        self.layout.addWidget(self.champ_new_item)
        self.layout.addWidget(self.btn_modifier_item)

        self.layout.addWidget(self.label_remove)
        self.layout.addWidget(self.champ_remove)
        self.layout.addWidget(self.btn_supprimer)

    def setup_connection(self):
        self.btn_creer.clicked.connect(self.create_profil)
        self.btn_supprimer.clicked.connect(self.remove_profil)
        self.btn_modifier.clicked.connect(self.modify_profil)
        self.btn_modifier_item.clicked.connect(self.modify_item)
    
    def create_profil(self):
        _user_id = self.champ_id.text()
        _nom = self.champ_nom.text()
        _prenom = self.champ_prenom.text()
        _photo = self.champ_photo.text()
        print(_user_id, _nom, _prenom, _photo)
        _profil = UI(_user_id, _nom, _prenom, _photo)
        _profil.write_database()
        print(_user_id, _nom, _prenom, _photo)
    
    def remove_profil(self):
        _user_id_remove = self.champ_remove.text()
        _profil = UI("default", "default", "default", "default")
        _profil.remove_key(_user_id_remove)
    
    def modify_profil(self):
        _old_key = self.champ_old_key.text()
        _new_key = self.champ_new_key.text()
        _profil = UI("default", "default", "default", "default")
        _profil.change_key(_new_key, _old_key)


    def modify_item(self):
        _first_key = self.champ_modify_item_user.text()
        _second_key = self.champ_modify_item.text()
        _new_item = self.champ_new_item.text()
        _profil = UI("default", "default", "default", "default")
        _profil.modify_key(_first_key, _second_key,_new_item)

    
a = QtWidgets.QApplication([])
window = App()
window.show()
a.exec_()

        