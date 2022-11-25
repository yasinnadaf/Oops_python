# Method overriding
class Parent1():
    def show(self):
        print("Parent1")


class Parent2():
    def display(self):
        print("Parent2")


class Child(Parent1, Parent2):
    def show(self):
        print("Child")


if __name__ == '__main__':
    obj = Child()

    obj.show()
    obj.display()