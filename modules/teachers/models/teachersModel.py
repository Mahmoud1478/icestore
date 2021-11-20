from inc.db.BaseModel import BaseModel


class Teachers(BaseModel):
    def __init__(self, **kwargs):
        super(Teachers, self).__init__(**kwargs)

    @property
    def students(self):
        return self._belongsToMany("students", "teachers_students", "student_id", "teacher_id")
