from inc.db.BaseModel import BaseModel


class CategoriesModel(BaseModel):
    def __init__(self):
        super(CategoriesModel, self).__init__()
        self._table_name = 'categories'
        self._fields = 'name',
