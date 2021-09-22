from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class BaseComponent(ABC):
    @property
    def parent(self) -> BaseComponent:
        return self._parent

    @parent.setter
    def parent(self, parent: BaseComponent):
        self._parent = parent

    def add(self, component: BaseComponent):
        pass

    def remove(self, component: BaseComponent):
        pass

    def is_composite(self):
        return False

    @abstractmethod
    def operation(self):
        pass


class Product(BaseComponent):
    def operation(self):
        return 'Продукт'


class Composite(BaseComponent):
    def __init__(self):
        self._children: List[BaseComponent] = []

    def add(self, component: BaseComponent):
        self._children.append(component)
        component.parent = self

    def remove(self, component: BaseComponent):
        self._children.remove(component)
        component.parent = None

    def is_composite(self):
        return True

    def operation(self):
        result = []
        for child in self._children:
            result.append(child.operation())
        return f'Отделение({"+".join(result)})'


def client_code(component: BaseComponent):
    print(f'РЕЗУЛЬТАТ: {component.operation()}', end='')


def client_code2(component1: BaseComponent, component2: BaseComponent):
    if component1.is_composite():
        component1.add(component2)
    print(f'РЕЗУЛЬТАТ: {component1.operation()}', end='')


if __name__ == '__main__':
    simple = Product()
    print('Клиент: У меня есть простой компонент:')
    client_code(simple)
    print('\n')

    tree = Composite()

    branch1 = Composite()
    branch1.add(Product())
    branch1.add(Product())

    branch2 = Composite()
    branch2.add(Product())

    tree.add(branch1)
    tree.add(branch2)

    print('Клиент: Теперь у меня есть составное отделение:')
    client_code(tree)
    print('\n')

    print('Клиент: Мне не нужно проверять классы компонентов, даже при управлении отделением:')
    client_code2(tree, simple)