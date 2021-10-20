from database.inc.table import Table


class Categories(Table):

    def up(self):
        self._create(
            self.column(name="id", type="int", primary=True, auto_increment=True, unsigned=True),
            self.column(name="name", unique=True, type="str", size=45)
        )

    def down(self):
        self._drop()
