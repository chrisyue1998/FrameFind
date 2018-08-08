import sys

from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class HeartFaceFrames(QDialog):
    def __init__(self):
        super(HeartFaceFrames, self).__init__()
        loadUi('HeartFaceFrames.ui', self)


def run():
    app = QApplication(sys.argv)
    window = HeartFaceFrames()
    window.setWindowTitle('Frame Recommendations')
    window.show()
    sys.exit(app.exec())

