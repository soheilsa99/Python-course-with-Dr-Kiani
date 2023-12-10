from matplotlib import pyplot as plt
import numpy as np

x = [1, 5, 6, 9, 7, 3, 4]
y = [2, 10, 11, 17, 19, 20, 18]

plt.scatter(x, y)
plt.show()


print("----------------------------chart for sin --------------------------------")

x = np.arange(0, 10, 1)
y = np.sin(x)*np.log(x+7)
z = np.cos(x)
plt.plot(x, y)
plt.plot(x, z, c='r')
plt.show()


x = np.arange(0, 10, 0.5)
y = np.sin(x)*np.log(x+7)
z = np.cos(x)
plt.plot(x, y)
plt.plot(x, z, c='r')
plt.show()



x = np.arange(0, 10, 0.01)
y = np.sin(x)*np.log(x+7)
z = np.cos(x)
plt.plot(x, y)
plt.plot(x, z, c='r')
plt.show()



x = np.arange(0, 10, 0.01)
y = np.sin(x)*np.log(x+7)
z = np.cos(x)
plt.plot(x, y)
plt.scatter(x, z, c='r')
plt.show()




x = np.arange(0, 10, 0.01)
x2 = np.arange(0, 10, 1)
y = np.sin(x)*np.log(x+7)
z = np.cos(x2)
plt.plot(x, y)
plt.scatter(x2, z, c='r', marker='d')
plt.show()


