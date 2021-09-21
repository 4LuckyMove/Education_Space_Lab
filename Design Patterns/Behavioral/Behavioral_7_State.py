from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def find_food(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def dream(self):
        pass


class SleepState(State):
    def eat(self):
        return 'не может кушать, пока спит'

    def find_food(self):
        return 'во сне ищет еду'

    def move(self):
        return 'не может двигаться, пока спит'

    def dream(self):
        return 'спит и видит прекрасный сон'


class MainState(State):
    def eat(self):
        return 'начинает не спеша кушать моллюсков'

    def find_food(self):
        return 'находит вполне съедобную тушу выброшенную на берег'

    def move(self):
        return 'неуклюже ползет вдоль береговой линии'

    def dream(self):
        return 'замечтался об одной знакомой самке'


class WaterState(State):
    def eat(self):
        return 'кушать в воде не может'

    def find_food(self):
        return 'вспахивает бивням дно и ловит моллюсков'

    def move(self):
        return 'грациозно рассекает волны океана'

    def dream(self):
        return 'нет возможности спать и мечтать в воде'


class Walrus:
    def __init__(self, state: State):
        self._state = state

    def change_state(self, state: State):
        self._state = state

    def _execute(self, operation):
        try:
            func = getattr(self._state, operation)
            print(f'Морж {func()}')
        except AttributeError:
            print('Морж такого делать не умеет.')

    def eat(self):
        self._execute('eat')

    def find_food(self):
        self._execute('find_food')

    def move(self):
        self._execute('move')

    def dream(self):
        self._execute('dream')


if __name__ == '__main__':
    sleep = SleepState()
    main = MainState()
    in_water = WaterState()
    walrus = Walrus(main)

    print('ВЫВОД:')
    walrus.change_state(in_water)
    walrus.move()
    walrus.find_food()
    print('-' * 45)
    walrus.change_state(main)
    walrus.eat()
    walrus.move()
    walrus.dream()
    print('-' * 45)
    walrus.change_state(sleep)
    walrus.dream()
