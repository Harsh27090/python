class Car:
    # constructor
    # types:
    # default - (self)
    # parameterized
    # with default values
    def __init__(self,brand='Toyota', color='White'):
        self.color = color
        self.brand = brand

    #
    # def set_details(self, brand, color):
    #     self.brand = brand
    #     self.color = color

    # method
    def show_details(self):
        print(f'Brand: {self.brand}, Color: {self.color}')

car1 = Car('BMW', 'Blue')
# car1.set_details()

car2 = Car('Ferrari', 'Red')
# car2.set_details()

car = Car()

car1.show_details()
car2.show_details()
car.show_details()
