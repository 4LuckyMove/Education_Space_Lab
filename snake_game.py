import random

class BodySnake:

    def __init__(self):
        self.body_snake = '*'

    def add_body_snake(self):
        return self.body_snake

class Snake:

    DEFAULT_MOVE_DIR = 'd'

    def __init__(self, x=10, y=10):
        self.head = '*'
        self.body, self.body_x, self.body_y = [], [], []
        self.x = x
        self.y = y
        self.dir = None
        self.speed = 1
        self.board = Board(width=40, height=20)
        self.body_snake = BodySnake()

    def move(self, apple):
        self.dir = input('Выберете направлении змейки: ')

        # движение ВЛЕВО
        if self.dir in 'aA4фФ':
            self.x -= self.speed
        # движение ВПРАВО
        elif self.dir in 'dD6вВ':
            self.x += self.speed
        # движение ВВЕРХ
        elif self.dir in 'wW8цЦ':
            self.y -= self.speed
        # движение ВНИЗ
        elif self.dir in 'sS2ыЫ':
            self.y += self.speed
        else:
            print('')

        if self.x == apple.x and self.y == apple.y:
            apple.x = random.randint(2, self.board.width - 1)
            apple.y = random.randint(2, self.board.height - 1)
            self.body.append(self.body_snake.add_body_snake())
        print(f'Съедино яблок: {len(self.body)}')

    def add_body_snake(self):
        return (len(self.body) + 1)


class Apple:

    def __init__(self):
        self.board = Board(width=40, height=20)
        self.x = random.randint(2, self.board.width - 1)
        self.y = random.randint(2, self.board.height - 1)
        self.apple = 'A'

    def print_apple(self):
        print(self.apple, end='')


class Board:

    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height

    def print_board(self, snake, apple):
        for h in range(self.height):
            for w in range(self.width):
                if snake.x == w and snake.y == h:
                    print(snake.head * snake.add_body_snake(), end='')
                elif apple.x == w and apple.y == h:
                    apple.print_apple()

                if w == 0 or h == 0:
                    print('#', end='')
                elif h == self.height-1 or w == self.width-1:
                    print('#', end='')
                else:
                    for s in range(len(snake.body)):
                        snake.body_x.append(snake.x - 1)
                        snake.body_y.append(snake.y - 1)
                        if snake.body_x[s] == w - 1 and snake.x == apple.x and snake.body_y[s] == h - 1 \
                                and snake.y == apple.y:
                            # snake.body.insert(-1, (snake.x, snake.y))
                            print(snake.head + snake.body[s], end='')
                    print(' ', end='')
            print()

class Game:

    def start_game(self):
        board = Board(width=40, height=20)
        snake = Snake(10, 10)
        apple = Apple()

        print('Snake Game')
        print('Управление: WASD / 2468 / ЦФЫВ')
        # print('Выход из игры: E или 5')

        while not ((snake.x > board.width-1 or snake.x < 1) or (snake.y > board.height - 1 or snake.y < 1)):
            board.print_board(snake, apple)
            snake.move(apple)
        else:
            print('Game Over')


game1 = Game()
game1.start_game()