import MySQLdb
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QIcon


class Connection:
    def __init__(self):
        try:
            self.db = MySQLdb.connect(
                host="localhost",
                user="root",
                password="toor",
                database="futuretouch0"
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

    def all(self):
        return self.cursor.fetchall()

    def one(self):
        return self.cursor.fetchone()

    def commit(self):
        self.db.commit()
