from PySide2 import QtWidgets, QtCore, QtGui
from functools import partial
from custom_ui.calculatrice_ui import Ui_form_calculatrice

class MaCalculatrice(Ui_form_calculatrice, QtWidgets.QWidget):
    def __init__(self):
        super(MaCalculatrice, self).__init__()
        self.setupUi(self)
        self.setupConnections()
        self.setupRaccourcisClaviers()
       
    
    def modificationSetupUi(self):
        pass

    def setupConnections(self):
        self.btn_c.clicked.connect(self.printHere)

    def setupRaccourcisClaviers(self):
        QtWidgets.QShortcut(QtGui.QKeySequence('Esc'),self, self.printHere)

    def printHere(self):
        print("hello")


app = QtWidgets.QApplication([])
window = MaCalculatrice()
window.show()
app.exec_()
