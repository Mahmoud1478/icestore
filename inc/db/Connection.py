import json

import MySQLdb
from MySQLdb.cursors import Cursor, DictCursor
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

from globals import AutoLoader

with open("AppConfiguration.json", "r", encoding="utf8") as AppConfiguration:
    configuration = json.load(AppConfiguration)["database"]
cursesMapper = {
    "dict": DictCursor,
    "tuple": Cursor
}

from . query import Query


class Connection:
    __db = None

    def __init__(self):
        try:
            self.__cursorType = configuration["DefaultCursor"]
            self.__cursor = None
            self._statement = f"SELECT * FROM {self.__class__.__name__}"
            self._values = []
            if self.__db is None:
                # self.__db = MySQLdb.connect(host=configuration["host"], user=configuration["user"],
                # password=configuration["password"],database=configuration["name"])
                self.__db = MySQLdb.connect(**AutoLoader.controller("settingApi", "setting")().dbSetting)
                self.__db.set_character_set("utf8mb4")
                self.__db.dump_debug_info()
                self.__set_cursor()
                self.query = Query()
        except Exception as Error:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(str(Error))
            msg.setWindowTitle("خطا")
            msg.setWindowIcon(QIcon("images/logo.png"))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def __set_cursor(self) -> None:
        try:
            self.__cursor = self.__db.cursor(cursesMapper[self.__cursorType])
        except Exception as err:
            print("cursor type not supported", err)
            self.__cursor = self.__db.cursor(Cursor)

    def close(self) -> None:
        self.__db.close()

    def get(self) -> tuple:
        self._query(self._statement, tuple(self._values))
        return self.__cursor.fetchall()

    def first(self):
        self._query(self._statement, tuple(self._values))
        return self.__cursor.fetchone()

    def findObject(self):
        self._query(self._statement, tuple(self._values))
        self._statement = f"SELECT * FROM {self.__class__.__name__}"
        self._values = []
        val = self.__cursor.fetchone()
        if val:
            for key, value in val.items():
                self.__setattr__(key, value)
            return self
        else:
            return None

    def save(self):
        self._query(self._statement, tuple(self._values))
        self._statement = f"SELECT * FROM {self.__class__.__name__}"
        self._values = []
        self.__db.commit()
        return self

    def count(self):
        self._query(self._statement, tuple(self._values))
        return self.__cursor.rowcount

    def saveObject(self):
        self._statement += f" WHERE id = {getattr(self, 'id')}"
        print(self._statement, self._values)
        self._query(self._statement, tuple(self._values))
        self._statement = ""
        self._values = []
        self.__db.commit()
        return self

    def saveRows(self):
        self._query_(self._statement, self._values)
        self._statement = f"SELECT * FROM {self.__class__.__name__}"
        self._values = []
        self.__db.commit()
        return self

    def _query(self, query: str, values: tuple = None):
        self.__cursor.execute(query, values)
        return self

    def _query_(self, query: str, values: list = None):
        self.__cursor.executemany(str(query), values)
        print(self.__cursor.statement)
        return self

    def last_one(self) -> int:
        return self.__cursor.lastrowid

    def __chose_cursors(self) -> object:
        if str(self.__cursorType).lower() == "dict":
            return DictCursor
        elif str(self.__cursorType).lower() == "tuple":
            return Cursor
        else:
            return Cursor

    def set_cursor_type(self, cursors_type: str):
        self.__cursorType = str(cursors_type)
        self.__set_cursor()
        return self
