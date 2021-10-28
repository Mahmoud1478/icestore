from inc.db.BaseModel import BaseModel


class Users(BaseModel):
    def __init__(self):
        super(Users, self).__init__()

    @property
    def shift(self):
        return self._hasOneObject("shifts", "user_id", "id")
