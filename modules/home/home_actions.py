from modules.stocks.stocks import Stocks
from modules.units.units import Units
from modules.products.products import Products
from modules.categories.categorycontroller import CategoryController


class HomeActions:
    def add_category_action(self, widget, index):
        self.set_index(widget, index)

    def add_product_action(self):
        dialog = Products()

    def add_stock_action(self):
        dialog = Stocks()

    def add_unit_action(self):
        dialog = Units()

    def set_index(self, widget, index):
        widget.setCurrentIndex(index)
