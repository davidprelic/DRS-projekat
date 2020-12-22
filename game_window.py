from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDesktopWidget, QWidget, QGridLayout, QMainWindow, QLabel

from bullet import Bullet
from enemy import Enemy
from player import Player


class GameWindow(QMainWindow):
    def __init__(self, broj_playera):
        super().__init__()

        self.num_of_players = broj_playera
        self.initUI()

    def initUI(self):

        self.win = QWidget()
        self.setCentralWidget(self.win)
        grid = QGridLayout()
        # inicijalno napravi grid 15*20 i svakom polju grida dodaj labelu koja ima black background
        for i in range(0, 15):
            for j in range(0, 20):
                label = QLabel(self)
                label.setStyleSheet("background-color: black;")
                grid.addWidget(label, i, j)
        # border left
        for i in range(0, 15):
            label = QLabel(self)
            pixmap = QPixmap('Images/brick.png')
            label.setPixmap(pixmap)
            self.resize(pixmap.width(), pixmap.height())
            label.setScaledContents(True)
            label.setAccessibleName("brick")
            grid.addWidget(label, i, 0)
        # border top
        for i in range(0, 20):
            label = QLabel(self)
            pixmap = QPixmap('Images/brick.png')
            label.setPixmap(pixmap)
            self.resize(pixmap.width(), pixmap.height())
            label.setScaledContents(True)
            label.setAccessibleName("brick")
            grid.addWidget(label, 0, i)
        # border bottom
        for i in range(0, 20):
            label = QLabel(self)
            pixmap = QPixmap('Images/brick.png')
            label.setPixmap(pixmap)
            self.resize(pixmap.width(), pixmap.height())
            label.setScaledContents(True)
            label.setAccessibleName("brick")
            grid.addWidget(label, 14, i)
        # border right
        for i in range(0, 15):
            label = QLabel(self)
            pixmap = QPixmap('Images/brick.png')
            label.setPixmap(pixmap)
            self.resize(pixmap.width(), pixmap.height())
            label.setScaledContents(True)
            label.setAccessibleName("brick")
            grid.addWidget(label, i, 19)
        # platform
        label = QLabel(self)
        pixmap = QPixmap('Images/brick.png')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
        label.setScaledContents(True)
        label.setAccessibleName("brick")
        grid.addWidget(label, 5, 8)
        # platform
        for i in range(8):
            label = QLabel(self)
            pixmap = QPixmap('Images/brick.png')
            label.setPixmap(pixmap)
            self.resize(pixmap.width(), pixmap.height())
            label.setScaledContents(True)
            label.setAccessibleName("brick")
            grid.addWidget(label, 2, i + 6)
        # platform
        for i in range(4):
            label = QLabel(self)
            pixmap = QPixmap('Images/brick.png')
            label.setPixmap(pixmap)
            self.resize(pixmap.width(), pixmap.height())
            label.setScaledContents(True)
            label.setAccessibleName("brick")
            grid.addWidget(label, 5, i + 11)
        # platform
        for i in range(15):
            label = QLabel(self)
            pixmap = QPixmap('Images/brick.png')
            label.setPixmap(pixmap)
            self.resize(pixmap.width(), pixmap.height())
            label.setScaledContents(True)
            label.setAccessibleName("brick")
            grid.addWidget(label, 11, i + 4)
        # platform
        for i in range(8):
            label = QLabel(self)
            pixmap = QPixmap('Images/brick.png')
            label.setPixmap(pixmap)
            self.resize(pixmap.width(), pixmap.height())
            label.setScaledContents(True)
            label.setAccessibleName("brick")
            grid.addWidget(label, 8, i + 1)

        # setuj grid u okviru layout-a prozora i kreiraj sam prozor
        self.win.setLayout(grid)
        self.setWindowTitle("Bubble Bobble")
        self.setGeometry(100, 100, 850, 650)
        # da nema ovoga videla bi se mreza
        self.setStyleSheet("background-color: black;")
        self.enemies = []
        self.enemies.append(Enemy(self, grid, 400, 50))
        self.enemies.append(Enemy(self, grid, 450, 50))
        self.bullet1 = Bullet(self, grid)
        #self.bullet.raise_()
        # sakrij bullet widget na iza nekog drugog widget-a na njegovoj poziciji
        self.bullet1.lower()

        self.bullet2 = Bullet(self, grid)
        # self.bullet.raise_()
        # sakrij bullet widget na iza nekog drugog widget-a na njegovoj poziciji
        self.bullet2.lower()


        # kreiraj player-a i prosledi mu grid zbog funkcija koje koristi i u kojima ce koristiti grid polja
        self.player1 = Player(self, grid, self.bullet1, 51, 570, 1)

        if self.num_of_players == 2:
            self.player2 = Player(self, grid, self.bullet2, 735, 570, 2)

        #self.player1.setFocus()
        #self.player2.setFocus()

        # centriraj window i prikazi ga
        self.center()
        self.show()

    # kad ugasim aplikaciju rucno obrisi sve pokrenute procese(threadove) od enemyja
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        print("asdasd")
        for enemy in self.enemies:
            enemy.deleteLater()

    # centriranje windowa
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # def kreiraj_missed_bullet(self, grid, x, y ):
        # mb = MissedBullet(self, grid, x, y)

    def keyPressEvent(self, event):
        # provera da li je kliknut key_up i da li je player ispod top border-a
        # ako jeste, izvrsi funkciju jump
        if event.key() == QtCore.Qt.Key_Up and self.player1.y() >= 60:
            if not event.isAutoRepeat():
                if not self.player1.skok and self.player1.padanje:
                    self.player1.jump(0, False)
        #elif event.key() == QtCore.Qt.Key_Down and self.y() <= 565:
            #self.move(self.x(), self.y() + 5)
        # provera da li je kliknut key_left i da li je player desno od left border-a
        # ako jeste, pomeri ga 5px u levo pa proveri ako trenutno nije u skoku dal treba da pada
        elif event.key() == QtCore.Qt.Key_Left:
            if not event.isAutoRepeat():
                self.player1.setPixmap(QtGui.QPixmap('Images/bubble_left.png'))
                self.player1.setAccessibleName("player_left")
                self.player1.kretanje_levo = True
                self.player1.player_kreci_se_levo(False)

        # provera da li je kliknut key_right i da li je player levo od right border-a
        # ako jeste, pomeri ga 5px u desno pa proveri ako trenutno nije u skoku dal treba da pada
        elif event.key() == QtCore.Qt.Key_Right:
            if not event.isAutoRepeat():
                self.player1.setPixmap(QtGui.QPixmap('Images/bubble_right.png'))
                self.player1.setAccessibleName("player_right")
                self.player1.kretanje_desno = True
                self.player1.player_kreci_se_desno(False)

        # provera da li je kliknut key_space i da li je player okrenut levo ili desno
        elif event.key() == QtCore.Qt.Key_Space:
            if not event.isAutoRepeat():
                if not self.player1.bullet.metak_u_letu:
                    self.player1.bullet.setGeometry(self.player1.x(), self.player1.y(), 32, 32)
                    self.player1.bullet.raise_()
                    self.player1.raise_()

            if self.player1.accessibleName() == "player_right":
                self.player1.bullet.shoot_bubble_right(False, 0)
            else:
                self.player1.bullet.shoot_bubble_left(False, 0)

        # ostale buttone nismo overrideovali
        #else:
            #QLabel.keyPressEvent(self, event)
        if self.num_of_players == 2:
            if event.key() == QtCore.Qt.Key_W and self.player2.y() >= 60:
                if not event.isAutoRepeat():
                    if not self.player2.skok and self.player2.padanje:
                        self.player2.jump(0, False)
            elif event.key() == QtCore.Qt.Key_A:
                if not event.isAutoRepeat():
                    self.player2.setPixmap(QtGui.QPixmap('Images/bobble_left.png'))
                    self.player2.setAccessibleName("player_left")
                    self.player2.kretanje_levo = True
                    self.player2.player_kreci_se_levo(False)
            elif event.key() == QtCore.Qt.Key_D:
                if not event.isAutoRepeat():
                    self.player2.setPixmap(QtGui.QPixmap('Images/bobble_right.png'))
                    self.player2.setAccessibleName("player_right")
                    self.player2.kretanje_desno = True
                    self.player2.player_kreci_se_desno(False)
            elif event.key() == QtCore.Qt.Key_Control:
                if not event.isAutoRepeat():
                    if not self.player2.bullet.metak_u_letu:
                        self.player2.bullet.setGeometry(self.player2.x(), self.player2.y(), 32, 32)
                        self.player2.bullet.raise_()
                        self.player2.raise_()

                    if self.player2.accessibleName() == "player_right":
                        self.player2.bullet.shoot_bubble_right(False, 0)
                    else:
                        self.player2.bullet.shoot_bubble_left(False, 0)

            if event.key() == QtCore.Qt.Key_P:
                if not event.isAutoRepeat():
                    print("pritisnut P")
            if event.key() == QtCore.Qt.Key_O:
                if not event.isAutoRepeat():
                    print("pritisnut O")
            # ostale buttone nismo overrideovali
            #else:
                #QLabel.keyPressEvent(self, event)

    def keyReleaseEvent(self, event):
        if event.key() == QtCore.Qt.Key_Left:
            if not event.isAutoRepeat():
                self.player1.kretanje_levo = False
        if event.key() == QtCore.Qt.Key_Right:
            if not event.isAutoRepeat():
                self.player1.kretanje_desno = False

        if self.num_of_players == 2:
            if event.key() == QtCore.Qt.Key_A:
                if not event.isAutoRepeat():
                    self.player2.kretanje_levo = False
            if event.key() == QtCore.Qt.Key_D:
                if not event.isAutoRepeat():
                    self.player2.kretanje_desno = False
