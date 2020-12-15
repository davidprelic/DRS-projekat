from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDesktopWidget, QWidget, QGridLayout, QMainWindow, QLabel

from player import Player


class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.win = QWidget()
        self.setCentralWidget(self.win)
        grid = QGridLayout()

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
        self.setStyleSheet("background-color: black;")
        self.player = Player(self, grid)
        self.player.setFocus()

        # centriraj window i prikazi ga
        self.center()
        self.show()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        print("asdasd")

    # centriranje windowa
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

