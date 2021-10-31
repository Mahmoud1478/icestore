from modules.categories.models.categoriesModel import Categories
from globals import AutoLoader
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class CategoriesController(QWidget):
    def __init__(self):
        super(CategoriesController, self).__init__()
        AutoLoader.uiFile("categories", self)
        self.oldName = None
        self.loadData()
        self.editOff()
        self.eventHandler()
        self.ui()

    def ui(self):
        self.linePlaceholder()

    def eventHandler(self):
        self.table.doubleClicked.connect(self.editSignal)
        self.edit_btn.clicked.connect(self.updateItem)
        self.cancle_btn.clicked.connect(self.editOff)
        self.add_new.clicked.connect(self.createNew)
        # self.table.resizeEvent = self.tableUi

    def loadData(self):
        categories = Categories().set_cursor_type("tuple").select("name").orderBy("id").get()
        self.table.setRowCount(len(categories))
        for row, row_date in enumerate(categories):
            for column, data in enumerate(row_date):
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(row, column, item)

    def editOn(self):
        self.add_new.setEnabled(False)

        self.edit_btn.setEnabled(True)
        self.cancle_btn.setEnabled(True)

    def editOff(self):
        self.add_new.setEnabled(True)
        self.edit_btn.setEnabled(False)
        self.cancle_btn.setEnabled(False)
        self.name.setText("")
        self.oldName = None

    def editSignal(self):
        self.editOn()
        row = self.table.currentRow()
        name = self.table.item(row, 0).text()
        self.name.setText(str(name))
        self.oldName = name

    def createNew(self):
        if self.name.text() != "":
            Categories().create(name=self.name.text()).save()
            self.loadData()
            self.name.setText("")

    def tableUi(self, e=None):
        width = self.table.width()
        self.table.setColumnWidth(0, width * 0.85)
        self.table.setColumnWidth(1, width * .10)

    def linePlaceholder(self):
        palette = self.name.palette()
        text_color = QColor("white")
        palette.setColor(QPalette.PlaceholderText, text_color)
        self.name.setPalette(palette)

    def updateItem(self):
        name = self.name.text()
        if name != "":
            Categories().update(name=name).where("name", self.oldName).save()
            self.loadData()
            self.name.setText("")
            self.editOff()
