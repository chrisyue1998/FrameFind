# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IntroWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from FaceCaptureWindow import Ui_FaceCaptureWindow

class Ui_MainWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_FaceCaptureWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(621, 364)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(260, 260, 113, 32))
        self.start.setCheckable(False)
        self.start.setObjectName("start")

        self.start.clicked.connect(self.openWindow)

        self.frameFindName = QtWidgets.QLabel(self.centralwidget)
        self.frameFindName.setGeometry(QtCore.QRect(170, 120, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(45)
        self.frameFindName.setFont(font)
        self.frameFindName.setAlignment(QtCore.Qt.AlignCenter)
        self.frameFindName.setObjectName("frameFindName")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.frameFindName.setText(_translate("MainWindow", "FrameFind"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

