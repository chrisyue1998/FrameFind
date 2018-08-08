# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SquareFaceFrames.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint


class Ui_SquareFaceFrames(object):
    def setupUi(self, SquareFaceFrames):
        SquareFaceFrames.setObjectName("SquareFaceFrames")
        SquareFaceFrames.resize(720, 631)
        self.faceShapeText = QtWidgets.QLabel(SquareFaceFrames)
        self.faceShapeText.setGeometry(QtCore.QRect(160, 20, 411, 111))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.faceShapeText.setFont(font)
        self.faceShapeText.setAlignment(QtCore.Qt.AlignCenter)
        self.faceShapeText.setObjectName("faceShapeText")
        self.imageFrame = QtWidgets.QLabel(SquareFaceFrames)
        self.imageFrame.setGeometry(QtCore.QRect(160, 140, 411, 281))
        self.imageFrame.setText("")
        self.imageFrame.setObjectName("imageFrame")
        self.pixmap = QtGui.QPixmap('squareface0.jpg')
        self.pixmap = self.pixmap.scaledToWidth(411, QtCore.Qt.FastTransformation)
        self.imageFrame.setPixmap(self.pixmap)
        self.imageFrame.resize(self.pixmap.width(), self.pixmap.height())
        self.shuffleButton = QtWidgets.QPushButton(SquareFaceFrames)
        self.shuffleButton.setGeometry(QtCore.QRect(150, 550, 431, 32))
        self.shuffleButton.setObjectName("shuffleButton")
        self.linkDesc = QtWidgets.QLabel(SquareFaceFrames)
        self.linkDesc.setGeometry(QtCore.QRect(170, 470, 111, 16))
        self.linkDesc.setObjectName("linkDesc")
        self.purchaseLink = QtWidgets.QLabel(SquareFaceFrames)
        self.purchaseLink.setGeometry(QtCore.QRect(280, 470, 281, 16))
        self.purchaseLink.setText("")
        self.purchaseLink.setObjectName("purchaseLink")
        self.purchaseLink.setOpenExternalLinks(True)
        url = "<a href=\"https://www.vintandyork.com/big-timer-573.html\">Go To Website</a>"
        self.purchaseLink.setText(url)

        self.index = rand_index(5)
        self.shuffleButton.clicked.connect(self.shuffle_on_click)

        self.retranslateUi(SquareFaceFrames)
        QtCore.QMetaObject.connectSlotsByName(SquareFaceFrames)

    def retranslateUi(self, SquareFaceFrames):
        _translate = QtCore.QCoreApplication.translate
        SquareFaceFrames.setWindowTitle(_translate("SquareFaceFrames", "Dialog"))
        self.faceShapeText.setText(_translate("SquareFaceFrames", "You are closest to a square face"))
        self.shuffleButton.setText(_translate("SquareFaceFrames", "Shuffle"))
        self.linkDesc.setText(_translate("SquareFaceFrames", "Link to purchase:"))

    def shuffle_on_click(self):
        index = self.index.rand()
        self.pixmap = QtGui.QPixmap('squareface' + str(index) + '.jpg')
        self.pixmap = self.pixmap.scaledToWidth(411, QtCore.Qt.FastTransformation)
        self.imageFrame.setPixmap(self.pixmap)
        self.imageFrame.resize(self.pixmap.width(), self.pixmap.height())
        if index == 0:
            url = "<a href=\"https://www.gucci.com/us/en/pr/men/mens-accessories/mens-eyewear/mens-sunglasses/" \
                  "mens-round-oval/round-frame-metal-glasses-p-494332I33308880\">Go To Website</a>"
            self.purchaseLink.setText(url)
        elif index == 1:
            url = "<a href=\"https://www.vintandyork.com/big-timer-573.html\">Go To Website</a>"
            self.purchaseLink.setText(url)
        elif index == 2:
            url = "<a href=\"https://www.zennioptical.com/p/womens-oval-eyeglass-frames-/78104?skuId=7810423\">" \
                  "Go To Website</a>"
            self.purchaseLink.setText(url)
        elif index == 3:
            url = "<a href=\"https://www.lenscrafters.com/lc-us/burberry/8053672806571\">Go To Website</a>"
            self.purchaseLink.setText(url)
        else:
            url = "<a href=\"https://www.39dollarglasses.com/9330_BLACK.html\">Go To Website</a>"
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
    SquareFaceFrames = QtWidgets.QDialog()
    ui = Ui_SquareFaceFrames()
    ui.setupUi(SquareFaceFrames)
    SquareFaceFrames.show()
    sys.exit(app.exec_())

