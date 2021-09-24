from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from modules.categories.uipy.categories import Ui_Form
from modules.categories.CategoryModel import CategoryModel


class CategoryController(QWidget, Ui_Form):
    def __init__(self):
        super(CategoryController, self).__init__()
        self.setupUi(self)
        self.stacked = None
        self.last_name = None
        self.edit_mode_off()
        self.home.clicked.connect(lambda: self.stacked.setCurrentIndex(0))
        self.load_data()
        self.create_.clicked.connect(self.new)
        self.cancel.clicked.connect(self.cancel_)
        self.edit.clicked.connect(self.edit_)
        self.table.doubleClicked.connect(self.get_item)

    def new(self):
        name = self.name.text()
        if name != "":
            try:
                CategoryModel().create((name,)).save()
                self.load_data()

            except Exception as err:
                print(err)

    def cancel_(self):
        self.name.setText("")
        self.last_name = None
        self.edit_mode_off()

    def edit_(self):
        name = self.name.text()
        if name != "":
            try:
                CategoryModel().update(["name=%s", (self.last_name,)], (name,)).save()
                self.load_data()
            except Exception as err:
                print(err)

    def get_item(self):
        row = self.table.currentRow()
        self.last_name = self.table.item(row, 1).text()
        self.name.setText(str(self.last_name))
        self.edit_mode_on()

    def load_data(self):
        categories = CategoryModel().all()
        self.table.setRowCount(len(categories))
        for row, row_data in enumerate(categories):
            for column, item in enumerate(row_data):
                self.table.setItem(row, column, QTableWidgetItem(str(item)))

    def edit_mode_on(self):
        self.create_.setEnabled(False)
        self.cancel.setEnabled(True)
        self.edit.setEnabled(True)

    def edit_mode_off(self):
        self.create_.setEnabled(True)
        self.cancel.setEnabled(False)
        self.edit.setEnabled(False)
