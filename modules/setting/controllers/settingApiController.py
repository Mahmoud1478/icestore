from PyQt5.QtCore import QSettings
import json

with open("AppConfiguration.json", "r", encoding="utf8") as config:
    configurations = json.load(config)["MyAppName"]


class SettingApiController:
    def __init__(self):
        self.__dbSetting = QSettings(configurations, "db")
        self.__activation = QSettings(configurations, "state")

    @staticmethod
    def setDefault(setting, default):
        return setting if setting is not None else default

    @property
    def dbSetting(self) -> dict:
        return {
            "host": self.setDefault(self.__dbSetting.value("host"), ""),
            "user": self.setDefault(self.__dbSetting.value("user"), ""),
            "password": self.setDefault(self.__dbSetting.value("password"), ""),
            "database": self.setDefault(self.__dbSetting.value("database"), ""),
        }

    @property
    def appState(self) -> dict:
        return {
            "state": self.setDefault(self.__activation.value("state"), 0),
            "app": self.setDefault(self.__activation.value("app"), ""),
            "migrate": self.setDefault(self.__activation.value("migrate"), 0),
        }

    @dbSetting.setter
    def dbSetting(self, value: dict):
        self.__dbSetting.setValue("host", value["host"])
        self.__dbSetting.setValue("user", value["user"])
        self.__dbSetting.setValue("password", value["password"])
        self.__dbSetting.setValue("database", value["database"])

    @appState.setter
    def appState(self, value: dict):
        self.__activation.setValue("state", value["state"])
        self.__activation.setValue("app", value["app"])
        self.__activation.setValue("migrate", value["migrate"])
