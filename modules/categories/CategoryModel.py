from inc.db.BaseModel import BaseModel


class CategoryModel(BaseModel):
    def __init__(self):
        super(CategoryModel, self).__init__()
        self.table_name = "categories"
        self.fields = 'name'
