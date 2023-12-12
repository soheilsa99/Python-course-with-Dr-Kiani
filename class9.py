# Hierarchical inheritance
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def show(self):
        print(self.w, self.h)


class Color_rect(Rectangle):
    def __init__(self, w, h, c):
        Rectangle.__init__(self, w, h)
        self.c = c

    def show(self):
        Rectangle.show(self)
        print(self.c)


class shape(Color_rect):
    def __init__(self, w, h, c):
        Color_rect.__init__(self, w, h, c)
        self.a = self.w * self.h

    def show(self):
        Color_rect.show(self)
        print(self.a)


s = shape(3, 4, 'red')
s.show()

