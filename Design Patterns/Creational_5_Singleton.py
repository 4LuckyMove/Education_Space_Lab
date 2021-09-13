class SingletonCar(object):
    __brand = None

    def __new__(cls, *args, **kwargs):
        if not SingletonCar.__brand:
            SingletonCar.__brand = object.__new__(cls)
        return SingletonCar.__brand

    def __init__(self, brand_car, model_car):
        self.brand_car = brand_car
        self.model_car = model_car


def client_code():
    car1 = SingletonCar('Nissan', 'Maxima')
    car2 = SingletonCar('Audi', 'Q7')

    print(f'car1: {car1}')
    print(f'car2: {car2}')
    print('-' * 58)
    print(f'Равны car1 и car2: {car1 == car2}')
    print('-' * 58)
    print(f'car1.brand_car: {car1.brand_car}')
    print(f'car2.brand_car: {car2.brand_car}')

client_code()