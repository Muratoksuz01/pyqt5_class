from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip
import sys
from PyQt5.QtGui import QIcon

def window():
    app=QApplication(sys.argv)#pencereyi olusturmak için
    win=QMainWindow()#pencereyi olusturmak için

    win.setWindowTitle("first application")
    win.setGeometry(200,200,700,700)
    win.setWindowIcon(QIcon("icon.png"))
    win.setToolTip("my tooltip")# fare ustune geldiğinde yazı geliyor  app in
    lbl_name=QtWidgets.QLabel(win)
    lbl_name.setText("adınız:")
    lbl_name.move(50,30)
    
    lbl_surname=QtWidgets.QLabel(win)
    lbl_surname.setText("surname:")
    lbl_surname.move(50,70)

    txt_name=QtWidgets.QLineEdit(win)
    txt_name.move(150,30)

    txt_surname=QtWidgets.QLineEdit(win)
    txt_surname.move(150,70)
    def cliced(self):
        print("tıklnadı"+"name "+txt_name.text()+"surname "+txt_surname.text())
    btn_save=QtWidgets.QPushButton(win)
    btn_save.setText("Save")
    btn_save.move(50,150)
    btn_save.clicked.connect(cliced)



    win.show()
    sys.exit(app.exec_())
window()

