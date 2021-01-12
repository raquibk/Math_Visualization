import matplotlib.pyplot as plt
import numpy as np

def allnumbers():
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

def three():
    fig = plt.figure()
    title = 'Spirals'
    fig.set_label(title)
    fig.canvas.manager.set_window_title(title)
    ax = fig.add_subplot(111, polar=True)
    ax.grid(True)

    plt.polar(3, 3, 'ro')
    plt.text(3, 3, '%d, %d' % (int(3), int(3)))

    plt.show()

def fortyfour():
    fig = plt.figure()
    title = 'Spirals'
    fig.set_label(title)
    fig.canvas.manager.set_window_title(title)
    ax = fig.add_subplot(111, polar=True)
    ax.grid(True)

    plt.polar(44, 44, 'ro')
    plt.text(44, 44, '%d, %d' % (int(44), int(44)))

    plt.show()


def seventen():
    fig = plt.figure()
    title = 'Spirals'
    fig.set_label(title)
    fig.canvas.manager.set_window_title(title)
    ax = fig.add_subplot(111, polar=True)
    ax.grid(True)

    plt.polar(710, 710, 'ro')
    plt.text(710, 710, '%d, %d' % (int(710), int(710)))

    plt.show()

fortyfour()
