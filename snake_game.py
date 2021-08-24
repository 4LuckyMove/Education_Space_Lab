import os
import time
import random
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
    tail = "o"


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

        print(f"X player: {pos_player_x} || Y player: {pos_player_y}")
        print(f"Score: {Game.score}\n\nWASD / Стрелочки - перемещение\nESC - выйти")
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
                print("Вы покинули игру")
                Game.game_thread = False
                exit()

            Game().board(pos_player_x=Game.x, pos_player_y=Game.y)

            time.sleep(0.2)


class GameFunction:

    def console_clear(self):
        for i in ["cls", "clear"]:
            os.system(i)
            break

    def main(self):
        Game().board()
        Thread(target=Game().move).start()
        Thread(target=Game().btn_move).start()

    def menu(self):
        pass


if __name__ == '__main__':
    GameFunction().console_clear()
    GameFunction().main()