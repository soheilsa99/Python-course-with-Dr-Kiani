def f1(a, b):
    c = a + b
    return c
#print(f1(3, 4))
x = 3
u = 4
z = f1(x, u)
print(z)

def f1(a, b):
    c = a + b
    return c
x = int(input('pleas enter value of a: '))
y = int(input('pleas enter value of b: '))
z = f1(x, y)
print(z)

# order is so important for sen variable to function
def f2(a, b):
    c = a - b
    return c


z = f1(b, a)
print(z)
# if we use print(c) we have problem !!!! the variable of function is local

def fact(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s
n = int(input('enter number:'))
print(fact(n))


def average(l):
    return sum(l)/len(l)

l = [23, 43, 53, 122, 25, 7, 5]
print(average(l))

"""
when the function has many output the result will show with tuple format
"""
def f(a, b):
    x = a - b
    y = a + b
    return x, y

print(f(3, 4))