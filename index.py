from globals import AutoLoader
from PyQt5.QtWidgets import QApplication
import sys


class Index:
    @staticmethod
    def index():
        api = AutoLoader.controller("settingApi", "setting")()
        if api.appState == 0 or api.appState["migrate"] == 0:
            return AutoLoader.mainController("welcome")
        else:
            return AutoLoader.mainController("home")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Index.index()()
    window.show()
    app.exec()
