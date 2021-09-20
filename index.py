from modules.product.ProductModel import ProductModel
from modules.users.UserModel import UserModel
from inc.db.BaseModel import BaseModel

model = UserModel()
# model = ProductModel()
model.create(("user model", "123456798", "مدير", "1", "1")).save()
