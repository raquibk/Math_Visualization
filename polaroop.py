import matplotlib.pyplot as plt
import numpy as np


x = int(input("Enter the number of natural numbers you want plotted:"))

class Spirals:
    def __init__(self, number):
        self.number = number

    def plot(self):
        fig = plt.figure()
        title = 'Spirals'
        fig.set_label(title)
        fig.canvas.manager.set_window_title(title)
        ax = fig.add_subplot(111, polar=True)
        ax.grid(False)
        self.N = np.arange(0, self.number)

        if self.number < 10:
            for num in self.N:
                plt.polar(num, num, 'ro')
                plt.text(num, num, '%d, %d' % (int(num), int(snum)))
        else:
            for num in self.N:
                plt.scatter(num, num, 0.5, 'red')
                plt.plot(num, num)

        plt.show()

    def plotnum(self):
        fig = plt.figure()
        title = 'Spirals'
        fig.set_label(title)
        fig.canvas.manager.set_window_title(title)
        ax = fig.add_subplot(111, polar=True)
        ax.grid(True)

        plt.polar(self.number, self.number, 'ro')
        plt.text(self.number, self.number, '%d, %d' % (int(self.number), int(self.number)))

        plt.show()

number = Spirals(x) 
number.plot()