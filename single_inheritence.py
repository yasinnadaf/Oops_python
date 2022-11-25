# one class inherits another class called single inheritance

class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def show(self):
        print(f'brand is  {self.brand} and color is {self.color}')


class Car(Vehicle):
    def car(self):
        print('child class')


if __name__ == '__main__':
    obj = Car('Mini cooper', 'red')
    obj.show()