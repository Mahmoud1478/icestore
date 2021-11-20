# from inc.db.Connection import Connection
from inc.db.PConnection import Connection
from globals import AutoLoader
from abc import ABC

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


class BaseModel(Connection, ABC):

    def __init__(self, **kwargs):
        self._columns: dict = {}
        for key, value in kwargs.items():
            self._columns[key] = value
        self.__table_name: str = str(self.__class__.__name__).lower()
        super(BaseModel, self).__init__()
        self._statement: str = SELECT_STATEMENT.format(table=self.__table_name, columns="*")

    def __getattribute__(self, key):
        data = object.__getattribute__(self, "_columns")
        if key in data:
            return data[key]
        return object.__getattribute__(self, key)

    def __setattr__(self, key, value):
        if key not in ["_columns", "_BaseModel__table_name", "_statement", "_Connection__cursor", "_Connection__db",
                       '_Connection__cursorType', "_values"]:
            data = object.__getattribute__(self, "_columns")
            data[key] = value
        else:
            object.__setattr__(self, key, value)

    def all(self):
        """get all data of the table  contains all fields"""
        self._statement = SELECT_STATEMENT.format(table=self.__table_name, columns="*")
        return self.get()

    def select(self, *args):
        """takes args and get  data of the table with your own fields"""
        self._statement = SELECT_STATEMENT.format(table=self.__table_name, columns=",".join(args))
        return self

    def where(self, condition: str, value, operator: str = "=", ):
        """
        * :param condition: string
        * :param value: any
        * :param operator: str
        * :return class
        add where to query takes condition:str, value:any and optional(operator:str)
        """
        self._statement += f" and {condition} {operator} %s" if "WHERE" in self._statement else WHERE_STATEMENT.format(
            condition=condition, operator=operator)
        self._values.append(value)
        return self

    def orWhere(self, condition: str, value: str, operator: str = "="):
        """
        add or statement to query
        * :param condition
        * :param value
        * :param operator by default =
        """
        self._statement += OR_STATEMENT.format(condition=condition, operator=operator)
        self._values.append(value)
        return self

    def between(self, column: str, start, end):
        """
        add where-between to query
        * :param column
        * :param start
        * :param end
        * :returns class
        """
        self._statement += f" AND {column} BETWEEN %s AND %s" if "WHERE" in self._statement else BETWEEN_STATEMENT.format(
            column=column, start=start, end=end)
        self._values.append(start)
        self._values.append(end)
        return self

    def delete(self):
        """
        add delete to query
        * :return: class
        """
        self._statement += DELETE_STATEMENT.format(table=self.__table_name)
        return self

    def orderBy(self, column: str, how: str = "ASC"):
        """
        add order by to query
        * :parameter column:str
        * :parameter how:str by default = ASC
        * :return: class
        """
        self._statement += ORDERBY_STATEMENT.format(column=column, how=how)
        return self

    def create(self, **kwargs):
        """
        * add insert statement to query with single values
        * :param kwargs: column's names as key value as value
        * :return: class
        """
        placeholder: str = ""
        last_key = list(kwargs)[-1]
        for key, value in kwargs.items():
            placeholder += "%s" if key == last_key else "%s,"

            self._values.append(value)
        self._statement = INSERT_STATEMENT.format(table=self.__table_name, columns=",".join(kwargs.keys()),
                                                  placeholder=placeholder)
        return self.save()

    def createMany(self, **kwargs):
        """
        * add insert statement to query with multiple values
        * :param kwargs: column's names as key values of columns as value
        * :return: class
        """
        self._statement = INSERT_STATEMENT.format(table=self.__table_name, columns=",".join(kwargs.keys()),
                                                  placeholder=",".join(["%s" for _ in range(len(kwargs.keys()))]))
        for item in zip(*list(kwargs.values())):
            self._values.append(item)
        return self.saveMany()

    def update(self, **kwargs):
        """
        add update statement to query
        * :param kwargs: column's names as key value of columns as value
        * :return: class
        """
        last_key: str = list(kwargs)[-1]
        columns: str = ""
        for key, value in kwargs.items():
            columns += f"{key} = %s" if key == last_key else f"{key} = %s,"
            self._values.append(value)
        self._statement = UPDATE_STATEMENT.format(table=self.__table_name, columns=columns)
        return self

    def sqlRaw(self, sql: str):
        """
        add row sql to query
        * :param sql: sql statement
        * :return: class
        """
        self._statement = sql
        return self

    # ******** relationships **************

    def _hasMany(self, model: str, foreign_key: str, local_key: str, module_name: str = None):
        modelClass = AutoLoader.model(model) if module_name is None else AutoLoader.subModel(module_name, model)
        return modelClass.where(local_key, self._columns[foreign_key])

    def _hasOne(self, className: str, foreign_key: str, local_key: str, module_name: str = None):
        model = AutoLoader.model(className) if module_name is None else AutoLoader.subModel(module_name, className)
        return model.where(foreign_key, self._columns[local_key]).limit(1).first()

    def _belongsTo(self, className: str, foreign_key: str, local_key: str, module_name: str = None):
        model = AutoLoader.model(className) if module_name is None else AutoLoader.subModel(module_name, className)
        return model.where(foreign_key, self._columns[local_key]).limit(1).first()

    def _belongsToMany(self, modelName: str, intermediateTable: str, foreign_key: str, local_key: str,
                       module_name: str = None):
        model = AutoLoader.model(modelName) if module_name is None else AutoLoader.subModel(module_name, modelName)
        return model.select(f"{modelName}.*") \
            .join(intermediateTable) \
            .on(f"{intermediateTable}.{foreign_key}", f"{modelName}.id").join(self.__table_name) \
            .on(f"{intermediateTable}.{local_key}", f"{self.__table_name}.id") \
            .where(f"{intermediateTable}.{local_key}", self._columns["id"])

    # ***************************************************************************
    def groupBy(self, column: str):
        self._statement += f" , {column}" if "GROUP BY" in self._statement else GROUPBY_STATEMENT.format(column=column)
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

    def saveObject(self):
        if "id" in self._columns:
            columnToUpdate = {**self._columns}
            obj_id = columnToUpdate.pop('id')
            self.update(**columnToUpdate).where("id", obj_id).save()
        else:
            self.create(**self._columns).save()
        return self

    def findObject(self):
        val = self.first()
        self._statement = SELECT_STATEMENT.format(table=self.__table_name, columns="*")
        self._values = []
        if val:
            for key, value in val.items():
                self._columns[key] = value
            return self
        return None
