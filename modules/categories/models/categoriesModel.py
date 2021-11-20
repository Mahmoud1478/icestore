from inc.db.BaseModel import BaseModel


class Categories(BaseModel):
    def __init__(self, **kwargs):
        super(Categories, self).__init__(**kwargs)
