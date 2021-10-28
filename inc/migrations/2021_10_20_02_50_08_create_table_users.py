from inc.db.table import Table


class Users(Table):

    def up(self):
        return self._create(
            self.column(name="id", type="int", primary=True, auto_increment=True, unsigned=True),
            self.column(name="name", type="str", size=45, unique=True),
            self.column(name="password", type="str", size=45),
            self.column(name="permission", type="tinyint"),
        )

    def down(self):
        return self._drop()
