# access to change private attribute
class Student:
    def __init__(self, id, name, family):
        self.id = id
        self.__name = name
        self.family = family
        self.__grades = []

    def change_name(self, n):
        x = input("please Enter password: ")
        if x == '123':
            self.__name = n

    def add_grade(self, n):
        x = input("please Enter password: ")
        if x == '123':
            self.__grades.append(n)

    def average(self):
        return sum(self.__grades)/len(self.__grades)

    def show(self):
        print(self.id, self.__name, self.family, self.__grades)


s = Student(10, 'mm', 'sds')
s.change_name('t')
s.show()