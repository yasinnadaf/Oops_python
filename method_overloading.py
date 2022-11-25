# Method overloading
class Multiply():
    def product(self, x, y):
        p = x * y
        print(p)

    def product(self, x, y, z):
        p = x * y * z
        print(p)


if __name__ == '__main__':
    m = Multiply()
    m.product(2, 5, 7)

