from inc.db.BaseModel import BaseModel


class OrdersItems(BaseModel):
    def __init__(self):
        super(OrdersItems, self).__init__()
        self.table_name = "order_items"

    def order(self):
        return self.belongsTo("orders", "order_id")
