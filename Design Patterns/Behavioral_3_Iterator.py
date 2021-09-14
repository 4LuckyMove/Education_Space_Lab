from abc import ABC, abstractmethod


class Iterator(ABC):
    _error = None

    def __init__(self, collection, cursor):
        self._collection = collection
        self._cursor = cursor

    @abstractmethod
    def current(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def remove(self):
        pass

    def _raise_key_except(self):
        raise self._error(f'Коллекция класса {self.__class__.__name__} не находит ключ {self._cursor}')


class ListIterator(Iterator):
    _error = IndexError

    def __init__(self, collection: list):
        super().__init__(collection, 0)

    def current(self):
        if self._cursor < len(self._collection):
            return self._collection[self._cursor]
        self._raise_key_except()

    def next(self):
        if len(self._collection) >= self._cursor + 1:
            self._cursor += 1
            return self._collection[self._cursor]
        self._raise_key_except()

    def has_next(self):
        return len(self._collection) >= self._cursor + 1

    def remove(self):
        if 0 <= self._cursor < len(self._collection):
            self._collection.remove(self._collection[self._cursor])
        else:
            self._raise_key_except()


class DictionaryIterator(Iterator):
    _error = KeyError

    def __init__(self, collection: dict):
        super().__init__(collection, next(iter(collection)))
        self._keys = list(self._collection.keys())
        self._keys.pop(0)

    def current(self):
        if self._cursor in self._collection:
            return self._collection[self._cursor]
        self._raise_key_except()

    def next(self):
        if len(self._keys):
            self._cursor = self._keys.pop(0)
            return self._collection[self._cursor]
        else:
            self._raise_key_except()

    def has_next(self):
        return len(self._keys) > 0

    def remove(self):
        if self._cursor in self._collection:
            del self._collection[self._cursor]
            try:
                self.next()
            except self._error:
                raise KeyError(f'Коллекция типа {self.__class__.__name__} пуста.')
        else:
            self._raise_key_except()


class Collection(ABC):
    @abstractmethod
    def iterator(self):
        pass


class ListCollection(Collection):
    def __init__(self, collection: list):
        self._collection = collection

    def iterator(self):
        return ListIterator(self._collection)


class DictionaryCollection(Collection):
    def __init__(self, collection: dict):
        self._collection = collection

    def iterator(self):
        return DictionaryIterator(self._collection)


def client_code(title, collection: Collection):
    print(f'{title}')
    iterator = collection.iterator()
    print(iterator.current())
    iterator.next()
    print(iterator.next())
    iterator.remove()
    print(iterator.current())
    print(iterator.has_next())
    print('\n')


if __name__ == '__main__':
    print('Вывод теста:')
    client_code('Тестируем лист: ', ListCollection([1, 2, 3, 4, 5]))
    client_code('Тестируем словарь: ', DictionaryCollection({'a': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5}))