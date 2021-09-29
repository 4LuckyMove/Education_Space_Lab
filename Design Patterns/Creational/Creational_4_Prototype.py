from abc import ABC, abstractmethod
import time
import copy
import datetime


class Prototype(ABC):
    def __init__(self):
        time.sleep(3)
        self.vitality = None
        self.level = None
        self.defense = None
        self.attack = None

    @abstractmethod
    def clone(self):
        pass


class Archer(Prototype):
    def __init__(self, level, vitality, defense, attack):
        super().__init__()
        self.level = level
        self.vitality = vitality
        self.defense = defense
        self.attack = attack
        self._range_attack = 500

    def clone(self):
        return copy.deepcopy(self)


class Warrior(Prototype):
    def __init__(self, level, vitality, defense, attack):
        super().__init__()
        self.level = level
        self.vitality = vitality
        self.defense = defense
        self.attack = attack
        self._stamina = 100

    def clone(self):
        return copy.deepcopy(self)


class Mage(Prototype):
    def __init__(self, level, vitality, defense, attack):
        super().__init__()
        self.level = level
        self.vitality = vitality
        self.defense = defense
        self.attack = attack
        self._mana = 100

    def clone(self):
        return copy.deepcopy(self)


def client_code():
    create_npc = input('Какое кол-во создать NPC: ')
    archer = Archer(3, 550, 3, 74)
    warrior = Warrior(5, 1233, 10, 51)
    mage = Mage(10, 500, 2, 43)
    npc_clone = []

    print(f'Создание {create_npc} NPC: {datetime.datetime.now().time()}')
    for npc in range(int(create_npc)):
        archer_clone = archer.clone()
        warrior_clone = warrior.clone()
        mage_clone = mage.clone()
        npc_clone.extend([archer_clone, warrior_clone, mage_clone])
        print(f'Завершено создание клонов из Лучника, Воина и Мага {npc+1}: {datetime.datetime.now().time()}')
    print(f'Успешно завершено создание NPC в кол-ве {create_npc}: {datetime.datetime.now().time()}')


client_code()
