from inc.converters.UiConvertor import Ui


class UiHomeConvertor(Ui):
    def __init__(self):
        super(UiHomeConvertor, self).__init__()
        self.target_extension = ".ui"
        self.base_folder = "modules/home/ui"
        self.base_output_folder = "uipy"
        self.convert()