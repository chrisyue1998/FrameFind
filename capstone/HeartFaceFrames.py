# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HeartFaceFrames.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint


class Ui_HeartFaceFrames(object):
    def setupUi(self, HeartFaceFrames):
        HeartFaceFrames.setObjectName("HeartFaceFrames")
        HeartFaceFrames.resize(720, 631)
        self.faceShapeText = QtWidgets.QLabel(HeartFaceFrames)
        self.faceShapeText.setGeometry(QtCore.QRect(160, 20, 411, 111))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.faceShapeText.setFont(font)
        self.faceShapeText.setAlignment(QtCore.Qt.AlignCenter)
        self.faceShapeText.setObjectName("faceShapeText")
        self.imageFrame = QtWidgets.QLabel(HeartFaceFrames)
        self.imageFrame.setGeometry(QtCore.QRect(160, 140, 411, 281))
        self.imageFrame.setText("")
        self.imageFrame.setObjectName("imageFrame")
        self.pixmap = QtGui.QPixmap('heartface0.jpg')
        self.pixmap = self.pixmap.scaledToWidth(411, QtCore.Qt.FastTransformation)
        self.imageFrame.setPixmap(self.pixmap)
        self.imageFrame.resize(self.pixmap.width(), self.pixmap.height())
        self.shuffleButton = QtWidgets.QPushButton(HeartFaceFrames)
        self.shuffleButton.setGeometry(QtCore.QRect(150, 550, 431, 32))
        self.shuffleButton.setObjectName("shuffleButton")
        self.linkDesc = QtWidgets.QLabel(HeartFaceFrames)
        self.linkDesc.setGeometry(QtCore.QRect(170, 470, 111, 16))
        self.linkDesc.setObjectName("linkDesc")
        self.purchaseLink = QtWidgets.QLabel(HeartFaceFrames)
        self.purchaseLink.setGeometry(QtCore.QRect(280, 470, 281, 16))
        self.purchaseLink.setText("")
        self.purchaseLink.setObjectName("purchaseLink")
        self.purchaseLink.setOpenExternalLinks(True)
        url = "<a href=\"https://www.zennioptical.com/p/" \
              "metal-alloy-full-rim-frame-with-spring-hinges/4190?skuId=419011\">Go To Website</a>"
        self.purchaseLink.setText(url)

        self.index = rand_index(5)
        self.shuffleButton.clicked.connect(self.shuffle_on_click)

        self.retranslateUi(HeartFaceFrames)
        QtCore.QMetaObject.connectSlotsByName(HeartFaceFrames)

    def retranslateUi(self, HeartFaceFrames):
        _translate = QtCore.QCoreApplication.translate
        HeartFaceFrames.setWindowTitle(_translate("HeartFaceFrames", "Dialog"))
        self.faceShapeText.setText(_translate("HeartFaceFrames", "You are closest to a heart face"))
        self.shuffleButton.setText(_translate("HeartFaceFrames", "Shuffle"))
        self.linkDesc.setText(_translate("HeartFaceFrames", "Link to purchase:"))

    def shuffle_on_click(self):
        index = self.index.rand()
        self.pixmap = QtGui.QPixmap('heartface' + str(index) + '.jpg')
        self.pixmap = self.pixmap.scaledToWidth(411, QtCore.Qt.FastTransformation)
        self.imageFrame.setPixmap(self.pixmap)
        self.imageFrame.resize(self.pixmap.width(), self.pixmap.height())
        if index == 0:
            url = "<a href=\"https://www.zennioptical.com/p/" \
                  "metal-alloy-full-rim-frame-with-spring-hinges/4190?skuId=419011\">Go To Website</a>"
            self.purchaseLink.setText(url)
        elif index == 1:
            url = "<a href=\"https://www.lenscrafters.com/lc-us/ray-ban/8053672667394\">Go To Website</a>"
            self.purchaseLink.setText(url)
        elif index == 2:
            url = "<a href=\"https://www.eyebuydirect.com/eyeglasses/frames/record-black-s-18695\">" \
                  "Go To Website</a>"
            self.purchaseLink.setText(url)
        elif index == 3:
            url = "<a href=\"https://www.glasses.com/glasses/Polo-Ralph-Lauren-PH1153J/Tortoise\">Go To Website</a>"
            self.purchaseLink.setText(url)
        else:
            url = "<a href=\"https://www.smartbuyglasses.com/designer-eyeglasses/" \
                  "Giorgio-Armani/Giorgio-Armani-AR7103-5017-308262.html\">Go To Website</a>"
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
    HeartFaceFrames = QtWidgets.QDialog()
    ui = Ui_HeartFaceFrames()
    ui.setupUi(HeartFaceFrames)
    HeartFaceFrames.show()
    sys.exit(app.exec_())

