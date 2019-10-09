from PySide2 import QtWidgets, QtCore

class MainCalculatrice(QtWidgets.QWidget):
    def __init__(self):
        super(MainCalculatrice, self). __init__()
        self.setWindowTitle('calculatrice')
        self.setup_ui()
        
    def setup_ui(self):
        layout = QtWidgets.QGridLayout(self)

        lb_box = QtWidgets.QLabel('Calculatrice Maison')
        lb_box.setAlignment(QtCore.Qt.AlignCenter)

        lne_box_1 = QtWidgets.QLineEdit()
        lne_box_2 = QtWidgets.QLineEdit()

        btn_box_0 = QtWidgets.QPushButton('0')
        btn_box_1 = QtWidgets.QPushButton('1')
        btn_box_2 = QtWidgets.QPushButton('2')
        btn_box_3 = QtWidgets.QPushButton('3')
        btn_box_4 = QtWidgets.QPushButton('4')
        btn_box_5 = QtWidgets.QPushButton('5')
        btn_box_6 = QtWidgets.QPushButton('6')
        btn_box_7 = QtWidgets.QPushButton('7')
        btn_box_8 = QtWidgets.QPushButton('8')
        btn_box_9 = QtWidgets.QPushButton('9')

        btn_box_c = QtWidgets.QPushButton('C')
        btn_box_slash = QtWidgets.QPushButton('/')
        btn_box_x = QtWidgets.QPushButton('x')
        btn_box_neg = QtWidgets.QPushButton('-')
        btn_box_add = QtWidgets.QPushButton('+')
        btn_box_equal = QtWidgets.QPushButton('=')
        btn_box_point = QtWidgets.QPushButton('.')



        layout.addWidget(lne_box_1, 0, 0, 1, 4)  
        layout.addWidget(lne_box_2, 1, 0, 1, 4)

        layout.addWidget(btn_box_0, 2, 0, 1, 1)
        layout.addWidget(btn_box_1, 2, 1, 1, 1)
        layout.addWidget(btn_box_2, 2, 2, 1, 1)
        layout.addWidget(btn_box_3, 2, 3, 1, 1)

        layout.addWidget(btn_box_4, 3, 0, 1, 1)
        layout.addWidget(btn_box_5, 3, 1, 1, 1)
        layout.addWidget(btn_box_6, 3, 2, 1, 1)
        layout.addWidget(btn_box_7, 3, 3, 1, 1)

        layout.addWidget(btn_box_8, 4, 0, 1, 1)
        layout.addWidget(btn_box_9, 4, 1, 1, 1)
        layout.addWidget(btn_box_equal, 4, 2, 1, 1)
        layout.addWidget(btn_box_add, 4, 3, 1, 1)

        layout.addWidget(btn_box_point, 5, 0, 1, 1)
        layout.addWidget(btn_box_neg, 5, 1, 1, 1)
        layout.addWidget(btn_box_slash, 5, 2, 1, 1)
        layout.addWidget(btn_box_c, 5, 3, 1, 1)

        layout.addWidget(btn_box_x, 6, 3, 1, 1)
       
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if isinstance(widget, QtWidgets.QPushButton):
                widget.setFixedSize(64,64)



        self.resize(500,500)

app = QtWidgets.QApplication([])
window = MainCalculatrice()
window.show()
app.exec_()


