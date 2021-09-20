from modules.stocks.stocks import Stocks
from modules.units.units import Units
from modules.products.products import Products
from modules.categories.categories import Categories


class Callbacks:
    def add_category_action(self):
        dialog = Categories()

    def add_product_action(self):
        dialog = Products()

    def add_stock_action(self):
        dialog = Stocks()

    def add_unit_action(self):
        dialog = Units()
