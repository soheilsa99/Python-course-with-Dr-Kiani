"""
about global and local variable
"""
print("---------------------local variable-------------")
def fun():
    a = 10
    print(a)
a = 5
print(a)
fun()
print(a)

print("\n---------------------local variable-------------")

def fun():
    global a
    a = 10
    print(a)
a = 5
print(a)
fun()
print(a)