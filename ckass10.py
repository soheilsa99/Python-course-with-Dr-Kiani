# Multiple inheritance
class rect:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def show(self):
        print(self.w, self.h)


class color:
    def __init__(self, c):
        self.c = c

    def show(self):
        print(self.c)


class shape(rect, color):
    def __init__(self, w, h, c):
        rect.__init__(self, w, h)
        color.__init__(self, c)
        self.a = self.w*self.h

    def show(self):
        rect.show(self)
        color.show(self)
        print(self.a)


s = shape(3, 4, 'red')
s.show()
