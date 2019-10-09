from PySide2 import QtWidgets, QtCore

class MainCalculatrice(QtWidgets.QWidget):
    def __init__(self):
        super(MainCalculatrice, self). __init__()
        self.setWindowTitle('les signaux')

        layout = QtWidgets.QHBoxLayout(self)
        
        btn_click = QtWidgets.QPushButton('click')
        btn_click.clicked.connect(self.click_signal)

        btn_release = QtWidgets.QPushButton('release')
        btn_click.released.connect(self.release_signal)


        layout.addWidget(btn_click)
        layout.addWidget(btn_release)

    def click_signal(self):
        print('click')
    
    def release_signal(self):
        print('realease')
    
       

app = QtWidgets.QApplication([])
window = MainCalculatrice()
window.show()
app.exec_()