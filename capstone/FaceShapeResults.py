import sys

from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class SquareFaceFrames(QDialog):
    def __init__(self):
        super(SquareFaceFrames, self).__init__()
        loadUi('SquareFaceFrames.ui', self)


def run():
    app = QApplication(sys.argv)
    window = SquareFaceFrames()
    window.setWindowTitle('Frame Recommendations')
    window.show()
    sys.exit(app.exec())

