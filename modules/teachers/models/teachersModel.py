from inc.db.BaseModel import BaseModel


class Teachers(BaseModel):
    def __init__(self):
        super(Teachers, self).__init__()

    def students(self):
        return self._belongsToMany("students", "teachersstudents", "student_id", "teacher_id")
