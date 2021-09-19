from modules.product.ProductModel import ProductModel
from inc.db.BaseModel import BaseModel

# model = BaseModel()
model = ProductModel()
print(model.get_fields().all())

