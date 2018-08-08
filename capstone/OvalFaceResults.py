import sys

from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class OvalFaceFrames(QDialog):
    def __init__(self):
        super(OvalFaceFrames, self).__init__()
        loadUi('OvalFaceFrames.ui', self)


def run():
    app = QApplication(sys.argv)
    window = OvalFaceFrames()
    window.setWindowTitle('Frame Recommendations')
    window.show()
    sys.exit(app.exec())

