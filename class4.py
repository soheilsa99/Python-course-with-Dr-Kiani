import math
class fraction:
    def __init__(self, s, m):
        self.s = s
        self.m = m

    def __str__(self):
        return '\n '+str(self.s)+'\n---\n '+str(self.m)

    def simplify(self):
        g = math.gcd(self.s,self.m)
        self.s = self.s//g
        self.m = self.m//g

    def __add__(self, other):
        ns = self.s*other.m+self.m*other.s
        nm = self.m*other.m
        f = fraction(ns, nm)
        f.simplify()
        return f

    def __sub__(self, other):
        ns = self.s*other.m-self.m*other.s
        nm = self.m*other.m
        f = fraction(ns, nm)
        f.simplify()
        return f

    def __mul__(self, other):
        ns = self.s * other.s
        nm = self.m * other.m
        f = fraction(ns, nm)
        f.simplify()
        return f


    def __eq__(self, other):
        self.simplify()
        other.simplify()
        return self.s == other.s and self.m == other.m



f1 = fraction(3, 5)
f2 = fraction(2, 6)

print(f1)
print(f2)

print(f1 == f2)

n1 = fraction(6, 9)
n2 = fraction(4, 6)
print(n1)
print(n2)

print(n1 == n2)
n3 = n1 + n2
print(n3)

f4 = f1-f2*f1+f2
print(f4)

print("----------------------------------------------------------------")
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

    def show(self):
        print(self.id, self.name, self.family, self.grades)

s = Student('mm', 'sds', 10)
print(s.name)
print(s.family)

s.name = 'x'
s.show()
"""
we can change attribute out of class !!
also we have a solution :) private attribute with this format .__
also we can add a new attribute and write it out of class
"""
class Student:
    def __init__(self, name, family, id):
        self.__name = name
        self.__family = family
        self.id = id
        self.grades = []

    def add_grade(self, g):
        self.grades.append(g)

    def average(self):
        return sum(self.grades)/len(self.grades)

    def show(self):
        print(self.id, self.__name, self.__family, self.grades)


s = Student('mm', 'sds', 10)
# s.show()
# print(s.name)
# print(s.family)
# we can't change name and family directly...

s.address = ' dlfjslf '
print(s.address)

s.show()