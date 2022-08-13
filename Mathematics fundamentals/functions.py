import numpy as np
import matplotlib.pyplot as plt


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


func_space = Functions()

space = np.linspace(-5, 5, 100)
plt.plot(space, func_space.step(space, 0))
plt.show()
