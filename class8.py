# inheritance
class Person:
    def __init__(self, i, n, f):
        self.id = i
        self.name = n
        self.family = f

    def show(self):
        print(self.id, self.name, self.family)

class Student(Person):
    def __init__(self, i, n, f, g):
        Person.__init__(self, i, n, f)
        self.g = g

s = Student(1, 'a', 'b', 19)
s.show()
"""
show method of child or show method of parent !!
"""
class Person:
    def __init__(self, i, n, f):
        self.id = i
        self.name = n
        self.family = f

    def show(self):
        print(self.id, self.name, self.family)

class Student(Person):
    def __init__(self, i, n, f, g):
        super().__init__(i, n, f)
        self.g = g

    def show(self):
        #print(self.id, self.name, self.family, self.g)
        person.show(self)
        print(self.g)

s = Student(1, 'a', 'b', 19)
s.show()