from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class DataTable(QWidget):
    def __init__(self):
        super(DataTable, self).__init__()
        loadUi('globals/widgets/datatable/design.ui', self)
        # print(parent.parentWidget().objectName())
