import os
import time
import random
import keyboard
from threading import Thread


if os.getenv("OS") in ["Windows_NT", "Linux"]:
    import msvcrt as m


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
        GameFunction().console_clear()
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
                        # Menu().call_menu()

                if not (Game.x in range(width-39)) and not (Game.y in range(height-1)) or \
                    not (Game.x in range(width-1)) and not (Game.y in range(height-19)):
                    print(f'\nGAME OVER\nScore: {Game.score}')
                    Game.game_thread = False
                    exit()
                    # Menu().call_menu()

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
                # Menu().call_menu()

            Game().board(pos_player_x=Game.x, pos_player_y=Game.y)

            time.sleep(0.2)


class Menu:

    selected = 0
    main_menu = ["Продолжить игру", "Новая игра", "Рекорд", "Инструкция", "Выход"]

    def show_menu(self):
        GameFunction().console_clear()
        print('\n\tГлавное меню:')
        for i in range(len(Menu.main_menu)):
            print(f'{"►" if Menu.selected == i else " "} {i+1}. {Menu.main_menu[i]}')

    def up_menu(self):
        if Menu.selected == 0:
            return
        Menu.selected -= 1
        Menu().show_menu()

    def down_menu(self):
        if Menu.selected == len(Menu.main_menu):
            return
        Menu.selected += 1
        Menu().show_menu()

    def instruction(self):
        print('Управление:\nWASD / Стрелочки - перемещение\nESC - выйти')

    def call_menu(self):
        Menu().show_menu()
        keyboard.add_hotkey('up', Menu().up_menu)
        keyboard.add_hotkey('down', Menu().down_menu)
        # if Menu().show_menu()[0] == 'Продолжить игру':
        #     pass
        # elif Menu().show_menu()[1] == 'Новая игра':
        #     GameFunction().console_clear()
        #     GameFunction().main()
        # elif Menu().show_menu()[2] == 'Рекорд':
        #     pass
        # elif Menu().show_menu()[3] == 'Инструкция':
        #     Menu().instruction()
        # elif Menu().show_menu()[4] == 'Выход':
        #     print("Вы покинули игру")
        #     exit()

        keyboard.wait('enter')


class GameFunction:

    def console_clear(self):
        for i in ["cls", "clear"]:
            os.system(i)
            break

    def main(self):
        Game().board()
        Thread(target=Game().move).start()
        Thread(target=Game().btn_move).start()


if __name__ == '__main__':
    GameFunction().console_clear()
    # Menu().call_menu()
    GameFunction().main()