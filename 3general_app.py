from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip
import sys
from PyQt5.QtGui import QIcon

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("first application")
        self.setGeometry(200,200,700,700)
        self.setWindowIcon(QIcon("icon.png"))
        self.setToolTip("my tooltip")
        self.initUI()
    def initUI(self):
        self.lbl_name=QtWidgets.QLabel(self)
        self.lbl_name.setText("adınız:")
        self.lbl_name.move(50,30)
        
        self.lbl_surname=QtWidgets.QLabel(self)
        self.lbl_surname.setText("surname:")
        self.lbl_surname.move(50,70)

        self.txt_name=QtWidgets.QLineEdit(self)
        self.txt_name.move(150,30)
        self.txt_name.resize(200,32)

        self.txt_surname=QtWidgets.QLineEdit(self)
        self.txt_surname.move(150,70)
        self.txt_surname.resize(200,32)

        self.lbl_result=QtWidgets.QLabel(self)
        self.lbl_result.move(50,180)


        self.btn_save=QtWidgets.QPushButton(self)   
        self.btn_save.setText("Save")
        self.btn_save.move(50,150)
        self.btn_save.clicked.connect(self.cliced)
    def cliced(self):
        self.lbl_result.setText("ad "+ self.txt_name.text() +" surname: "+ self.txt_surname.text())        

def window():
    app=QApplication(sys.argv)#pencereyi olusturmak için
    win=MyWindow()#pencereyi olusturmak için

   
    win.show()
    sys.exit(app.exec_())
window()

