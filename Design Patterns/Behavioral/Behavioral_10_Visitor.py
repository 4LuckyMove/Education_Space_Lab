from abc import ABC, abstractmethod
from typing import List


class Spy(ABC):
    @abstractmethod
    def visit_military_base(self, military_base):
        pass

    @abstractmethod
    def visit_headquarters(self, headquarters):
        pass


class MilitaryFacility(ABC):
    @abstractmethod
    def accept(self, spy: Spy):
        pass


class MilitaryBase(MilitaryFacility):
    def __init__(self):
        self._secret_drafting = 1
        self._nuclear_submarines = 1

    def __repr__(self):
        return f'На военной базе находиться {self._nuclear_submarines} атомных подводных лодок и ' \
               f'{self._secret_drafting} секретных чертежей'

    def accept(self, spy: Spy):
        spy.visit_military_base(self)

    def remove_secret_drafting(self):
        if self._secret_drafting:
            self._secret_drafting -= 1

    def remove_nuclear_submarines(self):
        if self._nuclear_submarines:
            self._nuclear_submarines -= 1

    @property
    def is_combat_ready(self):
        return self._nuclear_submarines > 0


class CentralHq(MilitaryFacility):
    def __init__(self):
        self._generals = 3
        self._secret_documents = 2

    def __repr__(self):
        return f'В штабе находится {self._generals} генералов и ' \
               f'{self._secret_documents} секретных документов'

    def accept(self, spy: Spy):
        spy.visit_headquarters(self)

    def remove_generals(self):
        if self._generals:
            self._generals -= 1

    def remove_secret_doc(self):
        if self._secret_documents:
            self._secret_documents -= 1

    @property
    def is_command_ready(self):
        return self._generals > 0


class ScoutSpy(Spy):
    def __init__(self):
        self._collected_info = {}

    def visit_military_base(self, military_base: MilitaryBase):
        self._collected_info['base'] = f'Военная база:\n\t{str(military_base)}\n\tБоеготовность: ' \
                                       f'{"Да" if military_base.is_combat_ready else "Нет"}\n'

    def visit_headquarters(self, headquarters: CentralHq):
        self._collected_info['headquarters'] = f'Центральный штаб:\n\t{str(headquarters)}\n\tКомандование: ' \
                                               f'{"Функционирует" if headquarters.is_command_ready else "Не функционирует"}'

    def report(self):
        return f'Информация от разведчика:\n{"".join(self._collected_info.values())}\n'


class ProSpy(Spy):
    def visit_military_base(self, military_base: MilitaryBase):
        military_base.remove_secret_drafting()
        military_base.remove_nuclear_submarines()

    def visit_headquarters(self, headquarters: CentralHq):
        headquarters.remove_generals()
        headquarters.remove_generals()
        headquarters.remove_secret_doc()
        headquarters.remove_generals()
        headquarters.remove_secret_doc()


if __name__ == '__main__':
    base = MilitaryBase()
    hq = CentralHq()
    facilities = [base, hq]
    scout = ScoutSpy()
    print('Отправляем разведчика...\n')
    for f in facilities:
        f.accept(scout)
    print(scout.report())
    print('Отправляем проффесионального шпиона на задание...\n')
    spy = ProSpy()
    for f in facilities:
        f.accept(spy)
    print('Отправляем разведчика обновить данные...\n')
    for f in facilities:
        f.accept(scout)
    print(scout.report())
