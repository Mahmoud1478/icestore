import MySQLdb
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon


class Connection:
    def __init__(self):
        try:
            self.db = MySQLdb.connect(
                host="localhost",
                user="root",
                password="toor",
                database="ice_store"
            )
            self.db.set_character_set("utf8mb4")
            self.cursor = self.db.cursor()
        except Exception as Error:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("you have DataBase error {}".format(str(Error)))
            msg.setWindowTitle("خطا")
            msg.setWindowIcon(QIcon("images/logo.png"))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def close(self):
        self.db.close()

    def get_all(self):
        return self.cursor.fetchall()

    def first(self):
        return self.cursor.fetchone()

    def save(self):
        self.db.commit()

    def query(self, query, values=None):
        self.cursor.execute(str(query), values)
        return self

    def last_one(self):
        return self.cursor.lastrowid
