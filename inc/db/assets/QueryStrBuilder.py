from inc.db.assets.DBStatementClass.Mysql import Mysql


class QueryStrBuilder:

    def build(
        self,
        table: str,
        query_segments: dict,
        columns: list,
        query_type: str,
        driver,
    ):
        query = getattr(driver, query_type)().format(**self.__query_string_format(table, query_type, columns))
        for key, value in query_segments.items():
            if value:
                if isinstance(value, (str, int)):
                    query += f" {key} {value}"
                else:
                    query += self.__joinValues(key, value, driver.separator(key))
        return query

    @staticmethod
    def __joinValues(key: str, value, separator: str):
        if isinstance(value, list):
            return f' {key} {separator.join(value)} '
        elif isinstance(value, dict):
            return f' {key} ' + separator.join(f"{key_} {value_}" for key_, value_ in value.items())
        return ''

    @staticmethod
    def __query_string_format(table, type_, columns):
        query_format = {
            'select': {
                'table': table,
                'columns': ','.join(columns)
            },
            'update': {
                'table': table,
                'columns': ' = %s,'.join(columns) + '= %s'
            },
            'insert': {
                'table': table,
                'columns': ",".join(columns),
                'placeholder': ','.join('%s' for _ in range(len(columns)))
            },
            'delete': {
                'table': table
            },
        }
        return query_format[type_]
