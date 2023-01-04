# from inc.db.Connection import Connection
from inc.db.PConnection import Connection
from globals import AutoLoader
from abc import ABC
from json import loads
from .assets.DBStatementClass.Mysql import Mysql
from .assets.QueryStrBuilder import QueryStrBuilder
from ..Collection.Collect import Collect
from ..Collection.Collection import Collection


class BaseModel(ABC):
    __connection = Connection()

    def __init__(self, attrs: dict = None, test=None):
        self._drive = Mysql()
        self._primaryKey = 'id'
        self.__attrs = self.Attributes(self)
        self._hidden = []
        self.__connection = Connection()
        self._columns = ['*']
        self._with_columns = []
        self._with_ = []
        self._values = []
        self._table = str.lower(self.__class__.__name__)
        self.__query_type__ = 'select'
        self._query_segments = {
            'INNER JOIN': {},
            'LEFT JOIN': {},
            'RIGHT JOIN': {},
            'WHERE': [],
            'OR': [],
            'GROUP BY': [],
            'ORDER BY': None,
            'LIMIT': 0,
            'OFFSET': 0,
        }
        if attrs:
            self.__attrs.setAttrs(attrs)

    def __str__(self):
        return f'''{self.__class__}
        Table name -> {self._table}
        Attributes -> {self.attrs()}
        Hidden -> {self._hidden} 
        Driver -> {self._drive}
        Primary Key -> {self._primaryKey}\n'''

    def __reset(self):
        self._query_segments = {
            'INNER JOIN': {},
            'LEFT JOIN': {},
            'RIGHT JOIN': {},
            'WHERE': [],
            'OR': [],
            'GROUP BY': [],
            'ORDER BY': None,
            'LIMIT': 0,
            'OFFSET': 0,
        }
        self._values = []

    @classmethod
    def all(cls):
        """get all data of the table  contains all fields"""
        return cls().get()

    @classmethod
    def objects(cls, attrs: dict = None):
        return cls(attrs)

    def attrs(self):
        return self.__attrs.all()

    def attrsExcept(self, *args):
        return self.__attrs.exceptAttr(args)

    def attrsOnly(self, *args):
        return self.__attrs.only(args)

    def save(self):
        if not self.__attrs.hasAny():
            self.__connection.save()
            return self
        return self.__saveObject()

    def get(self, collection=True) -> Collection or Collect:
        records = Connection().get(QueryStrBuilder().build(
            self._table,
            self._query_segments,
            self._columns + self._with_columns,
            self.__query_type__,
            self._drive
        ), tuple(self._values))
        if collection: return Collection(records, self)
        return Collect(records)

    def close(self):
        self.__connection.close()
        return self

    def first(self):
        self.__attrs.setAttrs(self.__connection.first())
        return self

    def query(self):
        return self.__connection.showQuery()

    def query2(self):
        return self.__connection.test()

    def fetch_mode(self, cursors_type: str):
        self.__connection.set_cursor_type(cursors_type)
        return self

    def last_one(self) -> int:
        return self.__connection.last_one()

    def count(self):
        return self.__connection.count()

    def select(self, *args):
        """takes args and get  data of the table with your own fields"""
        self.__connection.queryObj.columns = list(args)
        self.__connection.queryObj.query_type = 'select'
        return self

    def where(self, column: str, value, operator: str = "=", ):
        """
        * :param column: string
        * :param value: any
        * :param operator: str
        * :return class
        add where to query takes column:str, value:any and optional(operator:str)
        """
        self.__connection.queryObj.query_segments['WHERE'].append(
            self._drive.where().format(condition=column, operator=operator))
        self.__connection.queryObj.values.append(value)
        return self

    def orWhere(self, condition: str, value: str, operator: str = "="):
        """
        add or statement to query
        * :param condition
        * :param value
        * :param operator by default =
        """
        self.__connection.queryObj.query_segments['OR'].append(
            self._drive.where().format(condition=condition, operator=operator))
        self.__connection.queryObj.values.append(value)
        return self

    def between(self, column: str, start, end):
        """
        add where-between to query
        * :param column
        * :param start
        * :param end
        * :returns class
        """
        self.__connection.queryObj.query_segments['WHERE'].append(
            self._drive.between().format(column=column, start=start, end=end))
        self.__connection.queryObj.values.append(start)
        self.__connection.queryObj.values.append(end)

        return self

    def delete(self):
        """
        add delete to query
        * :return None
        """
        self.__connection.queryObj.query_type = 'delete'
        if hasattr(self, self._primaryKey):
            self.where('id', self.__getattribute__(self._primaryKey))
            self.__connection.save()
            return
        return self

    def orderBy(self, column: str, how: str = "ASC"):
        """
        add order by to query
        * :parameter column:str
        * :parameter how:str by default = ASC
        * :return: class
        """
        self.__connection.queryObj.query_segments['ORDER BY'] = '{column} {how}'.format(column=column, how=how)
        return self

    def offset(self, count: int):
        self.__connection.queryObj.query_segments['OFFSET'] = count
        return self

    def create(self, **kwargs):
        """
        * add insert statement to query with single values
        * :param kwargs: column's names as key value as value
        * :return: class
        """
        self.__connection.queryObj.query_type = 'insert'
        self.__connection.queryObj.columns = list(kwargs.keys())
        self.__connection.queryObj.values = self.__connection.queryObj.values + list(kwargs.values())
        if self.__attrs.hasAny():
            return self.objects(**{**kwargs, 'id': self.__connection.save().last_one()})
        self.__setattr__('id', self.__connection.save().last_one())
        return self

    def createMany(self, **kwargs):
        """
        * add insert statement to query with multiple values
        * :param kwargs: column's names as key values of columns as value
        * :return: class
        """
        # for item in zip(*list(kwargs.values())):
        #     self._values.append(item)
        return self.__connection.saveMany()

    def update(self, **kwargs):
        """
        add update statement to query
        * :param kwargs: column's names as key value of columns as value
        * :return: class
        """
        self.__connection.queryObj.columns = list(kwargs.keys())
        self.__connection.queryObj.query_type = 'update'
        self.__connection.queryObj.values = self.__connection.queryObj.values + list(kwargs.values())
        return self

    def sqlRaw(self, sql: str):
        """
        add row sql to query
        * :param sql: sql statement
        * :return: class
        """
        # self.__connection.queryObj = sql
        return self

    def groupBy(self, column: str):
        self.__connection.queryObj.query_segments['GROUP BY'] = f"{column}"
        return self

    def limit(self, count: int):
        self.__connection.queryObj.query_segments['LIMIT'] = count
        return self

    def join(self, table: str, first: str, second: str, operator: str = "=", callback=None):
        self.__connection.queryObj.query_segments['INNER JOIN'][table] = 'ON {first} {operator} {second}'.format(
            first=first, second=second, operator=operator)
        if callable(callback):
            callback(self.__SubJoin(self.__connection.queryObj, self.__connection.queryObj.query_segments['INNER JOIN'],
                                    table))
        return self

    def leftJoin(self, table: str, first: str, second: str, operator: str = "=", callback=None):
        self.__connection.queryObj.query_segments['LEFT JOIN'][table] = 'ON {first} {operator} {second}'.format(
            first=first, second=second, operator=operator)
        if callable(callback):
            callback(self.__SubJoin(self.__connection.queryObj, self.__connection.queryObj.query_segments['LEFT JOIN'],
                                    table))
        return self

    def rightJoin(self, table: str, first: str, second: str, operator: str = "=", callback=None):
        self.__connection.queryObj.query_segments['RIGHT JOIN'][table] = 'ON {first} {operator} {second}'.format(
            first=first, second=second, operator=operator)
        if callable(callback):
            callback(self.__SubJoin(self.__connection.queryObj, self.__connection.queryObj.query_segments['RIGHT JOIN'],
                                    table))
        return self

    def __saveObject(self):
        if self.__attrs.has(self._primaryKey):
            self.update(
                **self.attrsExcept(self._primaryKey)
            ).where("id", self.__getattribute__(self._primaryKey)).save()
            return self
        return self.create(**self.attrs())

    def find(self, value, colum: str = None):
        val = self.where(colum or self._primaryKey, value).first()
        if val:
            self.__attrs.setAttrs(val)
            return self
        return None

    @staticmethod
    def selectAll(query: str, bind=(), *, fetch_mode='dict'):
        con = Connection()
        con.set_cursor_type(fetch_mode)
        return con.__getattribute__('_query')(query, bind).cursor.fetchall()

    @staticmethod
    def selectOne(query: str, bind=(), *, fetch_mode='dict'):
        con = Connection()
        con.set_cursor_type(fetch_mode)
        return con.__getattribute__('_query')(query, bind).cursor.fetchone()

    @staticmethod
    def statement(query: str, bind=()):
        con = Connection()
        return con.__getattribute__('_query')(query, bind).db.commit()

    def With(self, reals: list):
        for real in reals:
            self.__getattribute__(real)().eager_load()
        return self

    class _HasOne:
        def __init__(self, cls, foreign_key: str, related, local_key: str = 'id'):
            self.__cls = cls()
            self.__related = related
            self.__foreign_key = foreign_key
            self.__local_key = local_key

        def eager_load(self):
            table = str.lower(self.__cls.__getattribute__('_table'))
            columns = (
                f'''(select json_object({','.join([f'"{item}",{item}' for item in getattr(self.__cls, 'fillable', [])])}) from {table} where {table}.{self.__foreign_key} = {getattr(self.__related, '_table')}.{self.__local_key}) as {table}_ '''
            )
            getattr(self.__related, '_with_columns').append(columns)
            return self

        def sql(self):
            sql, values = self.__cls.query()
            return

    class __SubJoin:
        def __init__(self, queryObj, join, table):
            self.__queryObj = queryObj
            self.__join = join
            self.__table = table

        def on(self, first: str, second: str = "%s", operator: str = '=', value=None):
            self.__join[self.__table] += ' AND {first} {operator} {second}'.format(
                first=first, second=second, operator=operator)
            if value is not None:
                self.__queryObj.values.append(value)
            return self

        def orOn(self, first: str, second: str = "%s", operator: str = '=', value=None):
            if value is not None:
                self.__queryObj.values.append(value)

            self.__join[self.__table] += ' OR {first} {operator} {second}'.format(
                first=first, second=second, operator=operator)

            return self

        def where(self):
            pass

        def orWhere(self):
            pass

    def subSelect(self, query, alias):
        self.__connection.queryObj.columns.append(self._drive.subSelect().format(query=query, alias=alias))
        return self

    def whereRaw(self, sql):
        self.__connection.queryObj.query_segments['WHERE'].append(sql)
        return self

    def orWhereRaw(self, sql):
        self.__connection.queryObj.query_segments['OR'].append(sql)
        return self

    class __SubSelect:
        def __init__(self, queryObj):
            self.__queryObj = queryObj

        def select(self, *args):
            pass

        def From(self, table):
            pass

    class Attributes:
        def __init__(self, cls):
            self.__cls = cls

        def all(self):
            return {key: value for key, value in vars(self.__cls).items() if not key.startswith('_')}

        def exceptAttr(self, attrs):
            return {key: value for key, value in vars(self.__cls).items() if
                    not key.startswith('_') and key not in attrs}

        def only(self, attrs):
            return {key: value for key, value in vars(self.__cls).items() if not key.startswith('_') and key in attrs}

        def setAttrs(self, attrs: dict):
            for key, value in attrs.items():
                if key not in self.__cls.__getattribute__('_hidden'):
                    if key.endswith('_'):
                        self.__cls.__setattr__(key.rstrip('_'), loads(value))
                    else:
                        self.__cls.__setattr__(key, value)
            return self

        def has(self, attr):
            return hasattr(self.__cls, attr)

        def hasAny(self):
            return not not self.all()
