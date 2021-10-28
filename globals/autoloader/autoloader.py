import json
from importlib import import_module

with open("NameSpaces.json", "r", encoding="utf8") as paths:
    Paths = json.load(paths)
    paths.close()

with open("AppConfiguration.json", "r", encoding="utf8") as AppConfiguration:
    file = json.load(AppConfiguration)
    MODULE_PATH = file["Paths"]["Modules"]
    UI_PATH = file["Paths"]["uiUserInterface"]
    AppConfiguration.close()


class AutoLoader:

    @staticmethod
    def model(className: str):
        models_path = Paths["Models"].format(ModulesPath=MODULE_PATH, ModuleName=className.lower())
        model = import_module(models_path, ".")
        instance = getattr(model, className.capitalize())
        return instance()

    @staticmethod
    def subModel(moduleName: str, className: str):
        models_path = Paths["SubModels"].format(ModulesPath=MODULE_PATH, ModuleName=moduleName.lower(),
                                                ClassName=className.lower())
        model = import_module(models_path, ".")
        instance = getattr(model, className.capitalize())
        return instance()

    @staticmethod
    def mainController(className: str):
        models_path = Paths["MainControllers"].format(ModulesPath=MODULE_PATH, ModuleName=className.lower())
        controller = import_module(models_path)
        instance = getattr(controller, className.capitalize() + "Controller")
        return instance

    @staticmethod
    def controller(className: str, moduleName: str):
        models_path = Paths["Controllers"].format(ModulesPath=MODULE_PATH, ModuleName=moduleName,
                                                  ClassName=className)
        controller = import_module(models_path)
        instance = getattr(controller, className[0].upper() + className[1:] + "Controller")
        return instance

    @staticmethod
    def uiFile(moduleName: str, widget):
        uic = import_module("PyQt5.uic")
        loadUi = getattr(uic, "loadUi")
        return loadUi(str(Paths["UiFile"]).format(UiPath=UI_PATH, ModuleName=moduleName.lower()), widget)

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
