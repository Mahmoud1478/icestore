from modules.orders.model.OrdersModel import OrdersModel
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class OrdersController(QWidget):
    def __init__(self):
        super(OrdersController, self).__init__()
        loadUi("ui/orders/orders.ui", self)