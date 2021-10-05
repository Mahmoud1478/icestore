from inc.db.Connection import Connection


class BaseModel(Connection):
    def __init__(self):
        super(BaseModel, self).__init__()
        self.table_name = None
        self.fields = ""

    def all(self):
        """ get all data of the table  contains all fields """
        self.query(f"select * from {self.table_name}")
        return self.get_all()

    def get_fields(self, *fields):
        """ get all data of the table contain your own fields
             requires 1 optional parameters
             (
                 fields => the fields which will get from table by default it is equal field's var
                            but you can change it by passing your own fields
             )
        """
        if len(fields) == 0:
            fields = self.fields
        target_field = ",".join(fields)
        return self.query(f"select {target_field} from {self.table_name}")

    def where(self, *args, bind="and", **kwargs):

        """
            get all data of the table   it requires 2 parameters
            (
                conditions => where the selection will happen it is a string separated by ',' .
                                and 2nd ele is the values of conditions

                values => the values of conditions it is a tuple contain the values in order of conditions' str var
            )
             and 1 optional parameter
             (
                fields => the fields which will select by default it is equal field's var but you can change it
                        by passing your own fields
             )
        """
        if len(args) == 0:
            args = self.fields
        conditions = ''
        last_key = list(kwargs.keys())[-1]
        for key, value in kwargs.items():
            val = str(value).split(" ")
            if last_key == key:
                conditions += f'{key} {val[0]} "{val[1]}"'
            else:
                conditions += f'{key} {val[0]} "{val[1]}" {bind} '
        # return f"select {','.join(args)} from {self.table_name} where {str(conditions)}"
        return self.query(f"select {','.join(args)} from {self.table_name} where {str(conditions)}")

    def between(self):
        pass

    def delete(self, bind="and", **kwargs):
        """
            insert things in database it requires 2 parameters
            (
                conditions => where the deleting will happen it is  a string separated by ',' .

                values => the values of conditions it is a tuple contain the values in order of
                           conditions' str var
            )
        """
        conditions = ''
        last_key = list(kwargs.keys())[-1]
        for key, value in kwargs.items():
            val = str(value).split(" ")
            if last_key == key:
                conditions += f'{key} {val[0]} "{val[1]}"'
            else:
                conditions += f'{key} {val[0]} "{val[1]}" {bind} '
        # return f"delete  from {self.table_name} where {conditions}"
        return self.query(f"delete  from {self.table_name} where {conditions}")

    def create(self, values, fields=None):
        """
           insert things in database it requires 1 parameters
            (
               values => the values which will inset in database it is a tuple contain the values in order of
                            field's var
            )
            and 1 optional parameter
            (
                fields => the fields which will update by default it is equal field's var but you can change it
                            by passing your own fields
            )
        """

        if fields is None:
            fields = self.fields
        placeholder = ""
        counter = len(values)
        for i in range(counter):
            if i < counter - 1:
                placeholder += '%s,'
            else:
                placeholder += '%s'
        return self.query(f"insert  into {self.table_name} ({fields}) values({placeholder})", values)

    def update(self, conditions, values, fields=None):
        """
            update things in database it requires 2 parameters
            (
                conditions => where the update will happen it is  a list 1st ele is the conditions
                                and 2nd ele is the values of conditions

                values => the values which will save in database it is a tuple contain the values in order
                            of field's var
            )
             and 1 optional parameter
             (
                fields=> the fields which will update by default it is equal field's var but you can change it
                        by passing your own fields
             )
        """
        if fields is None:
            fields = self.fields
        counter = len(values)
        fields_list = fields.split(",")
        placeholder = ""
        for i in range(counter):
            if i < counter - 1:
                placeholder += f'{fields_list[i]} = %s,'
            else:
                placeholder += f'{fields_list[i]} = %s'
            i += 1
        return self.query(f"update {self.table_name} set {placeholder} where {conditions[0]}", values + conditions[1])
