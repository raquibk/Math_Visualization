import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
title = 'Spirals'
fig.set_label(title)
fig.canvas.manager.set_window_title(title)
ax = fig.add_subplot(111, polar=True)
ax.grid(False)

x = int(input("Enter the number of natural numbers:"))
N = np.arange(0, x)

if x<10:
    for number in N:
        plt.polar(number, number, 'ro')
        plt.text(number, number, '%d, %d' % (int(number), int(number)))
else:
    for number in N:
        plt.scatter(number, number, 0.5, 'red')
        plt.plot(number, number)

plt.show()