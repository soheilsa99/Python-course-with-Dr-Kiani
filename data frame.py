import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
#pandas make file as dataframe
df = pd.read_excel('Book1.xlsx', sheet_name='Sheet1', engine='openpyxl')
print(df)
name = df['name']
height = df['height']
weight = df['weight']
# filter process in dataframe
print("----------------- height < 170 ----------------------")
print(df[df['height'] < 170])
print("----------------- weight < 80 ----------------------")
print(df[df['weight'] < 80])
print("----------------- print special name ----------------------")
print(df.iat[2, 0])
print("----------------- show data in the chart ----------------------")
"""
plt.bar(x, y )
we should define x and y for chart
"""
plt.bar(name, height)
plt.show()
"""
pandas isn't good choice for big data and dataset, SQL is good choice :)
"""

x = np.arange(0, 10, 0.01)
x2 = np.arange(0, 10, 1)
y = np.sin(x)*np.log(x+7)
z = np.cos(x2)
df = pd.DataFrame(columns=['x2', 'z'])

for i in range(10):
    d = {'x2' : x2[i], 'z' : z[i]}
    df = df._append(d, ignore_index=True)
print(df)

df.to_excel('book2.xlsx')

"""
opening the text file
"""

f = open('sls.txt')
x = f.read()
print(x)

# just for write in text 'w'
f = open('sls.txt', 'w')
f.write('dfefwefewfwfe')

# for write in text
f = open('sls.txt', 'a')
f.write('dfefwefewfwfe')