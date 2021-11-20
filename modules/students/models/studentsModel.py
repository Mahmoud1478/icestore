from inc.db.BaseModel import BaseModel


class Students(BaseModel):
    def __init__(self,**kwargs):
        super(Students, self).__init__()

    @property
    def teachers(self):
        return self._belongsToMany("teachers", "teachersstudents", "teacher_id", "student_id")
