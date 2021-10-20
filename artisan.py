import sys
import os
import glob
import importlib
from datetime import datetime

args = sys.argv[1:]


class Artisan:
    def __init__(self):
        # print(args)
        if args[0].split(":")[0] == "make":
            if args[0].split(":")[1] == "module":
                self.create_module(args[1])
            elif args[0].split(":")[1] == "model":
                model = args[1].split(":")
                self.create_model(model[1], model[0])
            elif args[0].split(":")[1] == "controller":
                controller = args[1].split(":")
                self.create_controller(controller[1], controller[0])
            elif args[0].split(":")[1] == "migration":
                self.migrations(args[1])

        elif args[0].split(":")[0] == "convert":
            print("convert")
        elif args[0] == "migrate":
            self.migrate()
        elif args[0].split(":")[0] == "migrate":
            if args[0].split(":")[1] == "fresh":
                self.migrate_fresh()

    @staticmethod
    def model(path, name):
        with open(f"{path}/{name.capitalize()}Model.py", "w", encoding="utf8") as file:
            file.write(f'''from inc.db.BaseModel import BaseModel
            

class {name.capitalize()}Model(BaseModel):
    def __init__(self):
        super({name.capitalize()}Model, self).__init__()
        self._table_name = '{name.lower()}'
        self._fields = '', ''')

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

    @staticmethod
    def migration(path, name):
        with open(f"{path}\\{str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))}_{name.lower()}.py", "w",
                  encoding="utf8") as file:
            file.write(f'''from database.inc.table import Table
            
            
class {name.capitalize()}(Table):

    def up(self):
        self._create(
            self.column(name="id", type="int", primary=True, auto_increment=True, unsigned=True),
        )

    def down(self):
        self._drop() ''')

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

    def migrations(self, name):
        self.migration(os.path.join(os.getcwd(), "database\\migrations"), name)

    @staticmethod
    def auto_load(name):
        module_name = name
        module = importlib.import_module(f"database.migrations.{module_name}", ".")
        class_instance = getattr(module, module_name.split("_")[-1].capitalize())
        return class_instance()

    def migrate(self):
        files = glob.glob(f"{os.getcwd()}\\database\\migrations\\*.py")
        for file in files:
            name = str(file).split("\\")[-1].replace(".py", '')
            table = self.auto_load(name)
            table.up()
            print(f"migrated  {str(name)} ")

    def un_migrate(self):
        files = glob.glob(f"{os.getcwd()}\\database\\migrations\\*.py")
        for file in files:
            name = str(file).split("\\")[-1].replace(".py", '')
            table = self.auto_load(name)
            table.down()
            print(f"dropped  {str(name)} ")

    def migrate_fresh(self):
        self.un_migrate()
        self.migrate()


if __name__ == '__main__':
    Artisan()
