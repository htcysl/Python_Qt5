import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication

class Mainwindow(QDialog):
    def __init__(self):
        super(Mainwindow, self).__init__()
        loadUi("screen1.ui", self)
        self.button1.clicked.connect(self.gotoScreen2)

    def gotoScreen2(self):
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Screen2(QDialog):
    def __init__(self):
        super(Screen2, self).__init__()
        loadUi("screen2.ui", self)
        self.button2.clicked.connect(self.gotoscreen1)

    def gotoscreen1(self):
        w = Mainwindow()
        widget.addWidget(w)
        widget.setCurrentIndex(widget.currentIndex()+1)

# main
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
w = Mainwindow()
screen2 = Screen2()
widget.addWidget(w)
widget.setFixedHeight(300)
widget.setFixedWidth(400)
widget.show()


try:
    sys.exit(app.exec_())
except:
    print("Exiting")