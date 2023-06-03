import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from PyQt5.QtGui import QPalette,QColor

class Color(QWidget):
    def __init__(self,color):
        super(Color,self).__init__()
        self.setAutoFillBackground(True)

        palette=self.palette()
        palette.setColor(QPalette.Window, QColor(color))# buyuk kucuk harflere dikkat 

        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__ (self):
        super(MainWindow, self).__init__()
        """
        #layout=QtWidgets.QVBoxLayout()# bu yatayda 
        # layout=QtWidgets.QHBoxLayout()# bu dikeyde sıralar asagı taraf aynı
        # layout.addWidget(Color("red"))
        # layout.addWidget(Color("blue"))
        # layout.addWidget(Color("green"))
        # layout.addWidget(Color("yellow"))
        # widget = QWidget()
        # widget.setLayout(layout)
        """
        """
        # hlayout1=QtWidgets.QHBoxLayout()
        # hlayout1.addWidget(Color("red"))
        # hlayout1.addWidget(Color("blue"))
        # hlayout1.addWidget(Color("green"))

        # hlayout2=QtWidgets.QHBoxLayout()
        # hlayout2.addWidget(Color("red"))
        # hlayout2.addWidget(Color("blue"))

        # vlayout=QtWidgets.QVBoxLayout()
        # vlayout.addLayout(hlayout1)
        # vlayout.addLayout(hlayout2)     

        # widget=QWidget()
        # widget.setLayout(vlayout)   
        """
        """
        layout=QtWidgets.QGridLayout()
        layout.addWidget(Color("red"),0,0)
        layout.addWidget(Color("blue"),1,1)
        layout.addWidget(Color("yellow"),2,2)
        layout.addWidget(Color("orange"),3,3)
        widget=QWidget()
        widget.setLayout(layout)
        """

        h1layout=QtWidgets.QHBoxLayout()
        h1layout.addWidget(QColor("red"))
        h1layout.addWidget(Color("blue"))
        h1layout.addWidget(Color("green"))
        
        #h1layout.setContentsMargins(50,0,50,0)
        h1layout.setSpacing(50)#kolonlar arası mesafe ayarlıyor 
        h2layout=QtWidgets.QHBoxLayout()
        h2layout.addWidget(Color("red"))
        h2layout.addWidget(Color("green"))

        vlayout=QtWidgets.QVBoxLayout()
        vlayout.addLayout(h1layout)
        vlayout.addLayout(h2layout)

        widget=QWidget()
        widget.setLayout(vlayout)
        




        self.setCentralWidget(widget)
        self.setGeometry(100,100,500,500)
def app():
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    sys.exit(app.exec_())

app()