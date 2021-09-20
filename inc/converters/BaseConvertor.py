import os
import glob


class BaseConvertor:
    def __init__(self):
        self.target_extension = None
        self.current_path = str(os.getcwd())

    def find(self, path=None):
        if path is None:
            target_path = self.current_path
        else:
            target_path = os.path.join(self.current_path, str(path).replace("/", "\\"))

        return glob.glob(f'{target_path}\*{self.target_extension}')

    def convert(self):
        pass
