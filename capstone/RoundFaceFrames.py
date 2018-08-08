# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RoundFaceFrames.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint


class Ui_RoundFaceFrames(object):
    def setupUi(self, RoundFaceFrames):
        RoundFaceFrames.setObjectName("RoundFaceFrames")
        RoundFaceFrames.resize(720, 631)
        self.faceShapeText = QtWidgets.QLabel(RoundFaceFrames)
        self.faceShapeText.setGeometry(QtCore.QRect(160, 20, 411, 111))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.faceShapeText.setFont(font)
        self.faceShapeText.setAlignment(QtCore.Qt.AlignCenter)
        self.faceShapeText.setObjectName("faceShapeText")
        self.imageFrame = QtWidgets.QLabel(RoundFaceFrames)
        self.imageFrame.setGeometry(QtCore.QRect(160, 140, 411, 281))
        self.imageFrame.setText("")
        self.imageFrame.setObjectName("imageFrame")
        self.pixmap = QtGui.QPixmap('roundface0.jpg')
        self.pixmap = self.pixmap.scaledToWidth(411, QtCore.Qt.FastTransformation)
        self.imageFrame.setPixmap(self.pixmap)
        self.imageFrame.resize(self.pixmap.width(), self.pixmap.height())
        self.shuffleButton = QtWidgets.QPushButton(RoundFaceFrames)
        self.shuffleButton.setGeometry(QtCore.QRect(150, 550, 431, 32))
        self.shuffleButton.setObjectName("shuffleButton")
        self.linkDesc = QtWidgets.QLabel(RoundFaceFrames)
        self.linkDesc.setGeometry(QtCore.QRect(170, 470, 111, 16))
        self.linkDesc.setObjectName("linkDesc")
        self.purchaseLink = QtWidgets.QLabel(RoundFaceFrames)
        self.purchaseLink.setGeometry(QtCore.QRect(280, 470, 281, 16))
        self.purchaseLink.setText("")
        self.purchaseLink.setObjectName("purchaseLink")
        self.purchaseLink.setOpenExternalLinks(True)
        url = "<a href=\"https://www.39dollarglasses.com/3125_BLACK.html\">Go To Website</a>"
        self.purchaseLink.setText(url)

        self.index = rand_index(5)
        self.shuffleButton.clicked.connect(self.shuffle_on_click)

        self.retranslateUi(RoundFaceFrames)
        QtCore.QMetaObject.connectSlotsByName(RoundFaceFrames)

    def retranslateUi(self, RoundFaceFrames):
        _translate = QtCore.QCoreApplication.translate
        RoundFaceFrames.setWindowTitle(_translate("RoundFaceFrames", "Dialog"))
        self.faceShapeText.setText(_translate("RoundFaceFrames", "You are closest to a round face"))
        self.shuffleButton.setText(_translate("RoundFaceFrames", "Shuffle"))
        self.linkDesc.setText(_translate("RoundFaceFrames", "Link to purchase:"))

    def shuffle_on_click(self):
        index = self.index.rand()
        self.pixmap = QtGui.QPixmap('roundface' + str(index) + '.jpg')
        self.pixmap = self.pixmap.scaledToWidth(411, QtCore.Qt.FastTransformation)
        self.imageFrame.setPixmap(self.pixmap)
        self.imageFrame.resize(self.pixmap.width(), self.pixmap.height())
        if index == 0:
            url = "<a href=\"https://www.39dollarglasses.com/3125_BLACK.html\">Go To Website</a>"
            self.purchaseLink.setText(url)
        elif index == 1:
            url = "<a href=\"https://www.coastal.com/glasses/ray-ban/ray-ban-rx5287?v=black-transparent\">" \
                  "Go To Website</a>"
            self.purchaseLink.setText(url)
        elif index == 2:
            url = "<a href=\"https://www.zennioptical.com/p/womens-oval-eyeglass-frames-/78104?skuId=7810423\">" \
                  "Go To Website</a>"
            self.purchaseLink.setText(url)
        elif index == 3:
            url = "<a href=\"https://www.firmoo.com/eyeglasses-p-5429.html\">Go To Website</a>"
            self.purchaseLink.setText(url)
        else:
            url = "<a href=\"https://www.glassesusa.com/black-medium/oslo/" \
                  "31-p10356.html?gclid=CjwKCAjww6XXBRByEiwAM-ZUIDq1ErIXXTYU7po-bOgCGC_" \
                  "VwAFpH3ejNStMMYiPhxl7P_VvJHXfZBoCO7sQAvD_BwE\">Go To Website</a>"
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
    RoundFaceFrames = QtWidgets.QDialog()
    ui = Ui_RoundFaceFrames()
    ui.setupUi(RoundFaceFrames)
    RoundFaceFrames.show()
    sys.exit(app.exec_())

