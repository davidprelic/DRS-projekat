# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

def quit_clicked():
    print("Clicked quit")
    sys.exit()

def play1_clicked():
    print("Clicked play1")
    # neka akcija

def play2_clicked():
    print("Clicked play2")
    #neka akcija

class Ui_MainWindow(object):
    def __init__(self, quitMethodMainWindow, parent=None):
        super(Ui_MainWindow, self).__init__(parent)

        self.setupUi(self, Ui_MainWindow)
        self.retranslateUi(self, Ui_MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QtCore.QSize(850, 650))
        self.centralwidget.setMaximumSize(QtCore.QSize(850, 650))
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 850, 650))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(-30, -10, 921, 681))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/first_window_img.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 280, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Bubble Bobble")
        font.setPointSize(32)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 0);\n"
"color:rgb(255, 0, 155);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-radius:25px;\n"
"border-color:rgb(255, 0, 155);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"background-color: rgb(255, 0, 155);\n"
"color: rgb(255, 255, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-radius:25px;\n"
"border-color:rgb(255, 255, 0);\n"
"padding:6px\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")




        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 520, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Bubble Bobble")
        font.setPointSize(32)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 0);\n"
"color:rgb(255, 0, 155);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-radius:25px;\n"
"border-color:rgb(255, 0, 155);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"background-color: rgb(255, 0, 155);\n"
"color: rgb(255, 255, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-radius:25px;\n"
"border-color:rgb(255, 255, 0);\n"
"padding:6px\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(quit_clicked)


        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(320, 400, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Bubble Bobble")
        font.setPointSize(32)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 0);\n"
"color:rgb(255, 0, 155);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-radius:25px;\n"
"border-color:rgb(255, 0, 155);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"background-color: rgb(255, 0, 155);\n"
"color: rgb(255, 255, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border-radius:25px;\n"
"border-color:rgb(255, 255, 0);\n"
"padding:6px\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")



        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "Single"))
        self.pushButton_4.setText(_translate("MainWindow", "Quit"))
        self.pushButton_5.setText(_translate("MainWindow", "Multiplayer"))

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
'''