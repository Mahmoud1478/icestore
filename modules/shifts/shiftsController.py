from modules.shifts.model.shiftsModel import ShiftsModel
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class ShiftsController(QWidget):
    def __init__(self):
        super(ShiftsController, self).__init__()
        loadUi("ui/shifts/shifts.ui", self)