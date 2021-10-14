from database.inc.Connection import Connection


class Table(Connection):
    def __init__(self):
        super(Table, self).__init__()
        self.__query_string = ""

    def create(self):
        pass
