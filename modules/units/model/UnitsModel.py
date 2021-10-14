from inc.db.BaseModel import BaseModel


class UnitsModel(BaseModel):
    def __init__(self):
        super(UnitsModel, self).__init__()
        self.__table_name = 'units'
        self.__fields = 'name',
