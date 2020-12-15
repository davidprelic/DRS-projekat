import threading
from time import sleep

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QLabel


class Player(QLabel):
    def __init__(self, nebitno, grid):
        super().__init__(nebitno)
        # kreiraj player-a
        self.setGeometry(51, 570, 32, 32)
        self.setPixmap(QtGui.QPixmap('Images/bubble_right.png'))
        self.grid = grid
        self.setAccessibleName("player_right")




    # override funkcije keyPress kada kliknem strelice za kretanje
    def keyPressEvent(self, event):
        # provera da li je kliknut key_up i da li je player ispod top border-a
        if event.key() == QtCore.Qt.Key_Up and self.y() >= 60:
            self.move(self.x(), self.y()-5)
        #elif event.key() == QtCore.Qt.Key_Down and self.y() <= 565:
            #self.move(self.x(), self.y() + 5)
        # provera da li je kliknut key_left i da li je player desno od left border-a
        # ako jeste, pomeri ga 5px u levo
        elif event.key() == QtCore.Qt.Key_Left and self.x() >= 56:
            self.setPixmap(QtGui.QPixmap('Images/bubble_left.png'))
            self.setAccessibleName("player_left")
            self.move(self.x() - 5, self.y())

        # provera da li je kliknut key_right i da li je player levo od right border-a
        # ako jeste, pomeri ga 5px u desno
        elif event.key() == QtCore.Qt.Key_Right and self.x() <= 765:
            self.setPixmap(QtGui.QPixmap('Images/bubble_right.png'))
            self.setAccessibleName("player_right")
            self.move(self.x() + 5, self.y())

        # ostale buttone nismo overrideovali
        else:
            QLabel.keyPressEvent(self, event)


