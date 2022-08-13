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

    def reciprocal(self, x, horizontal_shift = 0, vertical_shift = 0):
        if x.any() == 0:
            return 0
        return 1 / (x - horizontal_shift) + vertical_shift

    def step(self, x, horizontal_shift = 0):
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
    
    def bell_curve(self,x, stretch = 1, horizontal_shift = 0):
        return stretch * np.exp(- (x+horizontal_shift) ** 2)

    def sin(self, x, frequency = 1):
        return np.sin(x * frequency)

    def cos(self,x,frequency = 1):
        return np.cos(x * frequency)
