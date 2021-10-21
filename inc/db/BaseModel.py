from inc.db.Connection import Connection

SELECT_STATEMENT = "SELECT {columns} FROM {table}"
DELETE_STATEMENT = "DELETE  FROM {table}"
WHERE_STATEMENT = " WHERE {condition} {operator} %s"
OR_STATEMENT = " OR {condition} {operator} %s"
BETWEEN_STATEMENT = " WHERE {column} BETWEEN %s AND %s"
INSERT_STATEMENT = "INSERT  INTO {table} ({columns}) values({placeholder})"
UPDATE_STATEMENT = "update {table} set {columns}"
ORDERBY_STATEMENT = " ORDER BY {column} {how}"


class BaseModel(Connection):
    def __init__(self):
        super(BaseModel, self).__init__()
        self._table_name = str(self.__class__.__name__).replace("Model", "").lower()
        self._statement = SELECT_STATEMENT.format(table=self._table_name, columns="*")

    def all(self):
        """ get all data of the table  contains all fields """
        self._statement = SELECT_STATEMENT.format(table=self._table_name, columns="*")
        return self.get()

    def select(self, *args) -> self:
        """ takes args and get  data of the table with your own fields"""
        self._statement = SELECT_STATEMENT.format(table=self._table_name, columns=",".join(args))
        return self

    def where(self, condition: str, value, operator: str = "=", ) -> self:
        """"""
        if "WHERE" in self._statement:
            self._statement += f" and {WHERE_STATEMENT.format(condition=condition, operator=operator)}"
        else:
            self._statement += WHERE_STATEMENT.format(condition=condition, operator=operator)
        self._values.append(value)
        return self

    def orWhere(self, condition: str, value: str, operator: str = "=") -> self:
        self._statement += OR_STATEMENT.format(condition=condition, operator=operator)
        self._values.append(value)
        return self

    def between(self, column: str, start, end) -> self:
        self._statement += BETWEEN_STATEMENT.format(column=column, start=start, end=end)
        self._values.append(start)
        self._values.append(end)
        return self

    def delete(self) -> self:
        """"""
        self._statement += DELETE_STATEMENT.format(table=self._table_name)
        return self

    def orderBy(self, column: str, how: str = "ASC") -> self:
        self._statement += ORDERBY_STATEMENT.format(column=column, how=how)
        return self

    def create(self, **kwargs) -> self:
        """"""
        placeholder = ""
        last_key = list(kwargs)[-1]
        for key, value in kwargs.items():
            if key == last_key:
                placeholder += "%s"
            else:
                placeholder += "%s,"
            self._values.append(value)
        self._statement = INSERT_STATEMENT.format(table=self._table_name, columns=",".join(kwargs.keys()),
                                                  placeholder=placeholder)
        return self

    def createMany(self, columns: list, values: list) -> self:
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
        self._statement = INSERT_STATEMENT.format(table=self._table_name, columns=columns_, placeholder=placeholder)
        for value in values:
            self._values.append(value)
        return self

    def update(self, **kwargs) -> self:
        """"""
        last_key = list(kwargs)[-1]
        columns = ""
        for key, value in kwargs.items():
            if key == last_key:
                columns += f"{key}=%s"
            else:
                columns += f"{key}=%s,"
            self._values.append(value)
        self._statement = UPDATE_STATEMENT.format(table=self._table_name, columns=columns)
        return self

    def sqlRow(self, sql) -> self:
        self._statement += sql
        return self
