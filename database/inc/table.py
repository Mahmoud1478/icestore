from database.inc.Connection import Connection

CREATE_TABLE_STATEMENT = "CREATE TABLE IF NOT EXISTS {name} ({columns});"
DROP_TABLE_STATEMENT = "DROP TABLE IF EXISTS {name}"
CREATE_DATABASE_STATEMENT = '''CREATE DATABASE IF NOT EXISTS {name} DEFAULT CHARACTER SET utf8mb4 COLLATE 
utf8mb4_0900_ai_ci DEFAULT ENCRYPTION='N' '''


class Table(Connection):
    def __init__(self):
        super(Table, self).__init__()
        self._name = self.__class__.__name__

    def _create(self, *args):
        return self._query(
            CREATE_TABLE_STATEMENT.format(name=str(self._name).lower(), columns=",".join(args)))

    def _drop(self):
        return self._query(DROP_TABLE_STATEMENT.format(name=self._name).lower())

    def create_database(self):
        self._query(CREATE_DATABASE_STATEMENT.format(name="test"))

    def column(self, name: str, type: str, size: int = None, default=None, nullable: bool = True, unique: bool = False,
               primary: bool = False, auto_increment: bool = False, unsigned: bool = False, foreignkey: dict = None):
        column_string = ""
        column_string += name
        column_string += self.__column_type(type, size)
        column_string += self.__add_unsigned(unsigned)
        column_string += self.__add_auto_increment(auto_increment)
        column_string += self.__add_primary(primary)
        column_string += self.__add_unique(unique)
        column_string += self.__add_null(nullable)
        column_string += self.__add_default(default)
        column_string += self.__add_foreign_key(name, foreignkey)
        return column_string

    @staticmethod
    def __column_type(type: str, size: int):
        size_ = f'({size})' if size is not None else ''
        if type.lower() == "int":
            return f" INTEGER{size_}"
        elif type.lower() == "str":
            return f" VARCHAR{size_}"
        elif type.lower() == "date":
            return
        elif type.lower() == "time":
            return
        elif type.lower() == "datetime":
            return
        elif type.lower() == "tinyint":
            return " TINYINT"
        elif type.lower() == "bigint":
            return " BIGINT"
        elif type.lower() == "":
            return
        elif type.lower() == "":
            return
        elif type.lower() == "":
            return
        else:
            return f" VARCHAR{size_}"

    @staticmethod
    def __add_primary(primary: bool):
        if primary:
            return " PRIMARY KEY"
        return ""

    @staticmethod
    def __add_default(default):
        if default is not None:
            return f" DEFAULT {default}"
        return ""

    @staticmethod
    def __add_auto_increment(auto_increment: bool):
        if auto_increment:
            return " AUTO_INCREMENT"
        return ""

    @staticmethod
    def __add_null(nullable: bool):
        if not nullable:
            return " NOT NULL"
        return ""

    @staticmethod
    def __add_unsigned(unsigned: bool):
        if unsigned:
            return " UNSIGNED"
        return ""

    @staticmethod
    def __add_unique(unique: bool):
        if unique:
            return f" UNIQUE"
        return ""

    @staticmethod
    def __add_foreign_key(name: str, foreignkey: dict):
        if foreignkey is not None:
            return f''' ,FOREIGN KEY ({name}) REFERENCES {foreignkey["ref"]}({foreignkey["on"]}) 
            ON DELETE {foreignkey["onDelete"]} ON UPDATE {foreignkey["onUpdate"]} '''
        return ""
