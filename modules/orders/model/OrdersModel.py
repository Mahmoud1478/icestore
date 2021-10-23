from inc.db.BaseModel import BaseModel


class Orders(BaseModel):
    def __init__(self):
        super(Orders, self).__init__()

    def items(self):
        return self.hasMany("order_items", "order_id")