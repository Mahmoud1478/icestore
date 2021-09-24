from inc.converters.UiConvertor import Ui


class UiCategoriesConvertor(Ui):
    def __init__(self):
        super(UiCategoriesConvertor, self).__init__()
        self.target_extension = ".ui"
        self.base_folder = "modules/categories/ui"
        self.base_output_folder = "uipy"
        self.convert()