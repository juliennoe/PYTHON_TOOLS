from PySide2 import QtCore, QtGui, QtWidgets, Qt

class PremiereApplication(QtWidgets.QWidget):
    def __init__(self):
        super(PremiereApplication, self). __init__()
        self.setWindowTitle('mon application')
        self.setup_ui()

    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self)

        lb_box = QtWidgets.QLabel('DEMO DIFFERENT WIDGET')
        lb_box.setAlignment(QtCore.Qt.AlignCenter)

        ln_box = QtWidgets.QLineEdit('entrer votre nom')
        ln_box.clearFocus()

        btn_click = QtWidgets.QPushButton('valider')

        cmb_box = QtWidgets.QComboBox(self)
        cmb_box.addItems(['premier item','deuxieme item'])

        list_box = QtWidgets.QListWidget()
        list_box.addItems(['premier item','deuxieme item'])
        list_box.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)

        chk_box = QtWidgets.QCheckBox('conditions d\'utilisations')
        print(chk_box.checkState())

        prg_bar = QtWidgets.QProgressBar()
        prg_bar.setRange(1,100)
        prg_bar.setValue(47)

        layout.addWidget(lb_box)
        layout.addWidget(ln_box)
        layout.addWidget(cmb_box)
        layout.addWidget(btn_click)
        layout.addWidget(list_box)
        layout.addWidget(chk_box)
        layout.addWidget(prg_bar)

app = QtWidgets.QApplication([])
fenetre = PremiereApplication()
fenetre.show()
app.exec_()


    