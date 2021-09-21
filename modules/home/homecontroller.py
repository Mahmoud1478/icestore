from modules.home.homesevices import HomeServices
from modules.home.home_actions import HomeActions
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.uic import loadUi


class HomeController(QMainWindow):
    def __init__(self):
        super(HomeController, self).__init__()
        loadUi("modules/home/ui/home.ui", self)
        QFontDatabase.addApplicationFont('assets/fonts/Cairo-Regular.ttf')
        self.actions_dec = {
            "information": {
                "الأقسام": {
                    "callback": HomeActions.add_category_action,
                    "icon": "assets/images/cat.ico"
                },
                "الأصناف": {
                    "callback": HomeActions.add_product_action,
                    "icon": "assets/images/cat.ico"
                },
                "المخازن": {
                    "callback": HomeActions.add_stock_action,
                    "icon": "assets/images/cat.ico"
                },
                "الوحدات": {
                    "callback": HomeActions.add_unit_action,
                    "icon": "assets/images/cat.ico"
                },
            },
            "purchases": {
                "الأقسام": {
                    "callback": HomeActions.add_category_action,
                    "icon": "assets/images/cat.ico"
                },
                "الأصناف": {
                    "callback": HomeActions.add_product_action,
                    "icon": "assets/images/cat.ico"
                },
                "المخازن": {
                    "callback": HomeActions.add_stock_action,
                    "icon": "assets/images/cat.ico"
                },
                "الوحدات": {
                    "callback": HomeActions.add_unit_action,
                    "icon": "assets/images/cat.ico"
                },
            },
            "reports": {
                "الأقسام": {
                    "callback": HomeActions.add_category_action,
                    "icon": "assets/images/cat.ico"
                },
                "الأصناف": {
                    "callback": HomeActions.add_product_action,
                    "icon": "assets/images/cat.ico"
                },
                "المخازن": {
                    "callback": HomeActions.add_stock_action,
                    "icon": "assets/images/cat.ico"
                },
                "الوحدات": {
                    "callback": HomeActions.add_unit_action,
                    "icon": "assets/images/cat.ico"
                },
            },
            "save": {
                "الأقسام": {
                    "callback": HomeActions.add_category_action,
                    "icon": "assets/images/cat.ico"
                },
                "الأصناف": {
                    "callback": HomeActions.add_product_action,
                    "icon": "assets/images/cat.ico"
                },
                "المخازن": {
                    "callback": HomeActions.add_stock_action,
                    "icon": "assets/images/cat.ico"
                },
                "الوحدات": {
                    "callback": HomeActions.add_unit_action,
                    "icon": "assets/images/cat.ico"
                },
            },
            "sales": {
                "الأقسام": {
                    "callback": HomeActions.add_category_action,
                    "icon": "assets/images/cat.ico"
                },
                "الأصناف": {
                    "callback": HomeActions.add_product_action,
                    "icon": "assets/images/cat.ico"
                },
                "المخازن": {
                    "callback": HomeActions.add_stock_action,
                    "icon": "assets/images/cat.ico"
                },
                "الوحدات": {
                    "callback": HomeActions.add_unit_action,
                    "icon": "assets/images/cat.ico"
                },
            },
            "setting": {
                "الأقسام": {
                    "callback": HomeActions.add_category_action,
                    "icon": "assets/images/cat.ico"
                },
                "الأصناف": {
                    "callback": HomeActions.add_product_action,
                    "icon": "assets/images/cat.ico"
                },
                "المخازن": {
                    "callback": HomeActions.add_stock_action,
                    "icon": "assets/images/cat.ico"
                },
                "الوحدات": {
                    "callback": HomeActions.add_unit_action,
                    "icon": "assets/images/cat.ico"
                },
            },
            "stores": {
                "الأقسام": {
                    "callback": HomeActions.add_category_action,
                    "icon": "assets/images/cat.ico"
                },
                "الأصناف": {
                    "callback": HomeActions.add_product_action,
                    "icon": "assets/images/cat.ico"
                },
                "المخازن": {
                    "callback": HomeActions.add_stock_action,
                    "icon": "assets/images/cat.ico"
                },
                "الوحدات": {
                    "callback": HomeActions.add_unit_action,
                    "icon": "assets/images/cat.ico"
                },
            },
        }
        self.dispatch_actions()

    def dispatch_actions(self):
        for key in self.actions_dec.keys():
            btn = getattr(self, key)
            menu = QMenu(btn)

            # menu.setStyleSheet('''QMenu::item { background-color: white; } QMenu::item:selected { background-color:
            # blue; }''')
            menu.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
            # menu.aboutToShow.connect(lambda: menu.setMinimumWidth(btn.width))
            # menu.aboutToShow.connect(lambda parent=btn, ele=menu: print(parent.geometry()))
            for action in self.actions_dec[key].keys():
                action_ = QAction(QIcon(self.actions_dec[key][action]["icon"]), action, self)
                menu.addAction(action_)
                action_.triggered.connect(self.actions_dec[key][action]["callback"])
                menu.addSeparator()
            btn.setMenu(menu)
            menu.aboutToShow.connect(lambda parent=btn, ele=menu: ele.setMinimumWidth(parent.width()))
            menu.aboutToShow.connect(lambda parent=btn, ele=menu: print(ele.width()))
            # menu.setMinimumWidth(100)
