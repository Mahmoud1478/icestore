import MySQLdb
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
import json

with open("AppConfiguration.json", "r", encoding="utf8") as AppConfiguration:
    configuration = json.load(AppConfiguration)["database"]


class Connection:
    def __init__(self):
        try:
            self.__cursorType = configuration["DefaultCursor"]
            self.__cursor = None
            self._statement = ""
            self._values = []
            self.__db = MySQLdb.connect(
                host=configuration["host"],
                user=configuration["user"],
                password=configuration["password"],
                database=configuration["name"]
            )
            self.__db.set_character_set("utf8mb4")
            self.__set_cursor()
        except Exception as Error:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(str(Error))
            msg.setWindowTitle("خطا")
            msg.setWindowIcon(QIcon("images/logo.png"))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def __set_cursor(self) -> None:
        self.__cursor = self.__db.cursor(self.__chose_cursors())

    def close(self) -> None:
        self.__db.close()

    def get(self) -> tuple:
        self._query(self._statement, tuple(self._values))
        self._statement = ""
        self._values = []
        return self.__cursor.fetchall()

    def first(self) -> tuple:
        self._query(self._statement, tuple(self._values))
        self._statement = ""
        self._values = []
        return self.__cursor.fetchone()

    def save(self) -> int:
        self._query(self._statement, tuple(self._values))
        self._statement = ""
        self._values = []
        self.__db.commit()
        return self.__cursor.rowcount

    def saveRows(self) -> int:
        self._query_(self._statement, self._values)
        self._statement = ""
        self._values = []
        self.__db.commit()
        return self.__cursor.rowcount

    def _query(self, query: str, values: tuple = None):
        self.__cursor.execute(str(query), values)
        return self

    def _query_(self, query: str, values: list = None):
        self.__cursor.executemany(str(query), values)
        return self

    def last_one(self) -> int:
        return self.__cursor.lastrowid

    def __chose_cursors(self) -> object:
        if str(self.__cursorType).lower() == "dict":
            return MySQLdb.cursors.DictCursor
        elif str(self.__cursorType).lower() == "tuple":
            return MySQLdb.cursors.Cursor
        else:
            return MySQLdb.cursors.Cursor

    def set_cursor_type(self, cursors_type: str):
        self.__cursorType = str(cursors_type)
        self.__set_cursor()
        return self
