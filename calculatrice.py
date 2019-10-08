from PySide2 import QtWidgets, QtCore

class MainCalculatrice(QtWidgets.QWidget):
    def __init__(self):
        super(MainCalculatrice, self). __init__()
        self.setWindowTitle('calculatrice')
        
    def setup_ui(self):
        layout = QtWidgets.QGridLayout(self)

        lb_box = QtWidgets.QLabel('label')

        layout.addWidget(lb_box)

app = QtWidgets.QApplication([])
window = MainCalculatrice()
window.show()
app.exec_()


