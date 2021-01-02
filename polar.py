import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
import numpy as np

x = int(input("Enter the number of natural numbers:"))
N = np.arange(0, x)

if x<10:
    for number in N:
        plt.polar(number, number, 'ro')
        plt.text(number, number, '%d, %d' % (int(number), int(number)))
else:
    for number in N:
        plt.polar(number, number, 'ro')

plt.show()