from abc import ABC

from inc.db.assets.DBStatementInterface import IDBStatement


class Mysql(IDBStatement):

    def disable_keys(self):
        return 'SET FOREIGN_KEY_CHECKS = 0'

    def enable_keys(self):
        return 'SET FOREIGN_KEY_CHECKS = 1'

    def truncate(self):
        return 'TRUNCATE TABLE {name}'

    def create_schema(self):
        return '''CREATE DATABASE IF NOT EXISTS {name} DEFAULT CHARACTER SET utf8mb4 COLLATE  utf8mb4_0900_ai_ci
         DEFAULT ENCRYPTION='N'; '''

    def drop_schema(self):
        return ''' DROP DATABASE IF EXISTS {name};'''

    def create_table(self):
        return "CREATE TABLE IF NOT EXISTS {name} ({columns});"

    def drop_table(self):
        return 'DROP TABLE IF EXISTS {name}'

    def selectDistinct(self):
        return "SELECT DISTINCT  {columns} FROM {table}"

    def __str__(self):
        return 'MySql'

    def subSelect(self) -> str:
        return '({query}) as {alias}'

    def separator(self, key) -> str:
        separator_dic = {
            'INNER JOIN': ' INNER JOIN ',
            'RIGHT JOIN': ' RIGHT JOIN ',
            'LEFT JOIN': ' LEFT JOIN ',
            'GROUP BY': ',',
            'OR': ' OR ',
            'WHERE': ' AND '
        }
        return separator_dic[key]

    def delete(self) -> str:
        return "DELETE FROM {table}"

    def join(self) -> str:
        return '{type} JOIN {foreign_table}'

    def fullJoin(self) -> str:
        return '{type} JOIN {foreign_table} ON {first} {operator} {second}'

    def groupBy(self) -> str:
        return 'GROUP BY {column}'

    def orderBy(self) -> str:
        return 'ORDER BY {column} {how}'

    def on(self) -> str:
        return ''

    def limit(self) -> str:
        return 'limit {count}'

    def between(self) -> str:
        return '{column} BETWEEN %s AND %s'

    def select(self) -> str:
        return "SELECT {columns} FROM {table}"

    def insert(self) -> str:
        return 'INSERT INTO {table} ({columns}) values({placeholder})'

    def update(self) -> str:
        return 'UPDATE {table} SET {columns}'

    def where(self) -> str:
        return '{condition} {operator} %s'

    def orWhere(self) -> str:
        return 'OR {condition} {operator} %s'

    def whereExists(self) -> str:
        return '{column} BETWEEN %s AND %s'

    def whereNotExists(self) -> str:
        return ''

    def whereNotNull(self) -> str:
        return '{column} IS NOT NULL'

    def whereNull(self) -> str:
        return '{column} IS NULL'

    def selectCount(self) -> str:
        return 'SELECT COUNT({columns}) FROM {table}'

    def selectSum(self) -> str:
        return 'SELECT SUM({columns}) FROM {table}'

    def selectAvg(self) -> str:
        return 'SELECT AVG({columns}) FROM {table}'
