from modules.home.home import Home
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys


class Index:
    def __init__(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Home()
    window.show()
    app.exec()
