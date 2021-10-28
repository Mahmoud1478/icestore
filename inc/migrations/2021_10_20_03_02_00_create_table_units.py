from inc.db.table import Table
            
            
class Units(Table):

    def up(self):
        return self._create(
            self.column(name="id", type="int", primary=True, auto_increment=True, unsigned=True),
            self.column(name="name", unique=True, type="str", size=45)
        )

    def down(self):
        return self._drop()