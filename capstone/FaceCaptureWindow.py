# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FaceCaptureWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class Ui_FaceCaptureWindow(QDialog):
    def __init__(self, output_path):
        super(Ui_FaceCaptureWindow, self).__init__()
        loadUi('FaceCaptureWindow.ui', self)
        self.image = None
        self.image_taken = False
        self.output_path = output_path
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(5)

        self.camButton.clicked.connect(self.take_photo)

    def update_frame(self):
        ret, self.image = self.capture.read()
        self.image = cv2.flip(self.image, 1)
        self.display_image(self.image, 1)

    def take_photo(self):
        self.image_taken = True

    def display_image(self, img, window=1):
        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:
            if img.shape[2] == 4:
                qformat = QImage.Format_RGBA888
            else:
                qformat = QImage.Format_RGB888
        outImage = QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
        outImage = outImage.rgbSwapped()

        if window == 1:
            self.videoFrame.setPixmap(QPixmap.fromImage(outImage))
            self.videoFrame.setScaledContents(True)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Ui_FaceCaptureWindow()
    window.setWindowTitle('Face Capture')
    window.show()
    sys.exit(app.exec_())

