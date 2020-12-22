import threading
from time import sleep

from PyQt5 import QtGui
from PyQt5.QtWidgets import QLabel


class DeadEnemy(QLabel):
    def __init__(self, nebitno, grid, x, y):
        #print(nebitno)
        super().__init__(nebitno)
        # kreiraj DeadEnemy-ja
        self.setGeometry(x, y, 32, 32)
        self.setPixmap(QtGui.QPixmap('Images/dead_enemy.png'))
        self.grid = grid
        self.padanje = True
        # inicijalno odmah po kreiranju dead_enemija nek krene da se krece ka gore
        #self.enemy_kretnja_levo(False)

    def kreni_ka_gore(self, rekurzija):
        if not rekurzija:
            t = threading.Timer(0.05, lambda: self.kreni_ka_gore(True))
            t.start()
            if self.y() >= 52:
                self.move(self.x(), self.y() - 5)
        else:
            while self.y() >= 52:
                self.move(self.x(), self.y() - 5)
                sleep(0.05)
