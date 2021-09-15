from abc import ABC, abstractmethod
from weakref import proxy
import inspect


class Mediator(ABC):
    @abstractmethod
    def send(self, message):
        pass


class Friend(ABC):
    def __init__(self, mediator: Mediator):
        self._mediator = proxy(mediator)

    @abstractmethod
    def send(self, message):
        pass

    @abstractmethod
    def receive(self, message):
        pass


class CommunicationViber(Mediator):
    def __init__(self):
        self._first = None
        self._second = None

    def set_first(self, first: Friend):
        self._first = first

    def set_second(self, second: Friend):
        self._second = second

    def send(self, message):
        sender = inspect.currentframe().f_back.f_locals['self']
        receiver = self._first if sender == self._second else self._second
        receiver.receive(message)


class FirstFriend(Friend):
    def send(self, message):
        self._mediator.send(message)

    def receive(self, message):
        print(f'Первый друг получил сообщение: {message}')


class SecondFriend(Friend):
    def send(self, message):
        self._mediator.send(message)

    def receive(self, message):
        print(f'Второй друг прочитал сообщение в Viber: {message}')


def client_code():
    print('Вывод:')
    viber = CommunicationViber()
    first = FirstFriend(viber)
    second = SecondFriend(viber)
    viber.set_first(first)
    viber.set_second(second)
    first.send('Привет, как дела?')
    second.send('Привет, хорошо.')


client_code()