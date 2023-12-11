class Student:
    def __init__(self, name, family, id):
        self.n = name
        self.f = family
        self.i = id

    def show(self):
        print(self.n, self.f, self.i )

s1 = student("Mohamed", "Kiani", 20)
s1.show()

s2 = student("Soheil", "Sarrami", 10)
s2.show()


# examole one shop----------------------------------------------
class Product:
    def __init__(self,code,name,price):
        self.c = code
        self.n = name
        self.p = price

    def show(self):
        print(self.c, self.n, self.p)

    def changeprice(self, percent):
        self.p += self.p*percent/100

p1 = product(10, "chips", 30000)
p1.changeprice(20)

p2 = product(10, "yogurt", 60000)
p2.changeprice(-15)

p1.show()
p2.show()

#rectangle class
class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        print(self.width * self.height)

    def perimeter(self):
        print(2 * (self.width + self.height))

    def show(self):
        print(self.width, self.height)


r1 = Rectangle(4, 8)
r1.show()
r1.area()
r1.perimeter()

# student class new version
class Student:
    def __init__(self, name, family, id):
        self.n = name
        self.f = family
        self.i = id
        self.grades = []

    def addgrade(self, g):
        self.grades.append(g)

    def average(self):
        print(sum(self.grades)/len(self.grades))

    def show(self):
        print(self.n, self.f, self.i )

s1 = Student("Mohamed", "Kiani", 20)
s1.addgrade(12)
s1.addgrade(17)
s1.addgrade(20)
s1.addgrade(10)
s1.show()

s2 = Student("Soheil", "Sarrami", 10)
s2.addgrade(11)
s2.addgrade(15)
s2.addgrade(20)
s2.addgrade(10)
s2.addgrade(14)
s2.show()