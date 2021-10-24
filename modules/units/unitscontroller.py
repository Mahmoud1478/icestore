from modules.units.models.unitsModel import Units
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class UnitsController(QWidget):
    def __init__(self):
        super(UnitsController, self).__init__()
        loadUi("ui/units/units.ui", self)
        self.old_name = None
        # self.load_date()
        self.edit_off()
        self.event_handler()
        self.ui()

    def ui(self):
        self.line_placeholder()

    def event_handler(self):
        self.table.doubleClicked.connect(self.edit_signal)
        self.edit_btn.clicked.connect(self.update_item)
        self.cancle_btn.clicked.connect(self.edit_off)
        self.add_new.clicked.connect(self.create_new)
        self.table.resizeEvent = self.table_ui

    def load_date(self):
        categories = Units().select("name").get()
        self.table.setRowCount(len(categories))
        for row, row_date in enumerate(categories):
            for column, data in enumerate(row_date):
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(row, column, item)

    def edit_on(self):
        self.add_new.setEnabled(False)
        self.edit_btn.setEnabled(True)
        self.cancle_btn.setEnabled(True)

    def edit_off(self):
        self.add_new.setEnabled(True)
        self.edit_btn.setEnabled(False)
        self.cancle_btn.setEnabled(False)
        self.name.setText("")
        self.old_name = None

    def edit_signal(self):
        self.edit_on()
        row = self.table.currentRow()
        name = self.table.item(row, 0).text()
        self.name.setText(str(name))
        self.old_name = name

    def create_new(self):
        if self.name.text() != "":
            Units().create(name=self.name.text()).save()
            self.load_date()
            self.name.setText("")

    def table_ui(self, e=None):
        width = self.table.width()
        self.table.setColumnWidth(0, width * 0.85)
        self.table.setColumnWidth(1, width * .10)

    def line_placeholder(self):
        palette = self.name.palette()
        text_color = QColor("white")
        palette.setColor(QPalette.PlaceholderText, text_color)
        self.name.setPalette(palette)

    def update_item(self):
        name = self.name.text()
        if name != "":
            Units().update(name=name).where("name", self.old_name).save()
            self.load_date()
            self.name.setText("")
            self.edit_off()
