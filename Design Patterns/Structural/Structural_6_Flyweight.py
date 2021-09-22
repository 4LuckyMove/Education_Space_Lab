import json
from typing import Dict


class Flyweight:
    def __init__(self, shared_state: str):
        self._shared_state = shared_state

    def operation(self, unique_state: str):
        ss = json.dumps(self._shared_state)
        us = json.dumps(unique_state)
        print(f'Легковес: Отображение общего ({ss}) и уникального ({us}) состояния.', end='')


class FlyweightFactory:
    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: Dict):
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: Dict):
        return '_'.join(sorted(state))

    def get_flyweight(self, shared_state: Dict):
        key = self.get_key(shared_state)
        if not self._flyweights.get(key):
            print('Фабрика Легковеса: Не могу найти машину, создаю новую.')
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print('Фабрика Легковеса: Повторное использование существующего легковеса.')
        return self._flyweights[key]

    def list_flyweights(self):
        count = len(self._flyweights)
        print(f'Фабрика Легковеса: В наличии {count} машин.')
        print('\n'.join(map(str, self._flyweights.keys())), end='')


def add_car_to_db(factory: FlyweightFactory, plates: str, owner: str, brand: str, model: str, color: str):
    print('\n\nКлиент: Добавление машины в базу данных.')
    flyweght = factory.get_flyweight([brand, model, color])
    flyweght.operation([plates, owner])


if __name__ == '__main__':
    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2021", "yellow"],
        ["Mercedes-Benz", "G63", "black"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
        ["Mercedes-Benz", "C500", "red"],
    ])

    factory.list_flyweights()
    add_car_to_db(factory, 'AA6666AA', 'Волков Кирилл', 'BMW', 'M5', 'green')
    add_car_to_db(factory, 'АE4774EA', 'Краснов Дмитрий', 'Chevrolet', 'Camaro2018', "yellow")
    add_car_to_db(factory, 'AA6666AA', 'Волков Кирилл', 'BMW', 'M5', 'red')
    print("\n")
    factory.list_flyweights()