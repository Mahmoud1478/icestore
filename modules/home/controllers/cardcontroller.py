from modules.home.model.HomeModel import HomeModel
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class CardController(QWidget):
    def __init__(self, parent):
        super(CardController, self).__init__()
        loadUi("ui/home/card1.ui", self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        blur = 20
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(blur)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(170, 85, 255, ))
        self.frame.setGraphicsEffect(shadow)
        # print(self.objectName())
