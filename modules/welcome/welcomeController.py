from globals import AutoLoader
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import MySQLdb
import subprocess
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import ctypes
import Resorces_rc

CREATE_DATABASE_STATEMENT = '''CREATE DATABASE IF NOT EXISTS {name} DEFAULT CHARACTER SET utf8mb4 COLLATE 
utf8mb4_0900_ai_ci DEFAULT ENCRYPTION='N' '''


class WelcomeController(QMainWindow):
    def __init__(self):
        super(WelcomeController, self).__init__()
        loadUi("ui/__activator__/activator1.ui", self)
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('ElmalaHSoFt.IceStore.1.0.0')
        QFontDatabase.addApplicationFont('assets/fonts/Cairo-Regular.ttf')
        self.api = AutoLoader.controller("settingApi", "setting")()
        self.__db = None
        self.__cursor = None
        if self.api.appState["app"] == "":
            current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
            self.api.appState = {
                **self.api.appState,
                "app": self.strToBin(current_machine_id)}
        if self.api.appState["state"] == 0:
            self.db_frame.setEnabled(False)
        else:
            self.serial_field.setText(str(self.binToStr(self.api.appState["app"])))

        self.db_name_frame.setEnabled(False)
        self.dbname_field.setText(str(self.api.dbSetting["database"]))

        self.actiongot1.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.actiongo_to_2.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.show_serial_field.clicked.connect(self.showSerialField)
        self.check_serial.clicked.connect(self.checkSerial)
        self.show_host_field.clicked.connect(self.showHostField)
        self.show_username_field.clicked.connect(self.showUsernameField)
        self.show_password_field.clicked.connect(self.showPasswordField)
        self.activate_app.clicked.connect(self.activateApp)
        self.db_connect.clicked.connect(self.dbConnect)
        self.db_create.clicked.connect(self.dbCreate)
        self.password_field.setText(str(self.api.dbSetting["password"]))
        self.host_field.setText(str(self.api.dbSetting["host"]))
        self.username_field.setText(str(self.api.dbSetting["user"]))

    def checkSerial(self):
        if self.password.text() == "1":
            self.show_serial.setText(str(self.binToStr(self.api.appState["app"])))

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("wrong password")
            msg.setWindowTitle("خطا")
            msg.setWindowIcon(QIcon("images/logo.png"))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    @staticmethod
    def strToBin(text):
        return [bin(ord(i))[2:].zfill(8) for i in text]

    @staticmethod
    def binToStr(binaryText):
        return "".join([chr(int(i, 2)) for i in binaryText])

    def showSerialField(self):
        if self.show_serial_field.isChecked():
            self.serial_field.setEchoMode(QLineEdit.Normal)
        else:
            self.serial_field.setEchoMode(QLineEdit.Password)

    def showPasswordField(self):
        if self.show_password_field.isChecked():
            self.password_field.setEchoMode(QLineEdit.Normal)
        else:
            self.password_field.setEchoMode(QLineEdit.Password)

    def showUsernameField(self):
        if self.show_username_field.isChecked():
            self.username_field.setEchoMode(QLineEdit.Normal)
        else:
            self.username_field.setEchoMode(QLineEdit.Password)

    def showHostField(self):
        if self.show_host_field.isChecked():
            self.host_field.setEchoMode(QLineEdit.Normal)
        else:
            self.host_field.setEchoMode(QLineEdit.Password)

    def activateApp(self):
        if self.serial_field.text() == self.binToStr(self.api.appState["app"]):
            self.db_frame.setEnabled(True)
            self.api.appState = {
                **self.api.appState,
                "state": 1
            }
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("الرقم التسلسلي غير صحيح")
            msg.setWindowTitle("خطا")
            msg.setWindowIcon(QIcon("images/logo.png"))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def dbConnect(self):
        conn = {
            "host": self.host_field.text(),
            "user": self.username_field.text(),
            "password": self.password_field.text()
        }
        if conn["host"] != "" and conn["user"] != "" and conn["password"] != "":
            try:
                self.__db = MySQLdb.connect(**conn)
                self.console.appendPlainText("connected successfully")
                self.db_name_frame.setEnabled(True)
                self.__cursor = self.__db.cursor()
                self.api.dbSetting = {
                    **self.api.dbSetting,
                    **conn
                }
            except Exception as err:
                self.console.appendPlainText(str(err))

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("دخل بينات صحيحة")
            msg.setWindowTitle("خطا")
            msg.setWindowIcon(QIcon("images/logo.png"))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def dbCreate(self):
        name = self.dbname_field.text()
        if name != "":
            try:
                self.__cursor.execute(CREATE_DATABASE_STATEMENT.format(name=name))
                self.console.appendPlainText("database created successfully ")
                self.api.dbSetting = {
                    **self.api.dbSetting,
                    "database": name
                }
                self.__db = MySQLdb.connect(**self.api.dbSetting)
                self.db_migrate.setEnabled(True)
            except Exception as err:
                self.console.appendPlainText(str(err))
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("ادخل اسم صحيح")
            msg.setWindowTitle("خطا")
            msg.setWindowIcon(QIcon("images/logo.png"))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
