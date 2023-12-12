class Student:
    def __init__(self, i, n, f):
        self.id = i
        self.name = n
        self.family = f
        self.grades = []

    def show(self):
        print(self.id, self.name, self.family, self.grades)

    def add_grade(self, g):
        self.grades.append(g)


class Teacher:
    def __init__(self, i, n, f):
        self.id = i
        self.name = n
        self.family = f

    def show(self):
        print(self.id, self.name, self.family)

    def set_grade(self, s):
        s.show()
        n = float(input('Enter grade: '))
        s.addgrade(n)


#agreegation
s = Student(1, 'a', 'b')
t = Teacher(100, 'm', 'k')

t.set_grade(s)
s.show()