import abc


class Figure(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calculate_area(self):
        pass

    @abc.abstractmethod
    def calculate_perimeter(self):
        pass


class Rectangle(Figure):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)


class Square(Figure):
    def __init__(self, width):
        self.width = width

    def calculate_area(self):
        return self.width ** 2

    def calculate_perimeter(self):
        return 4 * self.width


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


class Factory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_figure(self, name):
        pass


class FigureFactory(Factory):
    def create_figure(self, name):
        if name == "круг":
            radius = input("Введите радиус круга: ")
            return Circle(float(radius))
        elif name == "прямоугольник":
            height = input("Введите высоту прямоугольника: ")
            width = input("Введите ширину прямоугольника: ")
            return Rectangle(int(height), int(width))
        elif name == "квадрат":
            width = input("Введите длину квадрата: ")
            return Square(int(width))


def figures_client():
    figure_factory = FigureFactory()
    figure_name = input("Введите имя фигуры: ")

    figure = figure_factory.create_figure(figure_name)

    print(f"Площадь {figure_name}: {figure.calculate_area()}")
    print(f"Периметр {figure_name}: {figure.calculate_perimeter()}")


figures_client()