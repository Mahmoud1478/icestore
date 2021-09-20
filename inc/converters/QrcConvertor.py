import os
import glob
from inc.converters.BaseConvertor import BaseConvertor

'''current_path = str(os.getcwd())
folder_name = str("pages_ui")
path = str(os.path.join(current_path, folder_name))'''


class Qrc(BaseConvertor):
    def __init__(self):
        super(Qrc, self).__init__()
        self.target_extension = ".qrc"
        self.base_folder = None

    def convert(self):
        list_qrc = self.find(self.base_folder)
        for item in list_qrc:
            # print(f'pyrcc6 {item} -o {str(item).replace(self.target_extension,".py")}')
            os.system(f'pyrcc5 {item} -o {str(item).replace(self.target_extension, ".py")}')
