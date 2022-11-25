# one class inherits multiple class

class Animal:
    def speaking(self):
        print('Animal speaking')


class Dog(Animal):
    def barking(self):
        print('Dog barking')


class BabyDog(Dog):
    def eat(self):
        print('Eat bread')


if __name__ == '__main__':
    obj = BabyDog()
    obj.speaking()
    obj.barking()
    obj.eat()


