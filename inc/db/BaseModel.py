from inc.db.Connection import Connection

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
BLONGSTO_STATEMENT = " join {local_table} on {foreign_table}.id = {on}"


class BaseModel(Connection):
    def __init__(self):
        super(BaseModel, self).__init__()
        self.table_name = str(self.__class__.__name__).lower()
        self._statement = SELECT_STATEMENT.format(table=self.table_name, columns="*")

    def all(self):
        """get all data of the table  contains all fields"""
        self._statement = SELECT_STATEMENT.format(table=self.table_name, columns="*")
        return self.get()

    def select(self, *args):
        """takes args and get  data of the table with your own fields"""
        self._statement = SELECT_STATEMENT.format(table=self.table_name, columns=",".join(args))
        return self

    def where(self, condition: str, value, operator: str = "=", ):
        """add where to query takes condition:str, value:any and optional(operator:str)"""
        if "WHERE" in self._statement:
            self._statement += f" and {WHERE_STATEMENT.format(condition=condition, operator=operator)}"
        else:
            self._statement += WHERE_STATEMENT.format(condition=condition, operator=operator)
        self._values.append(value)
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
        self._statement += DELETE_STATEMENT.format(table=self.table_name)
        return self

    def orderBy(self, column: str, how: str = "ASC"):
        """add order by to query takes :parameter column:str, optional(how:str)"""
        self._statement += ORDERBY_STATEMENT.format(column=column, how=how)
        return self

    def create(self, **kwargs):
        """"""
        placeholder = ""
        last_key = list(kwargs)[-1]
        for key, value in kwargs.items():
            if key == last_key:
                placeholder += "%s"
            else:
                placeholder += "%s,"
            self._values.append(value)
        self._statement = INSERT_STATEMENT.format(table=self.table_name, columns=",".join(kwargs.keys()),
                                                  placeholder=placeholder)
        return self

    def createMany(self, columns: list, values: list):
        """"""
        placeholder = ""
        columnsCount = len(columns)
        columns_ = ""
        for i, column in enumerate(columns):
            if i == columnsCount - 1:
                placeholder += "%s"
                columns_ += column
            else:
                placeholder += "%s,"
        self._statement = INSERT_STATEMENT.format(table=self.table_name, columns=columns_, placeholder=placeholder)
        for value in values:
            self._values.append(value)
        return self

    def update(self, **kwargs):
        """"""
        last_key = list(kwargs)[-1]
        columns = ""
        for key, value in kwargs.items():
            if key == last_key:
                columns += f"{key}=%s"
            else:
                columns += f"{key}=%s,"
            self._values.append(value)
        self._statement = UPDATE_STATEMENT.format(table=self.table_name, columns=columns)
        return self

    def sqlRow(self, sql: str):
        """:parameter sql:str add row sql to query"""
        self._statement += sql
        return self

    def hasMany(self, table: str, on: str):
        self._statement += HASMaNY_STATEMENT.format(foreign_table=table, local_table=self.table_name, on=on)
        return self

    def belongsTo(self, table: str, on: str):
        self._statement += BLONGSTO_STATEMENT.format(foreign_table=table, local_table=self.table_name, on=on)
        return self

    def groupBy(self, column: str, how: str = "DESC"):
        self._statement += GROUPBY_STATEMENT.format(column=column)
        return self
