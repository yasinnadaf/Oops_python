# constructor is a special method which is used to initialize object.
# it is called automatically when we create object of class.its definition executed whn we create the obj of class.

# Parameterized constructor
class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        print('Parameterized constructor')

    def show_details(self):
        print(f'student name is {self.name} id is {self.id}')


if __name__ == '__main__':
    std1 = Student('abhi', 4)
    std2 = Student('zain', 2)

    std1.show_details()
    print()
    std2.show_details()



# --> # Non_parameterized constructor
# it is uses when we do not want to manipulate the value or the constructor that has only self as an argument.

# class Employee:
#     def __init__(self):
#         print('This is non-parameterize constructor')
#
#     def show(self, company):
#         print('company name is', company)
#
#
# if __name__ == '__main__':
#     obj = Employee()
#     obj.show('tata')
#     print()
