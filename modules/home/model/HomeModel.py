from inc.db.BaseModel import BaseModel
            

class HomeModel(BaseModel):
    def __init__(self):
        super(HomeModel, self).__init__()
        self.table_name = 'home'
        self.fields = None