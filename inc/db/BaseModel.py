from inc.db.Connection import Connection


class BaseModel(Connection):
    def __init__(self):
        super(BaseModel, self).__init__()
        self.table_name = None
        self.fields = ""

    def all(self):
        self.cursor.execute(f"select * from {self.table_name}")
        return self.get_all()

    def get_fields(self, fields=None):
        if fields is None:
            fields = self.fields
        return self.query(f"select {fields} from {self.table_name} ")

    def where(self, conditions, values, fields=None):
        if fields is None:
            fields = self.fields
        return self.query(f"select {fields} from {self.table_name} where {conditions}", values)

