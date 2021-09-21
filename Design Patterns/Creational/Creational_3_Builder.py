from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    @property
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def produce_part_a(self):
        pass

    @abstractmethod
    def produce_part_b(self):
        pass

    @abstractmethod
    def produce_part_c(self):
        pass


class SpecialBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = SpecialProduct()

    @property
    def product(self):
        product = self._product
        self.reset()
        return product

    def produce_part_a(self):
        self._product.add('А')

    def produce_part_b(self):
        self._product.add('B')

    def produce_part_c(self):
        self._product.add('C')


class SpecialProduct:
    def __init__(self):
        self.parts = []

    def add(self, part: Any):
        self.parts.append(part)

    def list_parts(self):
        print(f'Часть продукта: {", ".join(self.parts)}', end='')


class Director:
    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder):
        self._builder = builder

    def build_basic_product(self):
        self.builder.produce_part_a()

    def build_full_product(self):
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == '__main__':
    director = Director()
    builder = SpecialBuilder()
    director.builder = builder

    print('Базовый продукт:')
    director.build_basic_product()
    builder.product.list_parts()
    print('\n')
    print('Полноценный продукт:')
    director.build_full_product()
    builder.product.list_parts()
    print('\n')
    print('Индивидуальный продукт:')
    builder.produce_part_b()
    builder.produce_part_c()
    builder.product.list_parts()