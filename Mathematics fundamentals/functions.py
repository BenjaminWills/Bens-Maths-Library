import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')

class Functions:
    def line(self, x, gradient, intercept):
        return gradient * x + intercept

    def polynomial(self, x, *coefficients):
        output = 0
        degree = len(coefficients) - 1
        for index, coefficient in enumerate(coefficients):
            output += coefficient * x ** (degree - index)
        return output

    def reciprocal(self, x, horizontal_shift, vertical_shift):
        if x.any() == 0:
            return 0
        return 1 / (x - horizontal_shift) + vertical_shift

    def step(self, x, horizontal_shift):
        if x.any() == horizontal_shift:
            return 1
        else:
            return 0

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sinh(self, x):
        return 1 / 2 * (np.exp(x) - np.exp(-x))

    def cosh(self, x):
        return 1 / 2 * (np.exp(x) + np.exp(-x))

    def tanh(self, x):
        if x.any() == 0:
            return 0
        return self.sinh(x) / self.cosh(x)

    def sin(self, x, frequency):
        return np.sin(x * frequency)

    def get_visualisation(self, function, start, end, steps):
        if start >= end:
            return None
        plotting_space = np.linspace(start, end, steps)
        fig, ax = plt.subplots()
        ax.plot(plotting_space, function(plotting_space))
        ax.set_aspect('auto')
        ax.grid(True, which='both',linestyle=':')
        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.yaxis.tick_left()
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')
        ax.xaxis.tick_bottom()
        plt.show()


func_space = Functions()


def sigmoid(x):
    return func_space.sigmoid(x)
func_space.get_visualisation(sigmoid, -5, 5, 100)
