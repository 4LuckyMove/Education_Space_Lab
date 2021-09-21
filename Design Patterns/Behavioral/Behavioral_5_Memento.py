from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters, digits


class Memento(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_date(self):
        pass


class RecoveryMemento(Memento):
    def __init__(self, state):
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self):
        return self._state

    def get_name(self):
        return f'{self._date} / ({self._state[0:9]}...)'

    def get_date(self):
        return self._date


class Creator:
    _state = None

    def __init__(self, state):
        self._state = state
        print(f'Создатель: мое исходное состояние: {self._state}')

    def _generate_random_str(self, length: int = 10):
        return ''.join(sample(ascii_letters, length))

    def do_something(self):
        print('Создатель: я занят!')
        self._state = self._generate_random_str(30)
        print(f'Создатель: мое состояние изменилось: {self._state}')

    def save(self) -> Memento:
        return RecoveryMemento(self._state)

    def recovery(self, memento: RecoveryMemento):
        self._state = memento.get_state()
        print(f'Создатель: мое состояние изменилось: {self._state}')


class Guardian:
    def __init__(self, creator: Creator):
        self._mementos = []
        self._creator = creator

    def backup(self):
        print('\nОпекун: сохранение состояния Создателя...')
        self._mementos.append(self._creator.save())

    def undo(self):
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f'Опекун: восстановление состояния до: {memento.get_name()}')
        try:
            self._creator.recovery(memento)
        except Exception:
            self.undo()

    def show_history(self):
        print('Опекун: вот список снимков:')
        for memento in self._mementos:
            print(memento.get_name())


def client_code():
    creator = Creator('Язык программирования Python.')
    guardian = Guardian(creator)

    guardian.backup()
    creator.do_something()

    guardian.backup()
    creator.do_something()

    guardian.backup()
    creator.do_something()

    print('\n')
    guardian.show_history()

    print('\nКлиент: А теперь сделаем backup!\n')
    guardian.undo()

    print('\nКлиент: Еще раз!\n')
    guardian.undo()

client_code()