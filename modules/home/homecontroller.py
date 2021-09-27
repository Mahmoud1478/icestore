from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from globals import SideMenuItem

import Resorces_rc


class HomeController(QMainWindow):
    def __init__(self):
        super(HomeController, self).__init__()
        loadUi("ui/home/home1.ui", self)
        self.user_menu_status = False
        self.main_menu_status = True
        self.menu_height = 45
        self.user.clicked.connect(self.toggle_user)
        self.toggleButton.clicked.connect(self.toggle_menu)
        self.extraCloseColumnBtn.clicked.connect(self.toggle_user)
        self.add_menus()
        self.available_space_menu = None
        self.open_menus_space = 0
        self.scrollContents.resizeEvent = self.menu_resize

    def menu_resize(self, event):
        self.available_space_menu = self.scrollContents.height() - (len(self.menus) * self.menu_height)

    def toggle_menu(self):
        if self.main_menu_status:
            # self.animate(self.leftMenuBg, 200, 0, b"minimumWidth")
            self.animate(self.leftMenuBg, 200, 0, b"maximumWidth")
            self.main_menu_status = False
        else:
            # self.animate(self.leftMenuBg, 0, 200, b"minimumWidth")
            self.animate(self.leftMenuBg, 0, 200, b"maximumWidth")
            self.main_menu_status = True

    def toggle_user(self):
        if self.user_menu_status:
            self.animate(self.extraLeftBox, 200, 0, b"minimumWidth")
            self.user_menu_status = False
        else:
            self.animate(self.extraLeftBox, 0, 200, b"minimumWidth")
            self.user_menu_status = True

    def add_menus(self):
        self.menus = [

            {

                "name": "تعريفات",
                "submenu": [
                    {
                        "name": "الأقسام",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: self.stackedWidget.setCurrentIndex(1)
                    },
                    {
                        "name": "اصناف",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },
                    {
                        "name": "المخازن",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },
                    {
                        "name": "وحدات",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },

                ]

            },
            {
                "name": "محازن",
                "submenu": [
                    {
                        "name": "الأقسام",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },
                    {
                        "name": "اصناف",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },
                    {
                        "name": "المخازن",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },
                    {
                        "name": "وحدات",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },

                ]
            },
            {
                "name": "مشتريات",
                "submenu": [
                    {
                        "name": "الأقسام",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },
                    {
                        "name": "اصناف",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },
                    {
                        "name": "المخازن",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },
                    {
                        "name": "وحدات",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },

                ]
            },
            {
                "name": "مبيعات",
                "submenu": [
                    {
                        "name": "الأقسام",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },
                    {
                        "name": "اصناف",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },
                    {
                        "name": "المخازن",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },
                    {
                        "name": "وحدات",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    }

                ]
            },
            {
                "name": "خزنة",
                "submenu": [
                    {
                        "name": "الأقسام",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },
                    {
                        "name": "اصناف",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },
                    {
                        "name": "المخازن",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },
                    {
                        "name": "وحدات",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },

                ]
            },
            {
                "name": "تقارير",
                "submenu": [
                    {
                        "name": "الأقسام",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },
                    {
                        "name": "اصناف",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },
                    {
                        "name": "المخازن",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },
                    {
                        "name": "وحدات",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },

                ]
            },
            {
                "name": "اعدادات",
                "submenu": [
                    {
                        "name": "الأقسام",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },
                    {
                        "name": "اصناف",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },
                    {
                        "name": "المخازن",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },
                    {
                        "name": "وحدات",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },

                ]
            }
        ]
        for menu in self.menus:
            item = SideMenuItem(name=menu["name"], items=menu["submenu"], height=self.menu_height)
            self.topMenuLayout.addWidget(item)
            item.open_signal.connect(self.open_signal_fun)
        self.topMenuLayout.setAlignment(Qt.AlignTop)
        self.scrollContents.setMinimumHeight(len(self.menus) * self.menu_height)

    def open_signal_fun(self, value):

        if self.available_space_menu - self.open_menus_space < value > 0 or \
                self.available_space_menu - self.open_menus_space > value < 0:
            self.animate(self.scrollContents, self.scrollContents.height(), self.scrollContents.height() + value,
                         b"minimumHeight")

        self.open_menus_space += value

    def animate(self, widget, start, end, prop):
        self.animation = QPropertyAnimation(widget, prop)
        self.animation.setDuration(300)
        self.animation.setStartValue(start)
        self.animation.setEndValue(end)
        self.animation.setEasingCurve(QEasingCurve.Linear)
        self.animation.start()
