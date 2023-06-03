from PyQt5 import QtWidgets
import sys
from cal import Ui_MainWindow

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__() 
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_to.clicked.connect(self.islem)
        self.ui.btn_bo.clicked.connect(self.islem)
        self.ui.btn_ca.clicked.connect(self.islem)
        self.ui.btn_ci.clicked.connect(self.islem)

    def islem(self):
        buton=self.sender()
        text = buton.text()
        s1=int(self.ui.txt_1.text())
        s2=int(self.ui.txt_2.text())
        if text=="topla":
            result=s1+s2
        elif text=="cıkar":
            result=s1-s2
        elif text=="carp":
            result=s1*s2
        elif text=="bol":
            result=s1/s2


        self.ui.lbl_result.setText(str(result))
def window():
    app=QtWidgets.QApplication(sys.argv)
    win=MyApp()
    win.show()
    sys.exit(app.exec_())

window()