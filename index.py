# from globals import AutoLoader
from collections import Counter, defaultdict

from past.builtins import cmp

from inc.Collection.Collect import Collect
from inc.db.migration.Column import Column
from inc.db.migration.Table import Table
from modules.categories.models.categoriesModel import Categories
from modules.orders.models.ordersitemsModel import Ordersitems
# from vendor.Auth import Auth
import cProfile
from timeit import timeit, repeat
import itertools


# class Index:
#     @staticmethod
#     def index():
#         Auth().set_user(Categories().first())
#         api = AutoLoader.controller("settingApi", "setting")()
#         if api.appState == 0 or api.appState["migrate"] == 1:
#             return AutoLoader.mainController("welcome")
#         else:
#             return AutoLoader.mainController("home")
#
from modules.users.models.User import Users


class UserMs(Table):
    @staticmethod
    def test(self, name, col):
        if callable(col):
            col()

    def run(self, colum: Column):
        colum.primaryKey()

    def up(self):
        # self.test('self', 'user', lambda colum=Column: (
        #
        # ))
        self.create('users_test', [
            self.column.id().unique(),
            self.column.string('first_name').notNull(),
            self.column.string('last_name'),
            self.column.longText('short_note'),
            self.column.tinyInteger('is_active').default(0),
            self.column.string('color').nullable()
        ])

    def down(self):
        self._drop()


if __name__ == '__main__':

    data = Users().With(['shift']).get()
    print(data[0].shifts)
    pass
