from modules.home.callbacks import Callbacks
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.uic import loadUi


class Home(QMainWindow, Callbacks):
    def __init__(self):
        super(Home, self).__init__()
        loadUi("modules/home/ui/home.ui", self)
        self.actions_dec = {
            "add_category": self.add_category_action,
            "add_product": self.add_product_action,
            "add_stock": self.add_stock_action,
            "add_unit": self.add_unit_action,
        }
        self.dispatch_actions()

    def dispatch_actions(self):
        for key in self.actions_dec.keys():
            getattr(self, key).triggered.connect(self.actions_dec[key])
