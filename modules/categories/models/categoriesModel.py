from inc.db.BaseModel import BaseModel


class Categories(BaseModel):
    def __init__(self, attrs: dict = None):
        super(Categories, self).__init__(attrs)
