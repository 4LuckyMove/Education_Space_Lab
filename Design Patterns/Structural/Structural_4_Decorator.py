from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def operation(self):
        pass


class ReturnComponent(Component):
    def operation(self):
        return 'Меня зовут Компонент'


class Decorator(Component):
    _component = None

    def __init__(self, component: Component):
        self._component = component

    @property
    def component(self):
        return self._component

    def operation(self):
        return self._component.operation()


class DecoratorA(Decorator):
    def operation(self):
        return f'Декоратор А({self.component.operation()})'


class DecoratorB(Decorator):
    def operation(self):
        return f'Декоратор Б({self.component.operation()})'


def client_code(component: Component):
    print(f'РЕЗУЛЬТАТ: {component.operation()}', end='')


if __name__ == '__main__':
    simple = ReturnComponent()
    print('Клиент: У меня есть простой компонент:')
    client_code(simple)
    print('\n')

    decor1 = DecoratorA(simple)
    decor2 = DecoratorB(decor1)
    print('Клиент: Теперь у меня есть обернутый компонент:')
    client_code(decor2)