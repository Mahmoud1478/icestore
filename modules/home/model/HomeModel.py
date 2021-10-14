from inc.db.BaseModel import BaseModel


class HomeModel(BaseModel):
    def __init__(self):
        super(HomeModel, self).__init__()
        self.__table_name = 'home'
        self.__fields = "",
