from __future__ import annotations
from abc import ABC, abstractmethod


class FurnitureFactory(ABC):
    @abstractmethod
    def create_style_table(self) -> Table:
        pass

    @abstractmethod
    def create_style_sofa(self) -> Sofa:
        pass


class ClassicalFurnitureFactory(FurnitureFactory):
    def create_style_table(self) -> Table:
        return ClassicalTable()

    def create_style_sofa(self) -> Sofa:
        return ClassicalSofa()


class ModernFurnitureFactory(FurnitureFactory):
    def create_style_table(self) -> Table:
        return ModernTable()

    def create_style_sofa(self) -> Sofa:
        return ModernSofa()


class Table(ABC):
    @abstractmethod
    def create_table(self):
        pass


class ClassicalTable(Table):
    def create_table(self):
        return 'Стол в стиле Классика'


class ModernTable(Table):
    def create_table(self):
        return 'Стол в стиле Модерн'


class Sofa(ABC):
    @abstractmethod
    def create_sofa(self):
        pass

    @abstractmethod
    def style_sofa_and_table(self, collaborator: Table):
        pass


class ClassicalSofa(Sofa):
    def create_sofa(self):
        return 'Диван в стиле Классика'

    def style_sofa_and_table(self, collaborator: Table):
        result = collaborator.create_table()
        return f'Диван в стиле Классика и {result}'


class ModernSofa(Sofa):
    def create_sofa(self):
        return 'Диван в стиле Модерн'

    def style_sofa_and_table(self, collaborator: Table):
        result = collaborator.create_table()
        return f'Диван в стиле Модерн и {result}'


def client_code(factory: FurnitureFactory):
    table = factory.create_style_table()
    sofa = factory.create_style_sofa()

    print(f'{table.create_table()}')
    print(f'{sofa.create_sofa()}')
    print(f'{sofa.style_sofa_and_table(table)}')


if __name__ == '__main__':
    print('Мебель в стиле Классика:')
    client_code(ClassicalFurnitureFactory())
    print('')
    print('Мебель в стиле Модерн:')
    client_code(ModernFurnitureFactory())