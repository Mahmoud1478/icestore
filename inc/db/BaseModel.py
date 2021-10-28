# from inc.db.Connection import Connection
from inc.db.PConnection import Connection
from inspect import isclass
from globals import AutoLoader

SELECT_STATEMENT = "SELECT {columns} FROM {table}"
DELETE_STATEMENT = "DELETE  FROM {table}"
WHERE_STATEMENT = " WHERE {condition} {operator} %s"
OR_STATEMENT = " OR {condition} {operator} %s"
BETWEEN_STATEMENT = " WHERE {column} BETWEEN %s AND %s"
INSERT_STATEMENT = "INSERT  INTO {table} ({columns}) values({placeholder})"
UPDATE_STATEMENT = "update {table} set {columns}"
ORDERBY_STATEMENT = " ORDER BY {column} {how}"
GROUPBY_STATEMENT = " GROUP BY {column} "
HASMaNY_STATEMENT = " join {foreign_table} on {local_table}.id = {on}"
BLONGSTO_STATEMENT = " join {foreign_table} on {local_key} = {foreign_key}"
JOIN_STATEMENT = " JOIN {foreign_table}"
ON_JOIN_STATEMENT = " ON {local_key} = {foreign_key}"


class BaseModel(Connection):

    def __init__(self):
        super(BaseModel, self).__init__()
        self.__table_name: str = str(self.__class__.__name__).lower()
        self._statement: str = SELECT_STATEMENT.format(table=self.__table_name, columns="*")

    def all(self):
        """get all data of the table  contains all fields"""
        self._statement = SELECT_STATEMENT.format(table=self.__table_name, columns="*")
        return self.get()

    def select(self, *args):
        """takes args and get  data of the table with your own fields"""
        self._statement = SELECT_STATEMENT.format(table=self.__table_name, columns=",".join(args))
        return self

    def where(self, condition: str, value, operator: str = "=", ):
        """add where to query takes condition:str, value:any and optional(operator:str)"""
        if "WHERE" in self._statement:
            self._statement += f" and {WHERE_STATEMENT.format(condition=condition, operator=operator)}"
        else:
            self._statement += WHERE_STATEMENT.format(condition=condition, operator=operator)
        self._values.append(value)
        return self

    def whereID(self, ):
        """add where to query takes condition:str, value:any and optional(operator:str)"""
        if "WHERE" in self._statement:
            self._statement += f" and {WHERE_STATEMENT.format(condition='id', operator='=')}"
        else:
            self._statement += WHERE_STATEMENT.format(condition="id", operator='=')
        self._values.append(getattr(self, "id"))
        return self

    def orWhere(self, condition: str, value: str, operator: str = "="):
        """add or to query takes condition:str, value:any and optional(operator:str)"""
        self._statement += OR_STATEMENT.format(condition=condition, operator=operator)
        self._values.append(value)
        return self

    def between(self, column: str, start, end):
        """add where-between to query takes column:str, start:any and end:any"""
        self._statement += BETWEEN_STATEMENT.format(column=column, start=start, end=end)
        self._values.append(start)
        self._values.append(end)
        return self

    def delete(self):
        """add delete to query"""
        self._statement += DELETE_STATEMENT.format(table=self.__table_name)
        return self

    def orderBy(self, column: str, how: str = "ASC"):
        """add order by to query takes :parameter column:str, optional(how:str)"""
        self._statement += ORDERBY_STATEMENT.format(column=column, how=how)
        return self

    def create(self, **kwargs):
        """"""
        placeholder: str = ""
        last_key = list(kwargs)[-1]
        for key, value in kwargs.items():
            if key == last_key:
                placeholder += "%s"
            else:
                placeholder += "%s,"
            self._values.append(value)
        self._statement = INSERT_STATEMENT.format(table=self.__table_name, columns=",".join(kwargs.keys()),
                                                  placeholder=placeholder)
        return self

    def createMany(self, columns: list, values: list):
        """"""
        placeholder: str = ""
        columnsCount: int = len(columns)
        columns_: str = ""
        for i, column in enumerate(columns):
            if i == columnsCount - 1:
                placeholder += "%s"
                columns_ += column
            else:
                placeholder += "%s,"
        self._statement = INSERT_STATEMENT.format(table=self.__table_name, columns=columns_, placeholder=placeholder)
        for value in values:
            self._values.append(value)
        return self

    def update(self, **kwargs):
        """"""
        last_key: str = list(kwargs)[-1]
        columns: str = ""
        for key, value in kwargs.items():
            if key == last_key:
                columns += f"{key} = %s"
            else:
                columns += f"{key} = %s,"
            self._values.append(value)
        self._statement = UPDATE_STATEMENT.format(table=self.__table_name, columns=columns)
        return self

    def sqlRaw(self, sql: str):
        """:parameter sql:str add row sql to query"""
        self._statement = sql
        return self

    def _hasMany(self, className: str, foreign_key: str, local_key: str, module_name: str = None):
        model = AutoLoader.model(className) if module_name is None else AutoLoader.subModel(module_name, className)
        return model.where(foreign_key, getattr(self, local_key)).get()

    def _hasOne(self, className: str, foreign_key: str, local_key: str, module_name: str = None):
        model = AutoLoader.model(className) if module_name is None else AutoLoader.subModel(module_name, className)
        return model.where(foreign_key, getattr(self, local_key)).limit(1).first()

    def _hasOneObject(self, className: str, foreign_key: str, local_key: str, module_name: str = None):
        model = AutoLoader.model(className) if module_name is None else AutoLoader.subModel(module_name, className)
        return model.where(foreign_key, getattr(self, local_key)).limit(1).findObject()

    def _belongsTo(self, className: str, foreign_key: str, local_key: str, module_name: str = None):
        model = AutoLoader.model(className) if module_name is None else AutoLoader.subModel(module_name, className)
        return model.where(local_key, getattr(self, foreign_key)).limit(1).first()

    def _belongsToObject(self, className: str, foreign_key: str, local_key: str, module_name: str = None):
        model = AutoLoader.model(className) if module_name is None else AutoLoader.subModel(module_name, className)
        return model.where(local_key, getattr(self, foreign_key)).limit(1).findObject()

    def _belongsToMany(self, modelName: str, intermediateTable: str, foreign_key: str, local_key: str,
                       module_name: str = None):
        model = AutoLoader.model(modelName) if module_name is None else AutoLoader.subModel(module_name, modelName)
        return model.select(f"{modelName}.*").join(intermediateTable).on(
            f"{intermediateTable}.{foreign_key}",
            f"{modelName}.id").join(
            self.__table_name).on(f"{intermediateTable}.{local_key}", f"{self.__table_name}.id").where(
            f"{intermediateTable}.{local_key}", getattr(self, "id")).get()

    def groupBy(self, column: str):
        self._statement += GROUPBY_STATEMENT.format(column=column)
        return self

    def limit(self, count: int):
        self._statement += f" limit {count}"
        return self

    def _setTable(self, table: str):
        self.__table_name = table
        self._statement = SELECT_STATEMENT.format(table=self.__table_name, columns="*")

    def join(self, table: str):
        self._statement += JOIN_STATEMENT.format(foreign_table=table)
        return self

    def on(self, localKey: str, foreignKey: str):
        self._statement += ON_JOIN_STATEMENT.format(local_key=localKey, foreign_key=foreignKey)
        return self

    def __filterAttr(self) -> dict:
        column = {}
        for key, value in self.__dict__.items():
            if not isclass(value) and not callable(value) and key[0] != "_" and key != "id":
                column[key] = value
        return column

    def saveObjectChanges(self):
        column = self.__filterAttr()
        if hasattr(self, "id"):
            self.update(**column).saveObject()
        else:
            self.create(**column).save()
        return self
