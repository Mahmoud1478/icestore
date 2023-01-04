from .Collect import Collect


class Collection:
    def __init__(self, collection, cls=None):
        self.__collection = Collect(collection)
        self.__cls = cls

    def __iter__(self):
        if self.__cls:
            for item in self.__collection:
                yield self.__cls.objects(item)
        else:
            for item in self.__collection:
                yield item

    def __str__(self) -> str:
        return f''' {self.__class__.__name__}
        class -> {self.__cls.__class__.__name__}
        item -> {self.__collection}'''

    def __getitem__(self, item):
        return self.__cls.objects(self.__collection[item])

    @classmethod
    def new_instance(cls, collection, cls_=None):
        return cls(collection, cls_)

    def isEmpty(self) -> bool:
        return self.__collection.isEmpty()

    def contains(self, value, key: str or int = None) -> bool:
        return self.__collection.contains(value, key)

    def pluck(self, key):
        self.__collection = self.__collection.pluck(key)
        return self

    def length(self):
        return self.__collection.length()

    def unique(self):
        self.__collection = self.__collection.unique()
        return self

    def map(self, fn):
        self.__collection = self.__collection.map(fn)
        return self

    def countBYKey(self, key: str or int, value) -> int:
        return self.__collection.countBYKey(key, value)

    def filter(self, fn):
        self.__collection = self.__collection.filter(fn)
        return self

    def first(self):
        item = self.__collection.first()
        if item: return self.__cls.objects(item)
        return None

    def last(self):
        item = self.__collection.last()
        if item: return self.__cls.objects(item)
        return None

    def nth(self, number):
        item = self.__collection.nth(number)
        if item: return self.__cls.objects(item)
        return None

    def take(self, number: int):
        self.__collection = self.__collection.take(number)
        return self

    # def only(self, *args):
    #     result = []
    #     for item in self.__collection:
    #         dict_ = {key: value for key, value in item.items() if key in args}
    #         result.append(dict_)
    #     return result
    #
    # def Except(self, *args):
    #     result = []
    #     for item in self.__collection:
    #         dict_ = {key: value for key, value in item.items() if key not in args}
    #         result.append(dict_)
    #     return result

    def where(self, key, value):
        self.__collection = self.__collection.where(key, value)
        return self

    def whereIn(self, key: str or int, value: list):
        self.__collection = self.__collection.whereIn(key, value)
        return self

    def whereNotIn(self, key: str or int, value: list):
        self.__collection = self.__collection.whereNotIn(key, value)
        return self

    def whereBetween(self, key: str or int, start: int, end: int):
        self.__collection = self.__collection.whereBetween(key, start, end)
        return self

    def whereNotBetween(self, key: str or int, start: int, end: int):
        self.__collection = self.__collection.whereNotBetween(key, start, end)
        return self

    def sort(self, *, key=None, reverse: bool = False):
        self.__collection.sort(key=key, reverse=reverse)
        return self

    def reverse(self):
        self.__collection.reverse()
        return self

    def reverseBy(self, key: str or int):
        self.__collection.reverseBy(key)
        return self

    def sortBy(self, key, *, reverse=False):
        self.__collection.sortBy(key=key, reverse=reverse)
        return self

    def sum(self, key: str or int = None) -> int:
        return self.__collection.sum(key)

    def max(self, key=None) -> int:
        return self.__collection.max(key)

    def min(self, key=None) -> int:
        return self.__collection.min(key)

    def avg(self, key: str or int = None) -> float:
        return self.__collection.avg(key)
