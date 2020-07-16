import matplotlib.pyplot as plt
import random

X1 = [random.random() for i in range(0,20)]
Y1 = [random.random()+2*i for i in X1]

plt.scatter(X1, Y1)
plt.grid()
plt.xlabel("X")
plt.ylabel("Y")
plt.show()