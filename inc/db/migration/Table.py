from abc import ABC, abstractmethod

from inc.db.PConnection import Connection
from inc.db.assets.DBStatementClass.Mysql import Mysql
from .Column import Column


class Table(ABC):
    def __init__(self):
        self._con = Connection()
        self._driver = Mysql()
        self.column = Column

    @abstractmethod
    def up(self):
        pass

    @abstractmethod
    def down(self):
        pass

    def create(self, name, columns: list):
        self._con.statement(self._driver.create_table().format(name=name,
                                                               columns=','.join(str(item) for item in columns)))

    def _drop(self):
        self._con.statement(self._driver.drop_table().format(name=self.__class__.__name__.lower()))

    @abstractmethod
    def run(self, colum: Column):
        pass

