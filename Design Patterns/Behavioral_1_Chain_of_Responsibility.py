from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    @abstractmethod
    def set_next_handler(self, handler):
        pass

    @abstractmethod
    def turn_handler(self, request) -> Optional[str]:
        pass


class BaseHandler(Handler):
    _next_handler: Handler = None

    def set_next_handler(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def turn_handler(self, request: Any):
        if self._next_handler:
            return self._next_handler.turn_handler(request)
        return None


class DoveHandler(BaseHandler):
    def turn_handler(self, request: Any):
        if request == 'зелень':
            return f'Голубь питается {request}ю'
        else:
            return super().turn_handler(request)


class KoalaHandler(BaseHandler):
    def turn_handler(self, request: Any):
        if request == 'эвкалипт':
            return f'Коала питается {request}ом'
        else:
            return super().turn_handler(request)


class CatHandler(BaseHandler):
    def turn_handler(self, request: Any):
        if request == 'мышь':
            return f'Кошка питается {request}ю'
        else:
            return super().turn_handler(request)


def client_code(handler: Handler) -> None:
    for food in ['эвкалипт', 'мышь', 'пицца']:
        print(f'Кто питается {food}?')
        result = handler.turn_handler(food)
        if result:
            print(f'{result}\n')
        else:
            print(f'{food} - никто не кушает.\n')


if __name__ == '__main__':
    dove = DoveHandler()
    koala = KoalaHandler()
    cat = CatHandler()

    dove.set_next_handler(koala).set_next_handler(cat)

    print('Цепочка: Голубь -> Коала -> Кошка\n')
    client_code(dove)

    print('Подцепочка: Коала -> Кошка\n')
    client_code(koala)