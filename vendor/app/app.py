import json
from datetime import datetime
from vendor.app.template.uitemplate import Template

with open("AppConfiguration.json", "r", encoding="utf8") as AppConfiguration:
    file = json.load(AppConfiguration)
    PyQtVersion = file["PyQtVersion"]
    APP_Name = file["MyAppName"]
    Paths = file["Paths"]
    AppConfiguration.close()


class App:
    @staticmethod
    def generateUi(name: str, type: str, module: str = ''):
        widget = {
            "widget": "Widget",
            "dialog": "Dialog",
            "mainWindow": "MainWindow",
            "dialogWRB": "DialogWithRightButtons",
            "dialogWBB": "DialogWithBottomButtons",
            "frame": "Frame"
        }
        uiFilePath = f"{Paths['uiUserInterface']}/{name if module == '' else module}/{name}.ui"
        with open(uiFilePath, "w", encoding="utf8") as uiFile:
            uiFile.write(getattr(Template, widget[type]).format(Name=name, AppName=APP_Name))
        return uiFilePath

    @staticmethod
    def generateMainController(name: str):
        lwName = name.lower()
        cpName = name.capitalize()
        controller_path = Paths["Modules"] + "/" + lwName + "/" + lwName + "Controller.py"
        with open(controller_path, "w", encoding="utf8") as controller:
            controller.write(f'''from modules.{lwName}.model.{lwName}Model import {cpName}Model
from PyQt{PyQtVersion}.QtWidgets import *
from PyQt{PyQtVersion}.uic import loadUi
from PyQt{PyQtVersion}.QtCore import *
from PyQt{PyQtVersion}.QtGui import *


class {cpName}Controller(QWidget):
    def __init__(self):
        super({cpName}Controller, self).__init__()
        loadUi("ui/{lwName}/{lwName}.ui", self)''')
            return controller_path

    @staticmethod
    def generateController(name: str, module_name: str):
        lwName = name.lower()
        cpName = name.capitalize()
        lwModulesName = module_name.lower()
        controller_path = Paths["Modules"] + "/" + lwModulesName + "/" + "controllers" + "/" + lwName + "Controller.py"
        with open(controller_path, "w", encoding="utf8") as controller:
            controller.write(
                f'''from {Paths["Modules"]}.{lwModulesName}.models.{lwModulesName}Model import {module_name.capitalize()}
from PyQt{PyQtVersion}.QtWidgets import *
from PyQt{PyQtVersion}.uic import loadUi
from PyQt{PyQtVersion}.QtCore import *
from PyQt{PyQtVersion}.QtGui import *


class {cpName}Controller(QWidget):
    def __init__(self):
        super({cpName}Controller, self).__init__()
        # loadUi("ui/{lwModulesName}/{lwName}.ui", self)''')
        return controller_path

    @staticmethod
    def generateModel(name: str, module_name: str):
        cpName = name.capitalize()
        model_path = Paths["Modules"] + "/" + module_name.lower() + "/" + "models" + "/" + name.lower() + "Model.py"
        with open(model_path, "w", encoding="utf8") as model:
            model.write(f'''from inc.db.BaseModel import BaseModel


class {cpName}(BaseModel):
    def __init__(self):
    super({cpName}, self).__init__() ''')
        return model_path

    @staticmethod
    def generateMainModel(name: str):
        lwName = name.lower()
        cpName = name.capitalize()
        model_path = Paths["Modules"] + "/" + lwName + "/" + "models" + "/" + lwName + "Model.py"
        with open(model_path, "w", encoding="utf8") as model:
            model.write(f'''from inc.db.BaseModel import BaseModel


class {cpName}(BaseModel):
    def __init__(self):
        super({cpName}, self).__init__() ''')
        return model_path

    @staticmethod
    def generateMigration(name: str):
        file_ = f"{Paths['migrations']}/{str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))}_create_table_{name.lower()}.py"
        print_ = file_.replace('\\', '/')
        with open(file_, "w", encoding="utf8") as migration:
            migration.write(f'''from inc.db.table import Table
            
            
class {name.capitalize() if "_" not in name else name}(Table):
    
    # self._name = 'MyTable' change table name 
    
    def up(self):
        return self._create(
            self.column(name="id", type="int", primary=True, auto_increment=True, unsigned=True),
        )

    def down(self):
        return self._drop() ''')
            return f"{print_}"

    @staticmethod
    def generateSeeder():
        pass
