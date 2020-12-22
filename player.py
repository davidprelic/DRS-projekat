import threading
from time import sleep

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QLabel


class Player(QLabel):
    def __init__(self, nebitno, grid, bullet, x, y, num_of_player):
        super().__init__(nebitno)
        # kreiraj player-a
        self.setGeometry(x, y, 32, 32)
        if num_of_player == 1:
            self.setPixmap(QtGui.QPixmap('Images/bubble_right.png'))
        else:
            self.setPixmap(QtGui.QPixmap('Images/bobble_left.png'))
        self.grid = grid
        self.setAccessibleName("player_right")
        self.bullet = bullet
        self.num_of_player = num_of_player

        self.padanje = True
        self.skok = False
        self.kretanje_levo = False
        self.kretanje_desno = False

    # skok playera -> inicijalno na t.start() se pravi thread koji za 0.01 sec poziva jump funkcija koja pomera playera 5px ka gore
    # zatim se poziva ista funkcija ali ovoga puta ne ulazi u prvi if nego ide u else i upada u petlju koja sleepuje thread na 0.01
    # polje skok sluzi da signalizira da je player u skoku
    # samo se jednom poziva threading.Timer.start() koji kreira novi thread za prosledjenu funkciju
    # da nema provere (if not rekurzija) kreirao bi se novi thread za svaki novi poziv ove funkcije (imalo bi previse threadova)
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

    # padanje playera -> inicijalno na t.start() se pravi thread koji za 0.01 sec poziva fall funkcija koja pomera playera 5px ka dole
    # zatim se poziva ista funkcija ali ovoga puta ne ulazi u prvi if nego ide u else i upada u petlju koja sleepuje thread na 0.01
    # polje padanje sluzi za proveru da li player trenutno pada
    # polje rekurzija sluzi da ignorise polje "padanje" zbog rekurzije
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

    # provera da li je ispod playera platforma, tj da li ce player padati
    # prvo uzimamo donju ivicu playera, zatim uzimam sva polja iz grida
    # zatim filtriram samo polja platforme, pa filtriram samo polja platforme koja su u x osi tacno ispod playera (+-5px)
    # i na kraju od tih polja platforme tacno ispod playera, filtriram samo ona koja su bar delom u ravni playera (y osi)
    # ako ima takvih polja, onda player nece padati i funkcija vraca false
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

    def player_kreci_se_desno(self, rekurzija):
        if not rekurzija:
            t = threading.Timer(0.01, lambda: self.player_kreci_se_desno(True))
            if self.kretanje_desno and self.x() <= 765:
                t.start()
                self.move(self.x() + 5, self.y())
                if not self.skok:
                    self.fall(False)
        else:
            while self.kretanje_desno and self.x() <= 765:
                self.move(self.x() + 5, self.y())
                if not self.skok:
                    self.fall(False)
                sleep(0.01)

    def player_kreci_se_levo(self, rekurzija):
        if not rekurzija:
            t = threading.Timer(0.01, lambda: self.player_kreci_se_levo(True))
            if self.kretanje_levo and self.x() >= 56:
                t.start()
                self.move(self.x() - 5, self.y())
                if not self.skok:
                    self.fall(False)
        else:
            while self.kretanje_levo and self.x() >= 56:
                self.move(self.x() - 5, self.y())
                if not self.skok:
                    self.fall(False)
                sleep(0.01)
