from __future__ import annotations


class Facade:
    def __init__(self, subsys1: Subsystem1, subsys2: Subsystem2):
        self._subsys1 = subsys1 or Subsystem1()
        self._subsys2 = subsys2 or Subsystem2()

    def operation(self):
        result = []
        result.append('Фасад инициализирует подсистемы:')
        result.append(self._subsys1.operation1())
        result.append(self._subsys2.operation1())
        result.append('Фасад запрос подсистемы на выполнения действия:')
        result.append(self._subsys1.operation_n())
        result.append(self._subsys2.operation_z())
        return '\n'.join(result)


class Subsystem1:
    def operation1(self):
        return 'Подсистема1: Готов!'

    def operation_n(self):
        return 'Подсистема1: Начнем!'


class Subsystem2:
    def operation1(self):
        return 'Подсистема2: Приготовься!'

    def operation_z(self):
        return 'Подсистема2: Огонь!'


def client_code(facade: Facade):
    print(facade.operation(), end='')


if __name__ == '__main__':
    subsys1 = Subsystem1()
    subsys2 = Subsystem2()
    facade = Facade(subsys1, subsys2)
    client_code(facade)