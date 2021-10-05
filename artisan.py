import sys
import os

args = sys.argv[1:]


class Artisan:
    def __init__(self):

        if args[0].split(":")[0] == "make":
            if args[0].split(":")[1] == "module":
                self.create_module(args[1])
            elif args[0].split(":")[1] == "model":
                model = args[1].split(":")
                self.create_model(model[1], model[0])
            elif args[0].split(":")[1] == "controller":
                controller = args[1].split(":")
                self.create_controller(controller[1], controller[0])

        elif args[0].split(":")[0] == "convert":
            print("convert")

    @staticmethod
    def model(path, name):
        with open(f"{path}/{name.capitalize()}Model.py", "w", encoding="utf8") as file:
            file.write(f'''from inc.db.BaseModel import BaseModel
            

class {name.capitalize()}Model(BaseModel):
    def __init__(self):
        super({name.capitalize()}Model, self).__init__()
        self.table_name = '{name.lower()}'
        self.fields = None''')

    @staticmethod
    def controller(path, name):
        with open(f"{path}/{name.lower()}controller.py", "w", encoding="utf8") as file:
            file.write(f'''from modules.{name.lower()}.model.{name.capitalize()}Model import {name.capitalize()}Model
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class {name.capitalize()}Controller(QWidget):
    def __init__(self):
        super({name.capitalize()}Controller, self).__init__()
        loadUi("ui/{name.lower()}/{name.lower()}.ui", self)''')

    @staticmethod
    def sec_controller(path, name, module_name):
        with open(f"{path}/{name.lower()}controller.py", "w", encoding="utf8") as file:
            file.write(
                f'''from modules.{module_name.lower()}.model.{module_name.capitalize()}Model import {module_name.capitalize()}Model
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class {name.capitalize()}Controller(QWidget):
    def __init__(self):
        super({name.capitalize()}Controller, self).__init__()
        # loadUi("ui/{module_name.lower()}/{name.lower()}.ui", self)''')

    def create_module(self, name):
        module_path = os.path.join(os.getcwd(), f"modules\\{name}")
        module_path_ui = os.path.join(os.getcwd(), f"ui\\{name}")
        if not os.path.isdir(module_path):
            os.mkdir(module_path)
            os.mkdir(os.path.join(module_path, "ui"))
            os.mkdir(os.path.join(module_path, "model"))
            os.mkdir(os.path.join(module_path, "controllers"))
            self.model(os.path.join(module_path, "model"), name)
            self.controller(module_path, name)
            with open(os.path.join(module_path, f"ui\\{name.lower()}.py"), "w", encoding="utf8"):
                pass
            if not os.path.isdir(module_path_ui):
                os.mkdir(module_path_ui)
                with open(os.path.join(os.getcwd(), f"ui\\{name}\\{name}.ui"), "w", encoding="utf8"):
                    pass
        else:
            print("the module is already exists ")

    def convert_qrc(self):
        pass

    def convert_ui(self):
        pass

    def create_model(self, path, name):
        self.model(os.path.join(os.getcwd(), f"modules\\{path}\\model"), name)

    def create_controller(self, path, name):
        self.sec_controller(os.path.join(os.getcwd(), f"modules\\{path}\\controllers"), name, path)


if __name__ == "__name__":
    Artisan()
