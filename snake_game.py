import os
import time
import random
import keyboard
from threading import Thread


if os.getenv("OS") in ["Windows_NT", "Linux"]:
    import msvcrt as m


class BcolorMenu:

    OKBLUE = '\033[94m'
    WARNING = '\033[93m'


def start_function():
    # print('Start works')
    os.system('cls' if os.name == 'nt' else 'clear')
    Game().board()
    Thread(target=Game().move).start()
    Thread(target=Game().btn_move).start()


def save_function():
    print('Save works')


def option_function():
    print('Option works')


class Menu:

    def __init__(self):
        self.exit = 0
        self.menu = []
        self.functions = []
        self.controller = []

    def add_menu(self, menu, function):
        self.menu.append(menu)
        self.functions.append(function)
        if len(self.controller) == 0:
            self.controller.append(1)
        else:
            self.controller.append(0)

    def start_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for menu_item in range(len(self.menu)):
            if self.controller[menu_item] == 1:
                print(BcolorMenu.WARNING + self.menu[menu_item])
            else:
                print(BcolorMenu.OKBLUE + self.menu[menu_item])
        # main_menu.start_menu()
        self.add_menu('Новая игра', start_function)
        self.add_menu('Save', save_function)
        self.add_menu('Option', option_function)
        self.add_menu('Exit', 'exit')

    def handle_menu(self, event):
        os.system('cls' if os.name == 'nt' else 'clear')
        if event.name == 'down':
            if self.controller.index(1) != (len(self.controller) - 1):
                self.controller.insert(0, 0)
                self.controller.pop()
        elif event.name == 'up':
            if self.controller.index(1) != 0:
                self.controller.append(0)
                self.controller.pop(0)
        for menu_item in range(len(self.menu)):
            if self.controller[menu_item] == 1:
                print(BcolorMenu.WARNING + self.menu[menu_item])
            else:
                print(BcolorMenu.OKBLUE + self.menu[menu_item])
        if event.name == 'enter':
            if self.functions[self.controller.index(1)] == 'exit':
                self.exit = 1
                return
            self.functions[self.controller.index(1)]()


last2X = 0
last2Y = 0
lastX = 0
lastY = 0
elemX = [0 for i in range(100)]
elemY = [0 for i in range(100)]


class Game:

    x = 5
    y = 3
    game_thread = True
    fruit_cord_x = 5
    fruit_cord_y = 6
    button_default = "d"
    score = 0
    icon_player = "►"
    tail = "*"

    def board(self, width: int = 40, height: int = 20, pos_player_x: int = x, pos_player_y: int = y):
        global elemX, elemY, last2X, last2Y, lastX, lastY
        os.system('cls' if os.name == 'nt' else 'clear')
        for h in range(height):
            for w in range(width):
                if pos_player_x == Game.fruit_cord_x and pos_player_y == Game.fruit_cord_y:
                    Game.fruit_cord_x = random.randint(2, width-1)
                    Game.fruit_cord_y = random.randint(2, height-1)
                    Game.score += 1

                for el in range(Game.score):
                    if pos_player_x == elemX[el] and pos_player_y == elemY[el]:
                        print(f'\nGAME OVER\nScore: {Game.score}')
                        Game.game_thread = False
                        exit()

                if not (Game.x in range(width-39)) and not (Game.y in range(height-1)) or \
                    not (Game.x in range(width-1)) and not (Game.y in range(height-19)):
                    print(f'\nGAME OVER\nScore: {Game.score}')
                    Game.game_thread = False
                    exit()

                if w == 0:
                    print('#', end='')
                elif h == 0:
                    print('#', end='')
                elif h == height-1:
                    print('#', end='')
                elif w == width-1:
                    print('#', end='')
                elif pos_player_x == w and pos_player_y == h:
                    print(Game.icon_player, end='')
                elif Game.fruit_cord_x == w and Game.fruit_cord_y == h:
                    print("A", end='')
                else:
                    pr = True
                    for ls in range(Game.score):
                        if elemX[ls] == w and elemY[ls] == h:
                            print(Game.tail, end="")
                            pr = False
                    if pr:
                        print(' ', end='')
            print()

        # print(f"X player: {pos_player_x} || Y player: {pos_player_y}")
        print(f"\nScore: {Game.score}\n\nWASD / Стрелочки - перемещение\nESC - выйти")
        lastX = pos_player_x
        lastY = pos_player_y
        if Game.score > 0:
            for el in range(Game.score):
                last2X = elemX[el]
                last2Y = elemY[el]
                elemX[el] = lastX
                elemY[el] = lastY
                lastX = last2X
                lastY = last2Y

    def btn_move(self):
        while Game.game_thread:
            Game.button_default = m.getch()[0]

    def move(self):
        while Game.game_thread:
            if Game.button_default in ["", " "]:
                Game.button_default = "d"
            elif Game.button_default in ["w", 119, 230, 72]:
                Game.y -= 1
                Game.icon_player = "▲"
            elif Game.button_default in ["a", 97, 228, 75]:
                Game.x -= 1
                Game.icon_player = "◄"
            elif Game.button_default in ["s", 115, 235, 80]:
                Game.y += 1
                Game.icon_player = "▼"
            elif Game.button_default in ["d", 100, 162, 77]:
                Game.x += 1
                Game.icon_player = "►"

            elif Game.button_default in ["exit", 27]:
                Game.game_thread = False
                exit()

            Game().board(pos_player_x=Game.x, pos_player_y=Game.y)

            time.sleep(0.2)


main_menu = Menu()
main_menu.start_menu()
keyboard.on_press(main_menu.handle_menu)
while main_menu.exit != 1:
    pass



# Menu().add_menu('Start', start_function)
# self.add_menu('Save', save_function)
# self.add_menu('Option', option_function)
# self.add_menu('Exit', 'exit')
# main_menu.start_menu()
# keyboard.on_press(self.handle_menu)
# while self.exit != 1:
#     pass


