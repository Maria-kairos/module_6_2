class Vehicle:
    __COLOR_VARIANTS = ['yellow', 'green', 'red', 'black']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        print('Модель:', self.__model)

    def get_horsepower(self):
        print('Мощность двигателя:', self.__engine_power)

    def get_color(self):
        print('Цвет:', self.__color)

    def print_info(self):
        print(self.get_model(), self.get_horsepower(), self.get_color(), 'Владелец:', self.owner)

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print('Нельзя сменить цвет на', new_color)

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'red', 500)
vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('Black')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()
