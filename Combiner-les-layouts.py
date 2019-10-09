from PySide import QtGui

class MonApplication(QtGui.QWidget):
	def __init__(self):
		super(MonApplication, self).__init__()

		# On cree un layout horizontal qui va contenir
		# nos 2 layouts verticaux.
		layoutPrincipal = QtGui.QHBoxLayout(self)

		# On cree 2 layouts verticaux
		layoutGauche = QtGui.QVBoxLayout()
		layoutDroite = QtGui.QVBoxLayout()
		
		# On ajoute les 2 layouts verticaux au layout
		# principal horizontal
		layoutPrincipal.addLayout(layoutGauche)
		layoutPrincipal.addLayout(layoutDroite)

		# On cree 3 boutons pour le layout gauche
		# et on les ajoute avec la fonction 'addWidget'
		btn_1 = QtGui.QPushButton('Bouton n1', self)
		btn_2 = QtGui.QPushButton('Bouton n2', self)
		btn_3 = QtGui.QPushButton('Bouton n3', self)

		layoutGauche.addWidget(btn_1)
		layoutGauche.addWidget(btn_2)
		layoutGauche.addWidget(btn_3)

		# On cree 3 autres boutons pour le layout droit
		btn_4 = QtGui.QPushButton('Bouton n4', self)
		btn_5 = QtGui.QPushButton('Bouton n5', self)
		btn_6 = QtGui.QPushButton('Bouton n6', self)

		layoutDroite.addWidget(btn_4)
		layoutDroite.addWidget(btn_5)
		layoutDroite.addWidget(btn_6)

		self.resize(500, 500)
		self.show()


app = QtGui.QApplication([])
fenetre = MonApplication()
app.exec_()

