from inc.db.BaseModel import BaseModel


class Students(BaseModel):
    def __init__(self):
        super(Students, self).__init__()

    def teachers(self):
        return self._belongsToMany("teachers", "teachersstudents", "teacher_id", "student_id")
