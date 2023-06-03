import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip
from PyQt5.QtGui import QIcon



class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("calculator")
        self.setGeometry(200,200,700,700)
        self.setWindowIcon(QIcon("calculator_icon.png"))
        self.initUI()
    
    def islem(self):
        ifade=self.txt_screen.text()
        hesap = eval(ifade)
        self.lbl_result.setText("result: "+str(hesap))


    def print_screen(self):
        buton=self.sender()
        text = buton.text()

        older_text=self.txt_screen.text()
        self.txt_screen.setText(older_text+text)
        older_text=older_text+text
    def initUI(self):

        self.txt_screen = QtWidgets.QLineEdit(self)
        self.txt_screen.move(150,75)
        self.txt_screen.resize(200,50)
        

        self.lbl_result=QtWidgets.QLabel(self)# print kısmı
        self.lbl_result.move(150,120)
        
        self.btn_1=QtWidgets.QPushButton(self)
        self.btn_1.setText("1")
        self.btn_1.move(150,150)
        self.btn_1.clicked.connect(self.print_screen)

        self.btn_2=QtWidgets.QPushButton(self)
        self.btn_2.setText("2")
        self.btn_2.move(250,150)
        self.btn_2.clicked.connect(self.print_screen)


        self.btn_3=QtWidgets.QPushButton(self)
        self.btn_3.setText("3")
        self.btn_3.move(350,150)
        self.btn_3.clicked.connect(self.print_screen)


        self.btn_4=QtWidgets.QPushButton(self)
        self.btn_4.setText("4")
        self.btn_4.move(150,190)
        self.btn_4.clicked.connect(self.print_screen)


        self.btn_5=QtWidgets.QPushButton(self)
        self.btn_5.setText("5")
        self.btn_5.move(250,190)
        self.btn_5.clicked.connect(self.print_screen)


        self.btn_6=QtWidgets.QPushButton(self)
        self.btn_6.setText("6")
        self.btn_6.move(350,190)
        self.btn_6.clicked.connect(self.print_screen)


        self.btn_7=QtWidgets.QPushButton(self)
        self.btn_7.setText("7")
        self.btn_7.move(150,230)
        self.btn_7.clicked.connect(self.print_screen)


        self.btn_8=QtWidgets.QPushButton(self)
        self.btn_8.setText("8")
        self.btn_8.move(250,230)
        self.btn_8.clicked.connect(self.print_screen)


        self.btn_9=QtWidgets.QPushButton(self)
        self.btn_9.setText("9")
        self.btn_9.move(350,230)
        self.btn_9.clicked.connect(self.print_screen)


        self.btn_0=QtWidgets.QPushButton(self)
        self.btn_0.setText("0")
        self.btn_0.move(150,270)
        self.btn_0.clicked.connect(self.print_screen)


        self.btn_00=QtWidgets.QPushButton(self)
        self.btn_00.setText("00")
        self.btn_00.move(250,270)
        self.btn_00.clicked.connect(self.print_screen)

        self.btn_ca=QtWidgets.QPushButton(self)
        self.btn_ca.setText("*")
        self.btn_ca.move(450,150)
        self.btn_ca.clicked.connect(self.print_screen)

        self.btn_bo=QtWidgets.QPushButton(self)
        self.btn_bo.setText("/")
        self.btn_bo.move(450,190)
        self.btn_bo.clicked.connect(self.print_screen)

        self.btn_ci=QtWidgets.QPushButton(self)
        self.btn_ci.setText("-")
        self.btn_ci.move(450,230)
        self.btn_ci.clicked.connect(self.print_screen)

        self.btn_to=QtWidgets.QPushButton(self)
        self.btn_to.setText("+")
        self.btn_to.move(450,270)
        self.btn_to.clicked.connect(self.print_screen)


        self.btn_hesapla=QtWidgets.QPushButton(self)
        self.btn_hesapla.setText("hesapla")
        self.btn_hesapla.move(350,270)
        self.btn_hesapla.clicked.connect(self.islem)


def window():
    app=QApplication(sys.argv)
    win=MyWindow()
    win.show()
    sys.exit(app.exec_())

window()