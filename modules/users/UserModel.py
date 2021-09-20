from inc.db.BaseModel import BaseModel


class UserModel(BaseModel):
    def __init__(self):
        super(UserModel, self).__init__()
        self.table_name = 'users'
        self.fields = "username ,password ,permissions ,close, reverse"
