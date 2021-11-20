from globals import AutoLoader
from PyQt5.QtWidgets import QApplication
import sys
from database.seeder.categoriesSeeder import CategoriesSeeder
from modules.categories.models.categoriesModel import Categories
from modules.students.models.studentsModel import Students
from modules.globalModels.teachers_studentsModel import teachers_students
from vendor import Faker
from modules.teachers.models.teachersModel import Teachers
from modules.orders.models.ordersModel import Orders
from modules.orders.models.ordersitemsModel import Ordersitems
from faker import factory


class Index:
    @staticmethod
    def index():
        api = AutoLoader.controller("settingApi", "setting")()
        if api.appState == 0 or api.appState["migrate"] == 1:
            return AutoLoader.mainController("welcome")
        else:
            return AutoLoader.mainController("home")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Index.index()()
    window.show()
    app.exec()
