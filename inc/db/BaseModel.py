from inc.db.Connection import Connection


class BaseModel(Connection):
    def __init__(self):
        super(BaseModel, self).__init__()
        self.table_name = None
        self.fields = ""

    def get_all(self):
        self.cursor.execute(f"select * from {self.table_name}")
        return self.all()

    def query(self, query, values=None):
        self.cursor.execute(str(query), values)
        return self

    def get_fields(self, fields=None):
        if fields is None:
            fields = self.fields
        self.cursor.execute(f"select {fields} from {self.table_name}")
        return self
