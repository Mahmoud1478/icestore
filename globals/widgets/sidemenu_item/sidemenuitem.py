from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class SideMenuItem(QWidget):
    open_signal = pyqtSignal(int)

    def __init__(self, name, height, items=None, alignment="right", style=None, ):
        super(SideMenuItem, self).__init__()
        self.height = height
        self.setMinimumHeight(self.height)
        self.name = name
        self.items = items
        self.alignment = alignment
        self.menu_status = False
        self.menu_frame = None
        self.setObjectName("container")
        self.default_style = {
            "widget": {
                "top": "2px solid  #f8f8f2",
                "bottom": "2px solid  #f8f8f2",
                "left": "none",
                "right": "none"
            },
            "main_btn": {
                "color": "white",
                "icon": "assets/images/icons/cil-chevron-bottom.png"
            },
            "item_btn": {
                "color": "white"
            },
        }
        self.style = style if style is not None else self.default_style
        self.setStyleSheet(f'''
            #container{{	
                border-top: {self.style["widget"]["top"]};
                border-left:{self.style["widget"]["left"]} ;
                border-right:{self.style["widget"]["right"]};
                border-bottom:{self.style["widget"]["bottom"]};
                  
            }}
            #container QPushButton{{
                background-repeat: no-repeat;
                border: none;
                background-color: transparent;
            }}
            #container #main_btn {{
                background-image:url({self.style["main_btn"]["icon"]});	
                background-position: {self.revers_alignment(self.alignment)} center;
                padding-{self.alignment}: 100px;
                border-{self.revers_alignment(self.alignment)}: 22px solid transparent;
                color: {self.style["main_btn"]["color"]};
                text-align: {self.revers_alignment(self.alignment)};
            }}
            #container #main_btn:hover {{
            background-color: #bd93f9;
            }}
            #container #main_btn:pressed {{	
            background-color: #ff79c6;
            color: rgb(255, 255, 255);
            }}
            #sideMenuItemMainMenuFrame QPushButton {{	
                background-position: {self.alignment} center;
                text-align: {self.alignment};
                color: {self.style["item_btn"]["color"]};
                border-{self.alignment}: 40px solid transparent;
                padding-{self.revers_alignment(self.alignment)}: 80px;
            }}
            #sideMenuItemMainMenuFrame QPushButton:hover {{
                background-color: #bd93f9;
            }}
            #sideMenuItemMainMenuFrame QPushButton:pressed {{	
                background-color: #ff79c6;
                color: rgb(255, 255, 255);
            }}
''')
        self.frame_height = len(self.items) * (self.height - 5)
        self.ui()
        self.setMaximumHeight(self.height + self.frame_height)
        self.setLayoutDirection(Qt.RightToLeft)

    def ui(self):
        self.menu_frame_func()
        bg_layout = QVBoxLayout(self)
        self.setLayout(bg_layout)
        bg_layout.setSpacing(0)
        bg_layout.setContentsMargins(0, 0, 0, 0)
        bg_layout.addWidget(self.top_btn())
        bg_layout.addWidget(self.menu_frame)

    def top_btn(self):
        main_btn = QPushButton(str(self.name))
        main_btn.setObjectName("main_btn")
        main_btn.setMinimumHeight(self.height)
        main_btn.setMaximumHeight(self.height)
        main_btn.clicked.connect(self.expand_menu)
        main_btn.setIcon(QIcon("assets/images/icons/icon_settings.png"))
        # main_btn.setLayoutDirection(Qt.RightToLeft)
        return main_btn

    def menu_frame_func(self):
        self.menu_frame = QFrame()
        self.menu_frame.setObjectName("sideMenuItemMainMenuFrame")
        layout = QVBoxLayout(self.menu_frame)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.menu_frame.setMaximumHeight(0)
        self.menu_frame.setLayout(layout)
        layout.setAlignment(Qt.AlignTop)
        self.menu_frame.setLayoutDirection(Qt.RightToLeft)
        for item in self.items:
            btn = QPushButton(str(item["name"]))
            btn.setStyleSheet(f'''
                background-image:url({item["icon"]});
            ''')
            btn.setMinimumHeight(self.height - 5)
            btn.setMaximumHeight(self.height - 5)
            btn.clicked.connect(item['callback'])
            layout.addWidget(btn)

    @staticmethod
    def revers_alignment(alignment):
        if alignment == "right":
            return "left"
        else:
            return "right"

    def animate(self, start, end, widget):
        self.animation = QPropertyAnimation(widget, b"maximumHeight")
        self.animation.setDuration(300)
        self.animation.setStartValue(start)
        self.animation.setEndValue(end)
        self.animation.setEasingCurve(QEasingCurve.Linear)
        self.animation.start()

    def expand_menu(self):
        if self.menu_status:
            self.animate(self.frame_height, 0, self.menu_frame)
            self.menu_status = False
            self.open_signal.emit(- self.frame_height)
        else:
            self.animate(0, self.frame_height, self.menu_frame)
            self.menu_status = True
            self.open_signal.emit(self.frame_height)
