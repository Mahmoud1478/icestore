from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from modules.categories.model.CategoriesModel import CategoriesModel


class CategoriesController(QWidget):
    def __init__(self):
        super(CategoriesController, self).__init__()
        loadUi("ui/categories/categories.ui", self)
        self.load_date()
        self.edit_off()
        self.cancle_btn.clicked.connect(self.edit_off)
        self.table.doubleClicked.connect(self.edit_signal)
        self.add_new.clicked.connect(self.create)

    def load_date(self):
        categories = CategoriesModel().get_fields().get_all()
        self.table.setRowCount(len(categories))
        for row, row_date in enumerate(categories):
            for column, data in enumerate(row_date):
                self.table.setItem(row, column, QTableWidgetItem(str(data)))

    def edit_on(self):
        self.add_new.setEnabled(False)
        self.edit_btn.setEnabled(True)
        self.cancle_btn.setEnabled(True)

    def edit_off(self):
        self.add_new.setEnabled(True)
        self.edit_btn.setEnabled(False)
        self.cancle_btn.setEnabled(False)

    def edit_signal(self):
        self.edit_on()
        row = self.table.currentRow()
        name = self.table.item(row, 0).text()
        self.name.setText(str(name))

    def create(self):
        if self.name.text() != "":
            CategoriesModel().create((self.name.text(),)).save()
            self.load_date()
