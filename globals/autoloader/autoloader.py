import json
from importlib import import_module

with open("AppConfiguration.json", "r", encoding="utf8") as AppConfiguration:
    PATHS = json.load(AppConfiguration)["Paths"]
    MODULE_PATH = PATHS["Modules"]


class AutoLoader:

    @staticmethod
    def model(className: str):
        models_path = PATHS["Models"].format(ModulesPath=MODULE_PATH, ModuleName=className.lower())
        model = import_module(models_path, ".")
        instance = getattr(model, className.capitalize())
        return instance()

    @staticmethod
    def subModel(moduleName: str, className: str):
        models_path = PATHS["SubModels"].format(ModulesPath=MODULE_PATH, ModuleName=moduleName.lower(),
                                                ClassName=className.lower())
        model = import_module(models_path, ".")
        instance = getattr(model, className.capitalize())
        return instance()

    @staticmethod
    def mainController():
        pass

    @staticmethod
    def controller():
        pass

    @staticmethod
    def uiFile(moduleName: str, widget):
        uic = import_module("PyQt5.uic")
        loadUi = getattr(uic, "loadUi")
        return loadUi(str(PATHS["UiFile"]).format(UiPath=PATHS[".uiUserInterface"], ModuleName=moduleName.lower()),
                      widget)

    @staticmethod
    def uiPyFile():
        pass

    @staticmethod
    def migration(fileName: str):
        fileName_ = str(fileName).replace(".py", "").split("\\")
        modulePath, className = fileName_, fileName_[-1].split("_table_")[-1]
        module = import_module(".".join(modulePath), ".")
        if "_" in className:
            class_instance = getattr(module, className)
        else:
            class_instance = getattr(module, className.capitalize())
        return class_instance()
