from abc import ABC, abstractmethod


class Realization(ABC):
    @abstractmethod
    def name_realization(self):
        pass

    @abstractmethod
    def operation_realization(self):
        pass


class PlatformA(Realization):
    def name_realization(self):
        return 'Платформа А'

    def operation_realization(self):
        return 'Платформа А: Результат на платформе А.'


class PlatformB(Realization):
    def name_realization(self):
        return 'Платформа Б'

    def operation_realization(self):
        return 'Платформа Б: Результат на платформе Б.'


class Manage:
    def __init__(self, realization: Realization):
        self.realization = realization

    def operation(self):
        return f'Управление: Базовая операция с {self.realization.name_realization()}\n' \
               f'{self.realization.operation_realization()}'


class ExtendedManage(Manage):
    def operation(self):
        return f'Расширенная Управление: Расширенная операция с {self.realization.name_realization()}\n' \
               f'{self.realization.operation_realization()}'


def client_code(abstraction: Manage):
    print(abstraction.operation())


if __name__ == '__main__':
    implementation = PlatformA()
    abstraction = Manage(implementation)
    client_code(abstraction)
    print('-' * 60)
    implementation = PlatformB()
    abstraction = ExtendedManage(implementation)
    client_code(abstraction)