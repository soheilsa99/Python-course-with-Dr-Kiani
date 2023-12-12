class Employee:
    def __init__(self, n, f, r, s):
        self.name = n
        self.family = f
        self.__rank = r
        self.__salary = s

    def show(self):
        print(self.name, self.family, self.__rank)
        if type == 'head' or type == 'admin':
            print(self.__salary)

    def change_rank(self, r):
        if type == 'admin' :
            self.__rank = r

    def change_salary(self, s):
        if type == 'admin':
            self.__salary = s


type = 'user'
u = input('User: ')
p = input('Password: ')
if (u == 'admin' and p == '123') or (u == 'head' and p == '456'):
    type = u

e = Employee('a', 'b', 2, 20)
e.show()
e.change_rank(3)
e.show()

