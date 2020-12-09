from PyQt5 import QtWidgets, QtGui, QtCore
import sys
from initialWindow import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class WindowManager(QMainWindow):
    def __init__(self, app):
        super(WindowManager, self).__init__()
        self.setGeometry(0, 0, 850, 650)
        self.setWindowTitle("Bubble Bobble")

        self.app = app
        self.mainWindowScene = MainWindow(self.startMethod,  self.quitMethod)
        self.changeViewMethod(QGraphicsView(self.mainWindowScene))
        self.show()


    def changeViewMethod(self, view):
        self.setCentralWidget(view)

    def startMethod(self):
           print("sadas")

    def quitMethod(self):
        sys.exit(self.app.exec_())



