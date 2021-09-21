from abc import ABC, abstractmethod
from typing import List


class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data: List):
        pass


class SortedStrategy(Strategy):
    def do_algorithm(self, data: List):
        return sorted(data)


class RevSortedStrategy(Strategy):
    def do_algorithm(self, data: List):
        return reversed(sorted(data))


class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        self._strategy = strategy

    def do_some_b_logic(self):
        print('Контекст: сортировка данных с использованием стратегии')
        result = self._strategy.do_algorithm(['a', 'b', 'c', 'd', 'e', 'f'])
        print(','.join(result))


if __name__ == '__main__':
    context = Context(SortedStrategy())
    print('Клиент: стратегия настроена на обычную сортировку.')
    context.do_some_b_logic()
    print('-' * 35)

    print('Клиент: стратегия настроена на обратную сортировку.')
    context = Context(RevSortedStrategy())
    context.do_some_b_logic()