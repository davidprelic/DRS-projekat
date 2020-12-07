import sys
import platform
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PySide2 import QtCore,QtGui,QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *







def window():
   app = QApplication(sys.argv)
   w = QWidget()
   b = QLabel(w)
   b.setText("Hello World!")
   w.setGeometry(100,10,850,650)
   w.move(550,200)
   b.move(50,20)
   w.setWindowTitle("PyQt5")
   w.show()
   sys.exit(app.exec_())


if __name__ == '__main__':
   window()
