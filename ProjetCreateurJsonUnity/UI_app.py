from PySide2 import QtWidgets

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("vos paramètres")
        self.setup_ui()
    
    def setup_ui(self):
        self.layout = QtWidgets.QHBoxLayout(self)
        self.champ_nom = QtWidgets.QTextEdit()

        self.layout.addWidget(self.champ_nom)


a = QtWidgets.QApplication([])
window = App()
window.show()
a.exec_()

        