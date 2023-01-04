from inc.db.BaseModel import BaseModel
from modules.shifts.models.Shift import Shifts


class Users(BaseModel):
    def __init__(self , attrs: dict = None):
        super(Users, self).__init__(attrs)
        self._hidden = ['password',]

    def shift(self):
        return self._HasOne(Shifts, 'user_id', self)
