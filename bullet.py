import threading
from time import sleep

from PyQt5 import QtGui
from PyQt5.QtWidgets import QLabel


class Bullet(QLabel):
    def __init__(self, nebitno, grid):
        super().__init__(nebitno)
        # kreiraj bullet
        self.setGeometry(51, 570, 32, 32)
        self.setPixmap(QtGui.QPixmap('Images/bubble_ball.png'))
        self.enemies = nebitno.enemies
        self.nebitno = nebitno
        self.game_win = nebitno
        self.dead_enemies = nebitno.dead_enemies
        self.grid = grid
        self.setAccessibleName("bullet")
        self.metak_u_letu = False

    # pucaj levo- > dok god je metak u letu ne moze se kliknuti space odnosno ponovo pucati
    # tek kad funkcija proveri_levo() vrati False onda sakrivam bullet i odobravam novo pucanje
    # samo se jednom poziva threading.Timer.start() koji kreira novi thread za prosledjenu funkciju
    # da nema provere (if not rekurzija) kreirao bi se novi thread za svaki novi poziv ove funkcije (imalo bi previse threadova)
    def shoot_bubble_left(self, rekurzija, index):
        if not rekurzija:
            index = index + 1
            if (not self.metak_u_letu) or rekurzija:
                self.metak_u_letu = True
                t = threading.Timer(0.01, lambda: self.shoot_bubble_left(True, index))
                if self.proveri_levo() and index < 45:
                    t.start()
                    self.move(self.x() - 5, self.y())
                else:
                    self.lower()
                    self.metak_u_letu = False
        else:
            while self.proveri_levo():
                index = index + 1
                if index < 45:
                    self.move(self.x() - 5, self.y())
                    sleep(0.01)
                else:
                    break
            self.lower()
            self.metak_u_letu = False

    # pucaj desno- > dok god je metak u letu ne moze se kliknuti space odnosno ponovo pucati
    # tek kad funkcija proveri_desno() vrati False onda sakrivam bullet i odobravam novo pucanje
    # samo se jednom poziva threading.Timer.start() koji kreira novi thread za prosledjenu funkciju
    # da nema provere (if not rekurzija) kreirao bi se novi thread za svaki novi poziv ove funkcije (imalo bi previse threadova)
    def shoot_bubble_right(self, rekurzija, index):
        if not rekurzija:
            index = index + 1
            if (not self.metak_u_letu) or rekurzija:
                self.metak_u_letu = True
                t = threading.Timer(0.01, lambda: self.shoot_bubble_right(True, index))
                if self.proveri_desno() and index < 45:
                    t.start()
                    self.move(self.x() + 5, self.y())
                else:
                    self.lower()
                    self.metak_u_letu = False
        else:
            while self.proveri_desno():
                index = index + 1
                if index < 45:
                    self.move(self.x() + 5, self.y())
                    sleep(0.01)
                else:
                    break
            self.lower()
            self.metak_u_letu = False

    # uzimam sva polja grida, filtriram samo cigle, zatim filtriram sve cigle koje su u x osi odmah desno uz bullet(+- 5px)
    # i na kraju filtriram samo ciglu koja je u ravni sa bullet-om po y osi
    def proveri_desno(self):
        items = (self.grid.itemAt(i) for i in range(self.grid.count()))

        bricks = []

        for w in items:
            if w.widget().accessibleName() == "brick":
                bricks.append(w.widget())

        enemies_2 = []
        bricks_2 = []

        for brick in bricks:
            if brick.x() >= (self.x() + self.width()) and brick.x() <= (self.x() + self.width()) + 5:
                bricks_2.append(brick)

        for enemy in self.enemies:
            if enemy.x() >= (self.x() + self.width()) and enemy.x() <= (self.x() + self.width()) + 10:
                enemies_2.append(enemy)

        gornja_ivica_bulleta = self.y()
        donja_ivica_bulleta = self.y() + self.height()
        brick_konacno = []

        for brick2 in bricks_2:
            if (brick2.y() <= gornja_ivica_bulleta and ((brick2.y() + brick2.height()) > gornja_ivica_bulleta)) or (
                    donja_ivica_bulleta <= (brick2.y() + brick2.height()) and donja_ivica_bulleta >= brick2.y()):
                brick_konacno.append(brick2)
                #print(brick2.pos())

        enemy_konacno = []

        for enemy in enemies_2:
            if (enemy.y() <= gornja_ivica_bulleta and ((enemy.y() + enemy.height()) > gornja_ivica_bulleta)) or (
                    donja_ivica_bulleta <= (enemy.y() + enemy.height()) and donja_ivica_bulleta >= enemy.y()):
                enemy_konacno.append(enemy)
                # stvori jaje i unisti enemija
                enemy.lower()
                for d_en in self.dead_enemies:
                    if d_en.x() == -100:
                        d_en.move(enemy.x(), enemy.y())
                        d_en.kreni_ka_gore(False)
                        break

                self.enemies.remove(enemy)

        return len(brick_konacno) == 0 and len(enemy_konacno) == 0

    # uzimam sva polja grida, filtriram samo cigle, zatim filtriram sve cigle koje su u x osi odmah levo uz bullet(+- 5px)
    # i na kraju filtriram samo ciglu koja je u ravni sa bullet-om po y osi
    def proveri_levo(self):
        items = (self.grid.itemAt(i) for i in range(self.grid.count()))

        bricks = []

        for w in items:
            if w.widget().accessibleName() == "brick":
                bricks.append(w.widget())

        bricks_2 = []
        enemies_2 = []

        for brick in bricks:
            if brick.x() + brick.width() <= self.x() and (brick.x() + brick.width()) >= (self.x() - 5):
                bricks_2.append(brick)

        for enemy in self.enemies:
            if enemy.x() + enemy.width() <= self.x() and (enemy.x() + enemy.width()) >= (self.x() - 10):
                enemies_2.append(enemy)

        gornja_ivica_bulleta = self.y()
        donja_ivica_bulleta = self.y() + self.height()
        brick_konacno = []

        for brick2 in bricks_2:
            if (brick2.y() <= gornja_ivica_bulleta and ((brick2.y() + brick2.height()) > gornja_ivica_bulleta)) or (
                    donja_ivica_bulleta <= (brick2.y() + brick2.height()) and donja_ivica_bulleta >= brick2.y()):
                brick_konacno.append(brick2)
                #print(brick2.pos())

        enemy_konacno = []

        for enemy in enemies_2:
            if (enemy.y() <= gornja_ivica_bulleta and ((enemy.y() + enemy.height()) > gornja_ivica_bulleta)) or (
                    donja_ivica_bulleta <= (enemy.y() + enemy.height()) and donja_ivica_bulleta >= enemy.y()):
                enemy_konacno.append(enemy)
                # stvori jaje i unisti enemija
                enemy.lower()
                for d_en in self.dead_enemies:
                    if d_en.x() == -100:
                        d_en.move(enemy.x(), enemy.y())
                        d_en.kreni_ka_gore(False)
                        break

                self.enemies.remove(enemy)

        return len(brick_konacno) == 0 and len(enemy_konacno) == 0
