from inc.db.BaseModel import BaseModel


class Ordersitems(BaseModel):
    def __init__(self, attrs: dict = None):
        super(Ordersitems, self).__init__(attrs)
        self.table('order_items')
