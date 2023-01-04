from .statement import statement


class Query:
    def __init__(self):
        self.prefix = ''
        self.limit = ''
        self.group = ''
        self.where = ''
        self.join_ = ''
        self.or_ = ''
        self.order = ''

    def resolve(self):
        return self.prefix + self.join_ + self.where + self.or_ + self.group + self.order + self.limit

