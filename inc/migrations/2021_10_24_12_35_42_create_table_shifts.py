from inc.db.table import Table


class Shifts(Table):

    def up(self):
        return self._create(
            self.column(name="id", type="int", primary=True, auto_increment=True, unsigned=True),
            self.column(name="user_id", type="int", unsigned=True, foreignkey={
                "ref": "users",
                "on": "id",
                "onUpdate": "CASCADE",
                "onDelete": "SET NULL"
            }),
            self.column(name="real_total", type="int", default=0, ),
            self.column(name="bone", type="int", default=1),
            self.column(name="start", type="datetime", default="CURRENT_TIMESTAMP"),
            self.column(name="end", type="datetime", ),
        )

    def down(self):
        return self._drop()
