from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot

class MainWindow(QGraphicsScene):
    def __init__(self, startMethodMainWindow, quitMethodMainWindow, parent=None):
        super(MainWindow, self).__init__(parent)

        screenWidth = 840
        screenHeigth = 640

        oImage = QPixmap('Images/first_window_img.jpg')
        sImage = oImage.scaled(QSize(screenWidth, screenHeigth))

        self.graphicsPixmapItem = QGraphicsPixmapItem(sImage)
        self.addItem(self.graphicsPixmapItem)
        self.setSceneRect(0, 0, screenWidth, screenHeigth)





        qbtn = QPushButton()
        qbtn.clicked.connect(quitMethodMainWindow)
        qbtn.setGeometry(350, 400, 200, 50)
        qbtn.setStyleSheet("border-radious")

        qbtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.addWidget(qbtn)

        pbtn = QPushButton()
        pbtn.clicked.connect(startMethodMainWindow)
        pbtn.setGeometry(350, 500, 133, 50)
        pbtn.setStyleSheet("background-color: rgb(255,255,0)")
        pbtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.addWidget(pbtn)

        #self.show()