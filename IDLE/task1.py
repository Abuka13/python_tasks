import numpy as np
import matplotlib.pyplot as plt
print('Write output messg.')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
x = np.linspace(-100, 100, 1000)
y = a*x**2 + b*x + c
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
