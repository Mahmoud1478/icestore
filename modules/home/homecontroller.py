from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi

import Resorces_rc


class HomeController(QMainWindow):
    def __init__(self):
        super(HomeController, self).__init__()
        loadUi("ui/home/home.ui", self)
