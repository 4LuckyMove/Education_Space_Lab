from abc import ABC, abstractmethod


class Unit(ABC):
    def __init__(self, speed: int):
        self._speed = speed

    def hit_and_run(self):
        self._move('вперед')
        self._stop()
        self._attack()
        self._move('назад')

    @abstractmethod
    def _attack(self):
        pass

    @abstractmethod
    def _stop(self):
        pass

    def _move(self, direction):
        self._output(f'движеться {direction} со скоростью {self._speed}')

    def _output(self, message):
        print(f'Отряд типа {self.__class__.__name__} {message}')


class Archer(Unit):
    def _attack(self):
        self._output('обстреливает врагов')

    def _stop(self):
        self._output('остановился в 100 шагах от врага')


class ArmeHorse(Unit):
    def _attack(self):
        self._output('на полном скаку врезается во вражеский строй')

    def _stop(self):
        self._output('летит вперед, не останавливаясь')


if __name__ == '__main__':
    print('ВЫВОД:')
    archers = Archer(4)
    archers.hit_and_run()
    print('-' * 65)
    cavalry = ArmeHorse(8)
    cavalry.hit_and_run()