import datetime


class Product:
    def __init__(self, i, n, p):
        self.__id = i
        self.__name = n
        self.__price = p

    def show(self):
        print(self.__id, self.__name, self.__price)


class factor:
    def __init__(self):
        global counter
        self.__id = counter
        counter += 1
        self.__datetime = datetime.datetime.now()
        self.__total_price = 0
        self.__list_prod = []

    def show(self):
        print('__________________________FACTOR__________________________')
        print('ID: ', self.id, '\tDATE: ', self.datetime)
        print('ID\t\tNAME\t\tPRICE')
        for p in self.__list_prod:
            p.show()
        print('__________________________________________________________')
        print('TOTAL: ', self.__totalprice)


    def add_product(self, p):
        self.__list_prod.append(p)

    def compute_sum(self):
        for p in self.__list_prod:
            self.__total_price += p.price


class Customer:
    def __init__(self, i, n, f):
        self.__id = i
        self.__name = n
        self.__family = f
        self.__fact = factor()

    def show(self):
        print(self.__id, self.__name, self.__family)

    def shop(self, p):
        self.__fact.add_product(p)

    def pay(self):
        self.__fact.computesum()
        self.__fact.show()
        x = int(input('ENTER $: '))
        if x >= self.__fact.gettotal():
            print('congratulation.... :)')
        else:
            print('No enough ..... :(')

listp = \
    [
        Product(1, 'pride', 260),
        Product(2, '206', 540),
        Product(3, 'camery', 1600),
        Product(4, 'lx570', 8000),
        Product(5, 'nissan', 450)
    ]

counter = 1000
c = Customer(1, 'hesam', 'fantastic')
for p in listp:
    p.show()
    x = input('Do you want to shop it? ')
    if x == 'y':
        c.shop(p)

c.pay()
