from inc.db.BaseModel import BaseModel
import importlib


class Orders(BaseModel):
    def __init__(self):
        super(Orders, self).__init__()

    def items(self):
        return self._hasMany("ordersitems", "id", "order_id", "orders")
