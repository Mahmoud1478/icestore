from modules.teachers.model.TeachersModel import TeachersModel
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class TeachersController(QWidget):
    def __init__(self):
        super(TeachersController, self).__init__()
        loadUi("ui/teachers/teachers.ui", self)