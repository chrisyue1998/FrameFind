import sys

from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class RoundFaceFrames(QDialog):
    def __init__(self):
        super(RoundFaceFrames, self).__init__()
        loadUi('RoundFaceFrames.ui', self)


def run():
    app = QApplication(sys.argv)
    window = RoundFaceFrames()
    window.setWindowTitle('Frame Recommendations')
    window.show()
    sys.exit(app.exec())

