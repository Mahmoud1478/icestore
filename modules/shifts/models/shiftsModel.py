from inc.db.BaseModel import BaseModel


class Shifts(BaseModel):
    def __init__(self):
        super(Shifts, self).__init__()

    @property
    def user(self):
        return self._belongsTo("users", "user_id", "id")
