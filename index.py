from modules.home.homecontroller import HomeController
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from modules.categories.model.CategoriesModel import Categories
from modules.orders.model.OrdersModel import Orders
from modules.orders.model.OrdersItemsModel import OrdersItems

from vendor import Faker
from vendor import Helper
from vendor import AutoLoader


class Index:
    def __init__(self):
        pass


if __name__ == '__main__':
    '''app = QApplication(sys.argv)
    window = HomeController()
    window.show()
    app.exec()'''
    """for i in range(50):
        name = Faker.text(i)
        print(i)"""

    # print(Faker.fullName(2, female=False))

    """for _ in range(200):
        Orders().create(
            discount=Faker.integer(0, 100),
            taxes=Faker.integer(0, 100),
            total=Faker.integer(0, 100),
        ).save()
    for _ in range(500):
        OrdersItems().create(
            product=Faker.fName(),
            count=Faker.integer(1, 200),
            order_id=Faker.integer(1,200),
        ).save()"""
    ##########################################################

    ''' print(Orders().select("product", "COUNT(count) as totalCount").items().groupBy(
        "product").get())'''
    print(OrdersItems().get())
