from globals import AutoLoader
from datetime import datetime
from vendor import App
import json
import time
import glob
import sys
import os


with open("AppConfiguration.json", "r", encoding="utf8") as AppConfiguration:
    file = json.load(AppConfiguration)
    configuration = file["Paths"]
    PyQtVersion = file["PyQtVersion"]


class Artisan:
    def __init__(self, sysArgs=None):
        self.args = sysArgs
        self.options = self.args[1:]
        self.FUNCTIONS_MAPPER = {
            "make": {
                "module": self.create_module,
                "model": self.create_model,
                "controller": self.create_controller,
                "migration": self.migrations,
            },
            "convert": {
                "qrc": self.convert_qrc,
                "ui": self.convert_ui,
            },
            "migrate": {
                "start": self.migrate,
                "fresh": self.migrate_fresh
            },
            "build": self.build,
            "exe": self.exe,

        }
        if ":" in self.args[0]:
            command, command_type = self.args[0].split(":")
            self.FUNCTIONS_MAPPER[command.lower()][command_type.lower()](self.options)
        else:
            self.FUNCTIONS_MAPPER[self.args[0].lower()](self.options)

    @staticmethod
    def model(path, name):
        model_path = f"{path}/{name.lower()}Model.py"
        with open(model_path, "w", encoding="utf8") as model:
            model.write(f'''from inc.db.BaseModel import BaseModel
            

class {name.capitalize()}(BaseModel):
    def __init__(self):
        super({name.capitalize()}, self).__init__() ''')
        return model_path

    @staticmethod
    def controller(path, name):
        with open(f"{path}/{name.lower()}Controller.py", "w", encoding="utf8") as controller:
            controller.write(f'''from modules.{name.lower()}.model.{name.lower()}Model import {name.capitalize()}Model
from PyQt{PyQtVersion}.QtWidgets import *
from PyQt{PyQtVersion}.uic import loadUi
from PyQt{PyQtVersion}.QtCore import *
from PyQt{PyQtVersion}.QtGui import *


class {name.capitalize()}Controller(QWidget):
    def __init__(self):
        super({name.capitalize()}Controller, self).__init__()
        loadUi("ui/{name.lower()}/{name.lower()}.ui", self)''')

    @staticmethod
    def sec_controller(path, name, module_name):
        with open(f"{path}/{name.lower()}Controller.py", "w", encoding="utf8") as controller:
            controller.write(
                f'''from modules.{module_name.lower()}.model.{module_name.lower()}Model import {module_name.capitalize()}Model 
from PyQt{PyQtVersion}.QtWidgets import *
from PyQt{PyQtVersion}.uic import loadUi
from PyQt{PyQtVersion}.QtCore import *
from PyQt{PyQtVersion}.QtGui import *


class {name.capitalize()}Controller(QWidget):
    def __init__(self):
        super({name.capitalize()}Controller, self).__init__()
        # loadUi("ui/{module_name.lower()}/{name.lower()}.ui", self)''')
        return f'''{path}/{name.lower()}Controller.py'''

    @staticmethod
    def migration(path, name):
        with open(f"{path}\\{str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))}_create_table_{name.lower()}.py", "w",
                  encoding="utf8") as model:
            model.write(f'''from database.inc.table import Table
            
            
class {name.capitalize() if "_" not in name else name}(Table):

    def up(self):
        return self._create(
            self.column(name="id", type="int", primary=True, auto_increment=True, unsigned=True),
        )

    def down(self):
        return self._drop() ''')
            return f"{str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))}_create_table_{name.lower()}.py"

    def create_module(self, options):
        name = options[0]
        module_path = f"{configuration['Modules']}/{name}"
        module_path_ui = f"{configuration['.uiUserInterface']}/{name}"
        if not os.path.isdir(module_path):
            os.mkdir(module_path)
            os.mkdir(f"{module_path}/ui")
            os.mkdir(f"{module_path}/models")
            os.mkdir(f"{module_path}/controllers")
            self.model(f"{module_path}/models", name)
            self.controller(module_path, name)
            with open(
                    f"{configuration['.pyUserInterface'].format(ModulesPath=module_path, ModuleName=name.lower())}",
                    "w", encoding="utf8"):
                pass
            if not os.path.isdir(module_path_ui):
                os.mkdir(module_path_ui)
                App.generateUi(module_path_ui, name)
        else:
            print("the module is already exists")

    def convert_qrc(self, *args):
        print("convert_qrc")
        return self

    def convert_ui(self, *args):
        print("convert_ui")
        return self

    def create_model(self, options):
        name, path = options[0].split("@")
        print(f'''created {self.model(f"{configuration['Modules']}/{path}/models", name)}''')

    def create_controller(self, options):
        name, path = options[0].split("@")
        print(f'''created {self.sec_controller(f"{configuration['Modules']}/{path}/controllers", name, path)}''')

    def migrations(self, options: list):
        print(f'''created {self.migration(f"{configuration['migrations']}", options[0])}''')

    @staticmethod
    def migrate(*args):
        files = glob.glob(f"{configuration['migrations']}/*.py")
        for item in files:
            start = time.time()
            name = str(item).split("\\")[-1].replace(".py", '')
            table = AutoLoader.migration(item)
            table.up()
            finish = time.time()
            print(f'''migrated {name} toke {finish - start} s ''')

    @staticmethod
    def un_migrate():
        files = glob.glob(f"{configuration['migration']}/*.py")
        for item in files:
            start = time.time()
            name = str(item).split("\\")[-1].replace(".py", '')
            table = AutoLoader.migration(item)
            table.down()
            finish = time.time()
            print(f"dropped {str(name)}  toke {finish - start} s")

    def migrate_fresh(self, *args):
        self.un_migrate()
        self.migrate()

    def test(self, op: list = None):
        print(op)

    def build(self, *args):
        pass

    def exe(self, *args):
        pass


if __name__ == '__main__':
    Artisan(sys.argv[1:])
