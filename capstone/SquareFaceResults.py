import sys

from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class SquareFaceFrames(QDialog):
    def __init__(self):
        super(SquareFaceFrames, self).__init__()
        loadUi('SquareFaceFrames.ui', self)
        self.frames = ['squareface1.jpg']

    def display_frame(self):
        label = self.imageFrame()
        pixmap = QPixmap(self.frames[0])
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())


def run():
    app = QApplication(sys.argv)
    window = SquareFaceFrames()
    window.setWindowTitle('Frame Recommendations')
    window.show()
    sys.exit(app.exec())

