from functools import reduce
from collections import defaultdict
from itertools import groupby
from typing import Any


class Collect(list):
    def __init__(self, data):
        super(Collect, self).__init__(data)
        self.__operators = {
            '=': '',
            '<=': '',
            '>=': '',
            '<': '',
            '>': '',
        }

    @classmethod
    def new_instant(cls, data):
        return cls(data)

    def isEmpty(self) -> bool:
        return not self

    def contains(self, value, key: str or int = None) -> bool:
        if key is None: return value in self
        for item in self:
            if item[key] == value: return True
        return False

    def pluck(self, key: str or int):
        return self.new_instant(map(lambda item: item[key], self))

    def length(self) -> int:
        return len(self)

    def unique(self):
        return self.new_instant(list(set(self)))

    def map(self, fn):
        return self.new_instant(map(fn, self))

    def mapWithIdx(self, fn):
        return self.new_instant(map(fn, enumerate(self)))

    def countBYKey(self, key: str or int, value) -> int:
        return self.where(key, value).length()

    def first(self):
        try:
            return self[0]
        except IndexError:
            return None

    def last(self):
        try:
            return self[-1]
        except IndexError:
            return None

    def nth(self, number: int):
        try:
            return self[number]
        except IndexError:
            return None

    def take(self, number: int):
        return self.new_instant(self[0:number])

    def filter(self, fn):
        return self.new_instant(filter(fn, self))

    def where(self, key: str or int, value, operator: str = "=="):
        return self.filter(lambda item: item[key] == value)

    def whereIn(self, key: str or int, value: list):
        return self.filter(lambda item: item[key] in value)

    def whereNotIn(self, key: str or int, value: list):
        return self.filter(lambda item: item[key] not in value)

    def whereBetween(self, key: str or int, start: int, end: int):
        return self.filter(lambda item: start < item[key] < end)

    def whereNotBetween(self, key: str or int, start: int, end: int):
        return self.filter(lambda item: not start < item[key] < end)

    def sort(self: list, *, key=None, reverse: bool = False):
        super().sort(key=key, reverse=reverse)
        return self

    def reverse(self):
        super().reverse()
        return self

    def reverseBy(self, key: str or int):
        self.sort(key=lambda item: item[key], reverse=True)
        return self

    def sortBy(self, key: str or int, reverse: bool = False):
        self.sort(key=lambda item: item[key], reverse=reverse)
        return self

    def sum(self, key: str or int = None) -> int:
        if key is None: return sum(self)
        if callable(key): return sum(key(item) for item in self)
        return sum(item[key] for item in self)

    def max(self, key=None) -> int:
        return max(self, key=key)

    def min(self, key=None) -> int:
        return min(self, key=key)

    def avg(self, key: str or int = None) -> float:
        return self.sum(key) / self.length()

    def dif(self):
        pass

    def flatten(self):
        return self.new_instant(sum(self, []))

    def __itemTo(self, type_):
        def transFn(item):
            if isinstance(item, dict):
                return type_(item.values())
            if isinstance(item, type_):
                return item
            if isinstance(item, (str, int)):
                return type_([item])
            return type_(item)

        return self.map(transFn)

    def itemToList(self):
        return self.__itemTo(list)

    def itemToTuple(self):
        return self.__itemTo(tuple)

    def itemToDictionary(self, *keys: str):
        def transFn(item):
            if isinstance(item, (tuple, list)):
                return {key: value for key, value in zip(keys, item)}
            if isinstance(item, dict):
                return {key: value for key, value in zip(keys, item.values())}
            return {keys[0]: item}

        return self.map(transFn)

    def groupBy(self, key: str or int):
        return {key: list(value) for key, value in groupby(self, lambda item: item.pop(key))}

    def each(self, fn):
        for idx, item in enumerate(self):
            if not fn(idx, item): break
