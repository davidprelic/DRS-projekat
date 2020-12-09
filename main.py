import sys
import platform
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Start import *


if __name__ == '__main__':
   app = QApplication([])
   OWindowManager = WindowManager(app)
   sys.exit(app.exec_())