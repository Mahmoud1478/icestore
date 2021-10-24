from modules.home.homeController import HomeController
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from modules.categories.models.categoriesModel import Categories
from modules.orders.models.ordersModel import Orders
from modules.orders.models.ordersitemsModel import Ordersitems
from modules.teachers.models.teachersModel import Teachers
from modules.students.models.studentsModel import Students
from globals import AutoLoader
from vendor import Faker
from vendor import Helper


class Index:
    def __init__(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HomeController()
    window.show()
    app.exec()

    """ for _ in range(200):
        Teachers().create(
            fname=Faker.fName(),
            lname=Faker.lName(),
            age=Faker.integer(20, 60),
        ).save()
    for _ in range(200):
        Students().create(
            fname=Faker.fName(),
            lname=Faker.lName(),
            age=Faker.integer(15, 19),
        ).save()
    for _ in range(500):
        Teachersstudents().create(
            teacher_id=Faker.integer(1, 200),
            student_id=Faker.integer(1, 200),
        ).save()"""
    ##########################################################
    """order_items = Orders().where("id", 2000).findObject().items()
    print(order_items)"""
    ################################################################
    """mode = Students()
    data = mode.select("students.*").join("teachersstudents").on("teachersstudents.student_id", "students.id").join(
        "teachers").on("teachersstudents.teacher_id", "teachers.id").where("teachersstudents.teacher_id", 5).get()
    for item in data:
        print(f'''
    {item}
        ''')
    print("######################################### real ##########################")
    model2 = Teachers().where("id", 5).findObject()
    data2 = model2.students()
    for item in data2:
        print(f'''
    {item}
        ''')"""
    """mode = Teachers()
    data = mode.select("teachers.*").join("teachersstudents").on("teachersstudents.teacher_id", "teachers.id").join(
        "students").on("teachersstudents.student_id", "students.id").where("teachersstudents.student_id", 5).get()
    for item in data:
        print(f'''
    {item}''')
    print("######################################### real ##########################")
    model2 = Students().where("id", 5).findObject()
    data2 = model2.teachers()
    for item in data2:
        print(f'''
    {item}''')"""
    # AutoLoader.uiFile("units","x")
