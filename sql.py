import sqlite3
from sqlite3 import Connection
Connection = sqlite3.connect('database.db')
cursor = Connection.cursor()

# cursor.execute('create table product (id int primary key, name nvarchar(20), price int)')
# cursor.execute("insert into product values (1,'pride',250)")
# cursor.execute("insert into product values (2, '206',500)")
# cursor.execute("insert into product values (3, 'lexus',7500)")
# cursor.execute("insert into product values (4, 'Lmamad',590)")
#
# Connection.commit()

cursor.execute('select * from product')
L = cursor.fetchall()
print(L)

cursor.execute('select * from product where price > 500')
L = cursor.fetchall()
print(L)

cursor.execute('select sum (price) from product ')
L = cursor.fetchall()
print(L)


cursor.execute('select max (price) from product ')
L = cursor.fetchall()
print(L)

# also we can find avg and min and .....

