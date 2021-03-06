# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OvalFaceFrames.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint


class Ui_OvalFaceFrames(object):
    def setupUi(self, OvalFaceFrames):
        OvalFaceFrames.setObjectName("OvalFaceFrames")
        OvalFaceFrames.resize(720, 631)
        self.faceShapeText = QtWidgets.QLabel(OvalFaceFrames)
        self.faceShapeText.setGeometry(QtCore.QRect(160, 20, 411, 111))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.faceShapeText.setFont(font)
        self.faceShapeText.setAlignment(QtCore.Qt.AlignCenter)
        self.faceShapeText.setObjectName("faceShapeText")
        self.imageFrame = QtWidgets.QLabel(OvalFaceFrames)
        self.imageFrame.setGeometry(QtCore.QRect(160, 140, 411, 281))
        self.imageFrame.setText("")
        self.imageFrame.setObjectName("imageFrame")
        self.pixmap = QtGui.QPixmap('ovalface0.jpg')
        self.pixmap = self.pixmap.scaledToWidth(411, QtCore.Qt.FastTransformation)
        self.imageFrame.setPixmap(self.pixmap)
        self.imageFrame.resize(self.pixmap.width(), self.pixmap.height())
        self.shuffleButton = QtWidgets.QPushButton(OvalFaceFrames)
        self.shuffleButton.setGeometry(QtCore.QRect(150, 550, 431, 32))
        self.shuffleButton.setObjectName("shuffleButton")
        self.linkDesc = QtWidgets.QLabel(OvalFaceFrames)
        self.linkDesc.setGeometry(QtCore.QRect(170, 470, 111, 16))
        self.linkDesc.setObjectName("linkDesc")
        self.purchaseLink = QtWidgets.QLabel(OvalFaceFrames)
        self.purchaseLink.setGeometry(QtCore.QRect(280, 470, 281, 16))
        self.purchaseLink.setText("")
        self.purchaseLink.setObjectName("purchaseLink")
        self.purchaseLink.setOpenExternalLinks(True)
        url = "<a href=\"https://www.vintandyork.com/sky-703.html\">Go To Website</a>"
        self.purchaseLink.setText(url)

        self.index = rand_index(5)
        self.shuffleButton.clicked.connect(self.shuffle_on_click)

        self.retranslateUi(OvalFaceFrames)
        QtCore.QMetaObject.connectSlotsByName(OvalFaceFrames)

    def retranslateUi(self, OvalFaceFrames):
        _translate = QtCore.QCoreApplication.translate
        OvalFaceFrames.setWindowTitle(_translate("OvalFaceFrames", "Dialog"))
        self.faceShapeText.setText(_translate("OvalFaceFrames", "You are closest to an oval face"))
        self.shuffleButton.setText(_translate("OvalFaceFrames", "Shuffle"))
        self.linkDesc.setText(_translate("OvalFaceFrames", "Link to purchase:"))

    def shuffle_on_click(self):
        index = self.index.rand()
        self.pixmap = QtGui.QPixmap('ovalface' + str(index) + '.jpg')
        self.pixmap = self.pixmap.scaledToWidth(411, QtCore.Qt.FastTransformation)
        self.imageFrame.setPixmap(self.pixmap)
        self.imageFrame.resize(self.pixmap.width(), self.pixmap.height())
        if index == 0:
            url = "<a href=\"https://www.vintandyork.com/sky-703.html\">Go To Website</a>"
            self.purchaseLink.setText(url)
        elif index == 1:
            url = "<a href=\"https://www.firmoo.com/eyeglasses-p-5541.html\">Go To Website</a>"
            self.purchaseLink.setText(url)
        elif index == 2:
            url = "<a href=\"https://www.clearly.ca/glasses/ray-ban/ray-ban-rx5287?v=black-transparent\">" \
                  "Go To Website</a>"
            self.purchaseLink.setText(url)
        elif index == 3:
            url = "<a href=\"https://www.fetcheyewear.com/product/riley-collection/GreyHorn/designer-glasses\">" \
                  "Go To Website</a>"
            self.purchaseLink.setText(url)
        else:
            url = "<a href=\"https://www.glassesusa.com/gunmetal-large/leo/31-h10009.html\">Go To Website</a>"
            self.purchaseLink.setText(url)


class rand_index(object):
    def __init__(self, lst_len):
        self.visited = []
        self.lst_len = lst_len
        self.last_index = None

    def rand(self):
        if len(self.visited) == self.lst_len:
            self.visited = [self.last_index]

        index = randint(0, self.lst_len - 1)

        while index in self.visited:
            index = randint(0, self.lst_len - 1)

        self.last_index = index

        self.visited.append(index)

        return index


def run():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OvalFaceFrames = QtWidgets.QDialog()
    ui = Ui_OvalFaceFrames()
    ui.setupUi(OvalFaceFrames)
    OvalFaceFrames.show()
    sys.exit(app.exec_())

