from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Observer(ABC):
    @abstractmethod
    def update(self, publisher):
        pass


class Publisher(ABC):
    @abstractmethod
    def register(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class NewsPublisher(Publisher):
    _state: int = None
    _observers: List[Observer] = []

    def register(self, observer: Observer):
        print('Издатель: добавлен новый подписчик.')
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        print('Издатель: рассылка уведомлений...')
        for observer in self._observers:
            observer.update(self)

    def some_b_logic(self):
        print('\nИздатель: я занят.')
        self._state = randrange(0, 10)

        print(f'Издатель: мое состояние изменилось на {self._state}')
        self.notify()


class SubscriberA(Observer):
    def update(self, publisher: NewsPublisher):
        if publisher._state < 5:
            print('Подписчик А: прочитал новое уведомление.')


class SubscriberB(Observer):
    def update(self, publisher: NewsPublisher):
        if publisher._state == 0 or publisher._state >= 3:
            print('Подписчик Б: прочитал новое уведомление.')


if __name__ == '__main__':
    publisher = NewsPublisher()

    subs_a = SubscriberA()
    publisher.register(subs_a)

    subs_b = SubscriberB()
    publisher.register(subs_b)

    publisher.some_b_logic()
    publisher.some_b_logic()

    publisher.detach(subs_a)
    publisher.some_b_logic()