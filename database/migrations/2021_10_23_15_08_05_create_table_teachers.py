from database.inc.table import Table
            
            
class Teachers(Table):

    def up(self):
        return self._create(
            self.column(name="id", type="int", primary=True, auto_increment=True, unsigned=True),
            self.column(name="fname", type="str", size=45),
            self.column(name="lname", type="str", size=45),
            self.column(name="age", type="tinyint"),
        )

    def down(self):
        return self._drop() 