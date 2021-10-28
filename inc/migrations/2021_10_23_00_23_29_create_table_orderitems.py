from inc.db.table import Table


class Orderitems(Table):
    def __init__(self):
        super(Orderitems, self).__init__()
        self._name = "order_items"

    def up(self):
        return self._create(
            self.column(name="id", type="int", primary=True, auto_increment=True, unsigned=True),
            self.column(name="product", type="str", size=50, ),
            self.column(name="count", type="int", default=1, ),
            self.column(name="order_id", type="int", unsigned=True, foreignkey={
                "ref": "orders",
                "on": "id",
                "onDelete": "CASCADE",
                "onUpdate": "CASCADE"

            })
        )

    def down(self):
        return self._drop()
