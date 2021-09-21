class Target:
    def request(self):
        return 'Цель: поведение цели по умолчанию.\n'


class Adaptee:
    def specific_request(self):
        return 'илец еинедевоп еоньлаицепС'


class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def request(self):
        return f'Адаптер: (конвертация) {self.adaptee.specific_request()[::-1]}'


def client_code(target: Target):
    print(target.request(), end='')


if __name__ == '__main__':
    print('Клиент: Я могу нормально работать с целевыми объектами:')
    target = Target()
    client_code(target)
    print('-' * 50)
    adaptee = Adaptee()
    print("Клиент: у класса Adaptee странный интерфейс. "
          "Видишь, я этого не понимаю:")
    print(f'Adaptee: {adaptee.specific_request()}', end='\n')
    print('-' * 50)
    print('Клиент: Но я могу работать с ним через Адаптер:')
    adapter = Adapter(adaptee)
    client_code(adapter)