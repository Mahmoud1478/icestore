import os
from inc.converters.BaseConvertor import BaseConvertor


class Ui(BaseConvertor):
    def __init__(self):
        super(Ui, self).__init__()
        self.target_extension = ".ui"
        self.base_folder = None
        self.base_output_folder = None

    def convert(self):
        list_ui = self.find(self.base_folder)
        for item in list_ui:
            output = str(item).replace("\\ui", f"\\{self.base_output_folder}").replace(self.target_extension, ".py")
            # print(f'pyuic6  {item} -o {output}')
            os.system(f'pyuic5  {item} -o {output}')
