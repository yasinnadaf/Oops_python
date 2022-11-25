# child class inherits two or more parent class

class Calculation1:
    def summation(self , a, b):
        return a+b


class Calculation2:
    def multiplication(self, a, b):
        return a*b


class Derived(Calculation1, Calculation2):
    def divide(self, a, b):
        return a/b


if __name__ == '__main__':
    d = Derived()
    print(d.summation(10, 20))
    print(d.multiplication(10, 20))
    print(d.divide(10, 20))



