from modules.home.homesevices import HomeServices
from modules.home.home_actions import HomeActions
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# from PyQt6.uic import loadUi
from modules.home.uipy.home import Ui_MainWindow


class HomeController(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(HomeController, self).__init__()
        self.setupUi(self)
        QFontDatabase.addApplicationFont('assets/fonts/Cairo-Regular.ttf')
        self.actions_dec = {
            "information": {
                "الأقسام": {
                    "callback": lambda: HomeActions().add_category_action(self.stacked, 1),
                    "icon": "assets/images/cat.ico",
                    "shortcut": "Ctrl+Q"
                },
                "الأصناف": {
                    "callback": HomeActions.add_product_action,
                    "icon": "assets/images/cat.ico",
                    "shortcut": "Ctrl+Q"
                },
                "المخازن": {
                    "callback": HomeActions.add_stock_action,
                    "icon": "assets/images/cat.ico",
                    "shortcut": "Ctrl+Q"
                },
                "الوحدات": {
                    "callback": HomeActions.add_unit_action,
                    "icon": "assets/images/cat.ico",
                    "shortcut": "Ctrl+Q"
                },
            },
            "purchases": {
                "الأقسام": {
                    "callback": HomeActions.add_category_action,
                    "icon": "assets/images/cat.ico",
                    "shortcut": "Ctrl+Q"
                },
                "الأصناف": {
                    "callback": HomeActions.add_product_action,
                    "icon": "assets/images/cat.ico",
                    "shortcut": "Ctrl+Q"
                },
                "المخازن": {
                    "callback": HomeActions.add_stock_action,
                    "icon": "assets/images/cat.ico",
                    "shortcut": "Ctrl+Q"
                },
                "الوحدات": {
                    "callback": HomeActions.add_unit_action,
                    "icon": "assets/images/cat.ico",
                    "shortcut": "Ctrl+Q"
                },
            },
            "reports": {
                "الأقسام": {
                    "callback": HomeActions.add_category_action,
                    "icon": "assets/images/cat.ico",
                    "shortcut": "Ctrl+Q"
                },
                "الأصناف": {
                    "callback": HomeActions.add_product_action,
                    "icon": "assets/images/cat.ico",
                    "shortcut": "Ctrl+Q"
                },
                "المخازن": {
                    "callback": HomeActions.add_stock_action,
                    "icon": "assets/images/cat.ico",
                    "shortcut": "Ctrl+Q"
                },
                "الوحدات": {
                    "callback": HomeActions.add_unit_action,
                    "icon": "assets/images/cat.ico",
                    "shortcut": "Ctrl+Q"
                },
            },
            "save": {
                "الأقسام": {
                    "callback": HomeActions.add_category_action,
                    "icon": "assets/images/cat.ico",
                    "shortcut": "Ctrl+Q"
                },
                "الأصناف": {
                    "callback": HomeActions.add_product_action,
                    "icon": "assets/images/cat.ico",
                    "shortcut": "Ctrl+Q"
                },
                "المخازن": {
                    "callback": HomeActions.add_stock_action,
                    "icon": "assets/images/cat.ico",
                    "shortcut": "Ctrl+Q"
                },
                "الوحدات": {
                    "callback": HomeActions.add_unit_action,
                    "icon": "assets/images/cat.ico",
                    "shortcut": "Ctrl+Q"
                },
            },
            "sales": {
                "الأقسام": {
                    "callback": HomeActions.add_category_action,
                    "icon": "assets/images/cat.ico",
                    "shortcut": "Ctrl+Q"
                },
                "الأصناف": {
                    "callback": HomeActions.add_product_action,
                    "icon": "assets/images/cat.ico",
                    "shortcut": "Ctrl+Q"
                },
                "المخازن": {
                    "callback": HomeActions.add_stock_action,
                    "icon": "assets/images/cat.ico",
                    "shortcut": "Ctrl+Q"
                },
                "الوحدات": {
                    "callback": HomeActions.add_unit_action,
                    "icon": "assets/images/cat.ico",
                    "shortcut": "Ctrl+Q"
                },
            },
            "setting": {
                "الأقسام": {
                    "callback": HomeActions.add_category_action,
                    "icon": "assets/images/cat.ico",
                    "shortcut": "Ctrl+Q"
                },
                "الأصناف": {
                    "callback": HomeActions.add_product_action,
                    "icon": "assets/images/cat.ico",
                    "shortcut": "Ctrl+Q"
                },
                "المخازن": {
                    "callback": HomeActions.add_stock_action,
                    "icon": "assets/images/cat.ico",
                    "shortcut": "Ctrl+Q"
                },
                "الوحدات": {
                    "callback": HomeActions.add_unit_action,
                    "icon": "assets/images/cat.ico",
                    "shortcut": "Ctrl+Q"
                },
            },
            "stores": {
                "الأقسام": {
                    "callback": HomeActions.add_category_action,
                    "icon": "assets/images/cat.ico",
                    "shortcut": "Ctrl+Q"
                },
                "الأصناف": {
                    "callback": HomeActions.add_product_action,
                    "icon": "assets/images/cat.ico",
                    "shortcut": "Ctrl+Q"
                },
                "المخازن": {
                    "callback": HomeActions.add_stock_action,
                    "icon": "assets/images/cat.ico",
                    "shortcut": "Ctrl+Q"
                },
                "الوحدات": {
                    "callback": HomeActions.add_unit_action,
                    "icon": "assets/images/cat.ico",
                    "shortcut": "Ctrl+Q"
                },
            },
        }
        self.dispatch_actions()
        # self.pushButton.clicked.connect(HomeActions.add_category_action)
        self.stacked.widget(1).stacked = self.stacked

    def dispatch_actions(self):
        for key in self.actions_dec.keys():
            menu = getattr(self, key)
            menu.setLayoutDirection(Qt.RightToLeft)
            for action in self.actions_dec[key].keys():
                action_ = QAction(QIcon(self.actions_dec[key][action]["icon"]), action, self)
                menu.addAction(action_)
                action_.setShortcut(self.actions_dec[key][action]["shortcut"])
                action_.triggered.connect(self.actions_dec[key][action]["callback"])
                # menu.addSeparator()
