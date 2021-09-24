from modules.home.ui_to_py import UiHomeConvertor
from modules.categories.ui_to_py import UiCategoriesConvertor


class Convert:
    def __init__(self):
        UiHomeConvertor()
        UiCategoriesConvertor()


Convert()
