# Addition and subtraction of imaginary numbers

class Imaginary:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __str__(self):
        return str(self.r)+'+'+str(self.i)+"i"

    def __add__(self, other):
        nr = self.r+other.r
        ni = self.i+other.i
        i = Imaginary(nr, ni)
        return i

    def __sub__(self, other):
        nr = self.r - other.r
        ni = self.i - other.i
        i = Imaginary(nr, ni)
        return i

c1 = Imaginary(2, 3)
print(c1)

c2 = Imaginary(3, 4)
print(c2)

c3 = c2 - c1
print("result of subtraction is:", c3)
c3 = c2 + c1
print("result of addition is:", c3)