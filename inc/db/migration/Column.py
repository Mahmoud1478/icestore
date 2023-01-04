class Column:

    def __init__(self, name: str, type_: str, size: int = None):
        self._segments = [name, type_.format(size=f'({size})' if size else '')]

    def __repr__(self):
        return ' '.join(self._segments)

    @classmethod
    def string(cls, name: str, *, size: int = 192):
        return cls(name, 'VARCHAR{size}', size)

    @classmethod
    def text(cls, name: str, *, size: int = 254):
        return cls(name, 'VARCHAR{size}', size)

    @classmethod
    def longText(cls, name):
        return cls(name, 'longtext')

    @classmethod
    def integer(cls, name: str, *, size: int = None):
        return cls(name, 'int{size}', size)

    @classmethod
    def tinyInteger(cls, name: str, *, size: int = None):
        return cls(name, 'tinyint{size}', size)

    @classmethod
    def smallInteger(cls, name: str, *, size: int = None):
        return cls(name, 'smallint{size}', size)

    @classmethod
    def bigInteger(cls, name: str, *, size: int = None):
        return cls(name, 'bigint{size}', size)

    @classmethod
    def id(cls, name: str = 'id'):
        return cls.bigInteger(name).primaryKey().increment().unsigned()

    @classmethod
    def date(cls, name):
        return cls(name)

    @classmethod
    def time(cls, name):
        return cls(name)

    @classmethod
    def datetime(cls, name):
        return cls(name)

    def test(self):
        return self._segments

    def unique(self):
        self._segments.append('unique')
        return self

    def nullable(self):
        return self.default('null')

    def notNull(self):
        self._segments.append('not null')
        return self

    def unsigned(self):
        self._segments.insert(2, 'unsigned')
        return self

    def primaryKey(self):
        self._segments.append('primary key')
        return self

    def increment(self):
        self._segments.append('auto_increment')
        return self

    def default(self, value):
        self._segments.append(f'default {value}')
        return self
