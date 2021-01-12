import matplotlib.pyplot as plt
import math
import numpy as np

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

def fibonacci(n):
    fibo = [0, 1]
    global gratio
    gratio = []
    for i in range(2,n):
        fibo.append(fibo[i-2]+fibo[i-1])


    for n in range(1, len(fibo)):
        try:
            gratio.append(fibo[n]/fibo[n-1])
        except ZeroDivisionError:
            gratio.append(0)



    plt.plot(gratio)
    plt.show()

if __name__ == "__main__":
    loop = False
    while loop is False:
        choice = int(input("Press 1 to see a variation of Ulam Spirals, and 2 to see the Golden Ratio tend to it's value: "))

        if choice ==1:
            loop = True
            x = int(input("Enter the number of natural numbers you want plotted:"))
            spiral = Spirals(x)
            spiral.plot()
        elif choice == 2:
            loop = True
            n = int(input('How many Fibonacci Numbers?: '))
            fibonacci(n)