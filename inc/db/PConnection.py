from MySQLdb.cursors import Cursor, DictCursor
from PyQt5.QtWidgets import QMessageBox
from globals import AutoLoader
from PyQt5.QtGui import QIcon
from abc import ABC
import MySQLdb
import time
import json
from .assets.QueryStrBuilder import QueryStrBuilder

with open("AppConfiguration.json", "r", encoding="utf8") as AppConfiguration:
    configuration = json.load(AppConfiguration)["database"]

cursesMapper = {
    "dict": DictCursor,
    "tuple": Cursor
}


class Connection(ABC):
    db = None
    cursor = None
    if db is None:
        try:
            db = MySQLdb.connect(**AutoLoader.controller("settingApi", "setting")().dbSetting)
            db.set_character_set("utf8mb4")
            db.dump_debug_info()
        except Exception as Error:
            """ msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(str(Error))
            msg.setWindowTitle("خطا")
            msg.setWindowIcon(QIcon("images/logo.png"))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()"""
            print(Error)

    def __init__(self):
        self.cursorType = configuration["DefaultCursor"]
        self.queryObj = QueryStrBuilder()
        self.__set_cursor()

    def __set_cursor(self) -> None:
        try:
            self.cursor = self.db.cursor(cursesMapper[self.cursorType])
        except Exception as err:
            print("cursor type not supported", err)
            self.cursor = self.db.cursor(Cursor)

    def close(self):
        self.db.close()
        return self

    def get(self, query, value) -> tuple or dict:
        self.query(query, value)
        return self.cursor.fetchall()

    def first(self):
        self._query(self.__build(), self.queryObj.values)
        self.queryObj.reset()
        return self.cursor.fetchone()

    def save(self):
        self._query(self.__build(), tuple(self.queryObj.values))
        self.queryObj.reset()
        self.db.commit()
        return self

    def count(self):
        self._query(self.__build(), tuple(self.queryObj.values))
        return self.cursor.rowcount

    def saveMany(self):
        self._query_(self.__build(), self.queryObj.values)
        self.queryObj.reset()
        self.db.commit()
        return self

    def query(self, query: str, values: tuple = None):
        start = time.time()
        self.cursor.execute(str(query), values)
        print(f"{bytes(self.cursor._executed).decode('utf8')}  {time.time() - start : .4f}s")
        return self

    def query_many(self, query: str, values: list = None):
        start = time.time()
        self.cursor.executemany(query, values)
        print(f"{bytes(self.cursor._executed).decode('utf8')}  {time.time() - start :.4f}s")

        return self

    def last_one(self) -> int:
        return self.cursor.lastrowid

    def set_cursor_type(self, cursors_type: str):
        self.cursorType = str(cursors_type)
        self.__set_cursor()
        return self

    def __build(self):
        return self.queryObj.build(self.table)

    def showQuery(self):
        return self.queryObj.build(self.table), self.queryObj.values

    def test(self):
        return self.queryObj.test(self.table)

    def statement(self, query: str, binding: tuple = None):
        self._query(query, binding)
        return self.db.commit()

    def toSql(self):
        return self.queryObj.build(self.table)
