from modules.students.model.StudentsModel import StudentsModel
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class StudentsController(QWidget):
    def __init__(self):
        super(StudentsController, self).__init__()
        loadUi("ui/students/students.ui", self)