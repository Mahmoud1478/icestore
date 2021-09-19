from inc.db.BaseModel import BaseModel


class ProductModel(BaseModel):
    def __init__(self):
        super(ProductModel, self).__init__()
        self.table_name = 'products'
        self.fields = "name ,category ,price ,port_name"
