import os
from inc.converters.BaseConvertor import BaseConvertor


class Qrc(BaseConvertor):
    def __init__(self):
        super(Qrc, self).__init__()
        self.target_extension = ".qrc"
        self.base_folder = None

    def convert(self):
        list_qrc = self.find(self.base_folder)
        for item in list_qrc:
            os.system(f'pyrcc5 {item} -o {str(item).replace(self.target_extension, "_rc") + ".py"}')
