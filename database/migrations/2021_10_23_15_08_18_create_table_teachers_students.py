from database.inc.table import Table


class teachers_students(Table):

    def up(self):
        return self._create(
            self.column(name="student_id", type="int", unsigned=True, foreignkey={
                "ref": "students",
                "on": "id",
                "onUpdate": "CASCADE",
                "onDelete": "CASCADE"
            }),
            self.column(name="teacher_id", type="int", unsigned=True, foreignkey={
                "ref": "teachers",
                "on": "id",
                "onUpdate": "CASCADE",
                "onDelete": "CASCADE"
            }),

        )

    def down(self):
        return self._drop()
