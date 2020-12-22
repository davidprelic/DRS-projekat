import threading
from time import sleep

from PyQt5 import QtGui
from PyQt5.QtWidgets import QLabel


class Enemy(QLabel):
    def __init__(self, nebitno, grid, x, y):
        #print(nebitno)
        super().__init__(nebitno)
        # kreiraj enemy-ja
        self.setGeometry(x, y, 32, 32)
        self.setPixmap(QtGui.QPixmap('Images/enemy_left.png'))
        self.grid = grid
        self.setAccessibleName("enemy_left")
        self.padanje = True
        # inicijalno odmah po kreiranju enemija nek krene da se krece levo
        self.enemy_kretnja_levo(False)

    # padanje enemija -> inicijalno na t.start() se pravi thread koji za 0.01 sec poziva fall funkcija koja pomera enemija 5px ka dole
    # zatim se poziva ista funkcija ali ovoga puta ne ulazi u prvi if nego ide u else i upada u petlju koja sleepuje thread na 0.01
    # polje padanje sluzi za proveru da li enemy trenutno pada
    # polje rekurzija sluzi da ignorise polje "padanje" zbog rekurzije
    # samo se jednom poziva threading.Timer.start() koji kreira novi thread za prosledjenu funkciju
    # da nema provere (if not rekurzija) kreirao bi se novi thread za svaki novi poziv ove funkcije (imalo bi previse threadova)
    def fall(self, rekurzija):
        if not rekurzija:
            if self.padanje or rekurzija:
                self.padanje = False
                t = threading.Timer(0.01, lambda: self.fall(True))
                if self.da_li_enemy_pada(self.grid):
                    t.start()
                    self.move(self.x(), self.y() + 5)
                else:
                    self.padanje = True
        else:
            while self.da_li_enemy_pada(self.grid):
                self.move(self.x(), self.y() + 5)
                sleep(0.01)
            self.padanje = True

    # provera da li je ispod enemija platforma, tj da li ce enemy padati
    # prvo uzimamo donju ivicu enemija, zatim uzimam sva polja iz grida
    # zatim filtriram samo polja platforme, pa filtriram samo polja platforme koja su u x osi tacno ispod enemija (+-5px)
    # i na kraju od tih polja platforme tacno ispod enemija, filtriram samo ona koja su bar delom u ravni enemija (y osi)
    # ako ima takvih polja, onda enemy nece padati i funkcija vraca false
    def da_li_enemy_pada(self, grid):
        donja_ivica_enemy = self.y() + self.height()

        items = (grid.itemAt(i) for i in range(grid.count()))
        bricks = []

        for w in items:
            if w.widget().accessibleName() == "brick":
                bricks.append(w.widget())

        bricks_2 = []
        for brick in bricks:
            if brick.y() >= donja_ivica_enemy and brick.y() <= donja_ivica_enemy + 5:
                bricks_2.append(brick)

        leva_ivica_enemy = self.x()
        desna_ivica_enemy = self.x() + self.width()

        brick_konacno = []

        for brick2 in bricks_2:
            if (brick2.x() <= leva_ivica_enemy and ((brick2.x() + brick2.width()) > leva_ivica_enemy)) or (
                    desna_ivica_enemy <= (brick2.x() + brick2.width()) and desna_ivica_enemy >= brick2.x()):
                brick_konacno.append(brick2)
        return len(brick_konacno) == 0




    # enemy ce se kretati levo dok god ne naidje na zid, kad naidje na zid menja sliku u enemy_right i pocinje da ide desno
    # pri svakom pokretu poziva se i fall funkcija kako bi videli dal ispod enemija ima platforme tj dal treba da pada
    # samo se jednom poziva threading.Timer.start() koji kreira novi thread za prosledjenu funkciju
    # da nema provere (if not rekurzija) kreirao bi se novi thread za svaki novi poziv ove funkcije (imalo bi previse threadova)
    def enemy_kretnja_levo(self, rekurzija):
        if not rekurzija:
            t = threading.Timer(0.01, lambda: self.enemy_kretnja_levo(True))
            if self.proveri_zid_levo():
                t.start()
                self.move(self.x() - 5, self.y())
                self.fall(False)

        else:
            while self.proveri_zid_levo():
                self.move(self.x() - 5, self.y())
                self.fall(False)
                sleep(0.01)




    # provera dal se odmah levo od enemija nalazi zid
    # prvo uzimam sve zidove, zatim filtriram sve one levo od njega (od njegove leve ivice)
    # i na kraju filtriram samo onaj zid koji se nalazi odmah levo od njega
    def proveri_zid_levo(self):
        items = (self.grid.itemAt(i) for i in range(self.grid.count()))
        bricks = []

        for w in items:
            if w.widget().accessibleName() == "brick":
                bricks.append(w.widget())

        bricks_2 = []
        for brick in bricks:
            if brick.x() + brick.width() <= self.x() and (brick.x() + brick.width()) >= (self.x() - 5):
                bricks_2.append(brick)

        gornja_ivica_bulleta = self.y()
        donja_ivica_bulleta = self.y() + self.height()
        brick_konacno = []

        for brick2 in bricks_2:
            if (brick2.y() <= gornja_ivica_bulleta and ((brick2.y() + brick2.height()) > gornja_ivica_bulleta)) or (
                    donja_ivica_bulleta <= (brick2.y() + brick2.height()) and donja_ivica_bulleta >= brick2.y()):
                brick_konacno.append(brick2)
                #print(brick2.pos())

        return len(brick_konacno) == 0