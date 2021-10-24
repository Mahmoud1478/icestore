from database.inc.table import Table


class Orders(Table):

    def up(self):
        return self._create(
            self.column(name="id", type="int", primary=True, auto_increment=True, unsigned=True),
            self.column(name="discount", type="str", size=45, default="0"),
            self.column(name="taxes", type="str", size=45, default="0"),
            self.column(name="total", type="str", size=45, default="0"),
            self.column(name="shift_id", type="str", size=45, default="0"),
            self.column(name="user_id", type="str", size=45, default="0")

        )

    def down(self):
        return self._drop()
