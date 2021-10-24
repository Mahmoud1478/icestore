from inc.db.BaseModel import BaseModel


class Ordersitems(BaseModel):
    def __init__(self):
        super(Ordersitems, self).__init__()
        self._setTable("order_items")

    def order(self):
        return self._belongsTo("orders", "id", "order_id")
