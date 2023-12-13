import datetime


class Product:
    def __init__(self, i, n, p):
        self.id = i
        self.name = n
        self.price = p

    def show(self):
        print(self.id, self.name, self.price)


class factor:
    def __init__(self):
        global counter
        self.id = counter
        counter += 1
        self.datetime = datetime.datetime.now()
        self.total_price = 0
        self.list_prod = []

    def show(self):
        print('__________________________FACTOR__________________________')
        print('ID: ', self.id, '\tDATE: ', self.datetime)
        print('ID\t\tNAME\t\tPRICE')
        for p in self.listprod:
            p.show()
        print('__________________________________________________________')
        print('TOTAL: ', self.totalprice)


    def add_product(self, p):
        self.list_prod.append(p)

    def compute_sum(self):
        for p in self.list_prod:
            self.total_price += p.price


class Customer:
    def __init__(self, i, n, f):
        self.id = i
        self.name = n
        self.family = f
        self.fact = factor()

    def show(self):
        print(self.id, self.name, self.family)

    def shop(self, p):
        self.fact.add_product(p)

    def pay(self):
        self.fact.computesum()
        self.fact.show()
        x = int(input('ENTER $: '))
        if x >= self.fact.gettotal():
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
