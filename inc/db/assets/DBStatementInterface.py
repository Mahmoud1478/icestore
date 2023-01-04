from abc import ABC, abstractmethod


class IDBStatement(ABC):

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def select(self) -> str:
        return ''

    @abstractmethod
    def subSelect(self) -> str:
        pass

    @abstractmethod
    def insert(self) -> str:
        return ''

    @abstractmethod
    def update(self) -> str:
        return ''

    @abstractmethod
    def where(self) -> str:
        return ''

    @abstractmethod
    def orWhere(self) -> str:
        return ''

    @abstractmethod
    def whereExists(self) -> str:
        return ''

    @abstractmethod
    def whereNotExists(self) -> str:
        return ''

    @abstractmethod
    def whereNotNull(self) -> str:
        return ''

    @abstractmethod
    def whereNull(self) -> str:
        return ''

    @abstractmethod
    def selectCount(self) -> str:
        return ''

    @abstractmethod
    def selectSum(self) -> str:
        return ''

    @abstractmethod
    def selectAvg(self) -> str:
        return ''

    @abstractmethod
    def delete(self) -> str:
        return ''

    @abstractmethod
    def join(self) -> str:
        return ''

    @abstractmethod
    @abstractmethod
    def groupBy(self) -> str:
        return ''

    @abstractmethod
    def orderBy(self) -> str:
        return ''

    @abstractmethod
    def on(self) -> str:
        return ''

    @abstractmethod
    def limit(self) -> str:
        return ''

    @abstractmethod
    def between(self) -> str:
        return ''

    @abstractmethod
    def fullJoin(self) -> str:
        return ''

    @abstractmethod
    def separator(self, key) -> str:
        pass

    @abstractmethod
    def selectDistinct(self):
        return ''

    @abstractmethod
    def create_schema(self):
        pass

    @abstractmethod
    def drop_schema(self):
        pass

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def drop_table(self):
        pass

    @abstractmethod
    def disable_keys(self):
        pass

    @abstractmethod
    def enable_keys(self):
        pass

    @abstractmethod
    def truncate(self):
        pass
