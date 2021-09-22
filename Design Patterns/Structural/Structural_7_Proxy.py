from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def request(self):
        pass


class RealSubject(Subject):
    def request(self):
        print('Реальный субъект: Обработка запроса.')


class Proxy(Subject):
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self):
        print('Заместитель: Проверка доступа перед запуском корректного запроса.')
        return True

    def log_access(self):
        print('Заместитель: Регистрация времени запроса.', end='')


def client_code(subject: Subject):
    subject.request()


if __name__ == '__main__':
    print('Клиент: Выполнение клиентского кода с реальным субъектом:')
    real_sub = RealSubject()
    client_code(real_sub)
    print('\n')

    print('Клиент: Выполнение клиентского кода с заместителем:')
    proxy = Proxy(real_sub)
    client_code(proxy)