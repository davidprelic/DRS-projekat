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

        self.padanje = True
        self.skok = False

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Up and self.y() >= 60:
            if not self.skok and self.padanje:
                self.jump(0, False)
        #elif event.key() == QtCore.Qt.Key_Down and self.y() <= 565:
            #self.move(self.x(), self.y() + 5)
        elif event.key() == QtCore.Qt.Key_Left and self.x() >= 56:
            self.setPixmap(QtGui.QPixmap('Images/bubble_left.png'))
            self.setAccessibleName("player_left")
            self.move(self.x() - 5, self.y())
            if not self.skok:
                self.fall(False)
        elif event.key() == QtCore.Qt.Key_Right and self.x() <= 765:
            self.setPixmap(QtGui.QPixmap('Images/bubble_right.png'))
            self.setAccessibleName("player_right")
            self.move(self.x() + 5, self.y())
            if not self.skok:
                self.fall(False)
        else:
            QLabel.keyPressEvent(self, event)

    def jump(self, index, rekurzija):
        if not rekurzija:
            self.skok = True
            index = index + 1
            t = threading.Timer(0.01, lambda: self.jump(index, True))
            if index < 35:
                t.start()
                if self.y() >= 50:
                    self.move(self.x(), self.y() - 5)
            else:
                self.fall(False)
                self.skok = False
        else:
            while index < 35:
                index = index + 1
                if self.y() >= 50:
                    self.move(self.x(), self.y() - 5)
                    sleep(0.01)
            self.fall(False)
            self.skok = False

    def fall(self, rekurzija):
        if not rekurzija:
            if self.padanje or rekurzija:
                self.padanje = False
                t = threading.Timer(0.01, lambda: self.fall(True))
                if self.da_li_igrac_pada(self.grid):
                    t.start()
                    self.move(self.x(), self.y() + 5)
                else:
                    self.padanje = True
        else:
            while self.da_li_igrac_pada(self.grid):
                self.move(self.x(), self.y() + 5)
                sleep(0.01)
            self.padanje = True

    def da_li_igrac_pada(self, grid):
        donja_ivica_playera = self.y() + self.height()

        items = (grid.itemAt(i) for i in range(grid.count()))
        bricks = []

        for w in items:
            if w.widget().accessibleName() == "brick":
                bricks.append(w.widget())

        bricks_2 = []
        for brick in bricks:
            if brick.y() >= donja_ivica_playera and brick.y() <= donja_ivica_playera + 5:
                bricks_2.append(brick)

        leva_ivica_playera = self.x()
        desna_ivica_playera = self.x() + self.width()

        brick_konacno = []

        for brick2 in bricks_2:
            if (brick2.x() <= leva_ivica_playera and ((brick2.x() + brick2.width()) > leva_ivica_playera)) or (
                    desna_ivica_playera <= (brick2.x() + brick2.width()) and desna_ivica_playera >= brick2.x()):
                brick_konacno.append(brick2)
        return len(brick_konacno) == 0