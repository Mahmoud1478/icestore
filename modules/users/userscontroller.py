from modules.users.models.usersModel import Users
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class UsersController(QWidget):
    def __init__(self):
        super(UsersController, self).__init__()
        loadUi("ui/users/users.ui", self)