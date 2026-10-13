import matplotlib.pyplot as plt
import numpy as np

a = np.arange(1, 11, 1)

b1 = (3 * a) + 2
b2 = (a**2) + 3

plt.figure(figsize=(7, 5))

plt.plot(a, b1, 'b', linewidth=3, label='y=3x+2')
plt.plot(a, b2, 'm', linewidth=3, label='y=x^2+3')

plt.legend(loc='upper left')
plt.show()
