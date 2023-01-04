
class Sqlite:
    @staticmethod
    def delete() -> str:
        return "DELETE  FROM {table}"

    @staticmethod
    def join() -> str:
        return 'INNER JOIN {foreign_table}'

    @staticmethod
    def leftJoin() -> str:
        return 'LEFT JOIN {foreign_table}'

    @staticmethod
    def rightJoin() -> str:
        return 'RIGHT JOIN {foreign_table}'

    @staticmethod
    def groupBy() -> str:
        return 'GROUP BY {column}'

    @staticmethod
    def orderBy() -> str:
        return 'ORDER BY {column} {how}'

    @staticmethod
    def on() -> str:
        return ''

    @staticmethod
    def limit() -> str:
        return 'limit {count}'

    @staticmethod
    def between() -> str:
        return '{column} BETWEEN %s AND %s'

    @staticmethod
    def select() -> str:
        return "SELECT {columns} FROM {table}"

    @staticmethod
    def insert() -> str:
        return 'INSERT  INTO {table} ({columns}) values({placeholder})'

    @staticmethod
    def update() -> str:
        return 'update {table} set {columns}'

    @staticmethod
    def where() -> str:
        return 'WHERE {condition} {operator} %s'

    @staticmethod
    def whereOr() -> str:
        return 'OR {condition} {operator} %s'

    @staticmethod
    def whereExists() -> str:
        return '{column} BETWEEN %s AND %s'

    @staticmethod
    def whereNotExists() -> str:
        return ''

    @staticmethod
    def whereNotNull() -> str:
        return '{column} IS NOT NULL'

    @staticmethod
    def whereNull() -> str:
        return '{column} IS NULL'

    @staticmethod
    def selectCount() -> str:
        return 'SELECT COUNT({columns}) FROM {table}'

    @staticmethod
    def selectSum() -> str:
        return 'SELECT SUM({columns}) FROM {table}'

    @staticmethod
    def selectAvg() -> str:
        return 'SELECT AVG({columns}) FROM {table}'
