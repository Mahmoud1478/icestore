import MySQLdb
import json

with open("AppConfiguration.json", "r", encoding="utf8") as AppConfiguration:
    configuration = json.load(AppConfiguration)["database"]


class Connection:
    def __init__(self):
        try:
            self.__db = MySQLdb.connect(
                host=configuration["host"],
                user=configuration["user"],
                password=configuration["password"],
                database=configuration["name"]
            )
            self.__db.set_character_set("utf8mb4")
            self.__cursor = self.__db.cursor()
        except Exception as Error:
            print(Error)

    def close(self):
        self.__db.close()

    def get_all(self):
        return self.__cursor.fetchall()

    def first(self):
        return self.__cursor.fetchone()

    def save(self):
        self.__db.commit()

    def _query(self, query, values=None):
        self.__cursor.execute(str(query), values)
        return self

    def last_one(self):
        return self.__cursor.lastrowid

    def rollback(self):
        return self.__cursor.rollback()
