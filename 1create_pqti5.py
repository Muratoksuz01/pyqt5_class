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



    win.show()
    sys.exit(app.exec_())
window()

