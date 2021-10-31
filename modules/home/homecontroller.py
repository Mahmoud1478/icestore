from globals import SideMenuItem
from globals import AutoLoader
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import ctypes

import Resorces_rc


class HomeController(QMainWindow):
    def __init__(self, username="اسم المستخدم"):
        super(HomeController, self).__init__()
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('ElmalaHSoFt.IceStore.1.0.0')
        QFontDatabase.addApplicationFont('assets/fonts/Cairo-Regular.ttf')
        # loadUi("ui/home/home.ui", self)
        AutoLoader.uiFile("home", self)
        self.available_space_menu = None
        self.user_menu_status = False
        self.main_menu_status = True
        self.open_menus_space = 0
        self.username = username
        self.menu_height = 45
        self.animation = None
        # self.shadow = None
        self.menus = None

        self.extraLabel.setText(str(self.username))
        self.event_handler()
        self.add_menus()
        # self.set_shadow()

    def event_handler(self):
        self.home_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.extraCloseColumnBtn.clicked.connect(self.toggle_user)
        self.closeAppBtn.clicked.connect(lambda: self.close())
        self.toggleButton.clicked.connect(self.toggle_menu)
        self.scrollContents.resizeEvent = self.menu_resize
        self.user.clicked.connect(self.toggle_user)

    def menu_resize(self, event):
        self.available_space_menu = self.scrollContents.height() - (
                (len(self.menus) * self.menu_height) + self.menu_height)

    def toggle_menu(self):
        if self.main_menu_status:
            self.animate(self.leftMenuBg, 200, 0, b"maximumWidth")
            self.main_menu_status = False
        else:
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
                        "callback": lambda: self.stackedWidget.setCurrentIndex(4)
                    },

                ]

            },
            {
                "name": "محازن",
                "submenu": [
                    {
                        "name": "تحويل بين المخازن",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },
                    {
                        "name": "جرد المخازن",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },

                ]
            },
            {
                "name": "مشتريات",
                "submenu": [
                    {
                        "name": "اضافة فاتورة",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },
                    {
                        "name": "عرض المشتريات",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },
                ]
            },
            {
                "name": "مبيعات",
                "submenu": [
                    {
                        "name": "اضافة فاتورة",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },
                    {
                        "name": "عرض الفواتير",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },

                ]
            },
            {
                "name": "عملاء وموردين",
                "submenu": [
                    {
                        "name": "اضافة عملاء",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },
                    {
                        "name": "عرض العملاء",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },
                    {
                        "name": "اضافة موردين",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },
                    {
                        "name": "عرض الموردين",
                        "icon": "assets/images/icons/cil-bell.png",
                        "callback": lambda: print("clicked")
                    },

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
            },
        ]
        for menu in self.menus:
            item = SideMenuItem(name=menu["name"], items=menu["submenu"], height=self.menu_height)
            self.topMenuLayout.addWidget(item)
            item.open_signal.connect(self.open_signal_fun)
        self.topMenuLayout.setAlignment(Qt.AlignTop)

    def open_signal_fun(self, value):
        if self.available_space_menu - self.open_menus_space < value > 0 or \
                self.available_space_menu - self.open_menus_space > value < 0:
            self.animate(self.scrollContents, self.scrollContents.height(), self.scrollContents.height() + value,
                         b"minimumHeight")
        self.open_menus_space += value

    def animate(self, widget, start, end, prop):
        self.animation = QPropertyAnimation(widget, prop)
        self.animation.stop()
        self.animation.setDuration(300)
        self.animation.setStartValue(start)
        self.animation.setEndValue(end)
        self.animation.setEasingCurve(QEasingCurve.Linear)
        self.animation.start()

    def set_shadow(self):
        blur = 20
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(blur)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(170, 85, 255, ))
        '''  self.chart_5.setGraphicsEffect(self.shadow)
        self.chart_4.setGraphicsEffect(self.shadow)
        self.chart_3.setGraphicsEffect(self.shadow)
        self.chart_2.setGraphicsEffect(self.shadow)'''
        self.widget_2.setGraphicsEffect(shadow)

    def changeEvent(self, a0: QResizeEvent) -> None:
        self.update()
