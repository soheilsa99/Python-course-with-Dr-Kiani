"""
overriding a method
in this example, we use a method instead show method
"""

class Student:
    def __init__(self, name, family, id):
        self.name = name
        self.family = family
        self.id = id
        self.grades = []

    def add_grade(self, g):
        self.grades.append(g)

    def average(self):
        return sum(self.grades)/len(self.grades)

    # def show(self):
    #     print(self.id, self.name, self.family, self.grades)

    def __str__(self):
        return self.id+','+self.name+','+self.family

S = Student('a', 'b', '1rd')
print(S)


"""
eq method for compare two things
for exampl we compare two sides of two rectangles
"""
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def __str__(self):
        return str(self.w)+' , '+str(self.h)

    def __eq__(self, other):
        if self.w == other.w and self.h == other.h:
            return True
        else:
            return False




r1 = Rectangle(4, 8)
r2 = Rectangle(4, 6)
print(r1 == r2)
"""
if we want to compare < and > with eq method we will see an error
we should use  'lt' and 'gt' method......xxxx
"""
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def __str__(self):
        return str(self.w)+' , '+str(self.h)
    def area(self):
        return self.w * self.h


    def __lt__(self, other):
        if self.area() < other.area():
            return True
        else:
            return False

r1 = Rectangle(4, 8)
r2 = Rectangle(4, 6)
(print(r1 > r2))

# add two sides of two rectangles together
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def __str__(self):
        return str(self.w)+' , '+str(self.h)

    def __add__(self, other):
        nw = self.w+other.w
        nh = self.h+other.h
        r = Rectangle(nw, nh)
        return r

r1 = Rectangle(4, 8)
r2 = Rectangle(4, 6)
r3 = r1+r2
print(r3)