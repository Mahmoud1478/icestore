from modules.home.homecontroller import HomeController
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class Index:
    def __init__(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HomeController()
    window.show()
    app.exec()
