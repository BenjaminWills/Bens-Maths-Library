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
        return np.sin(x/(2*np.pi) * frequency)

    def cos(self,x,frequency = 1):
        return np.cos(x/(2*np.pi) * frequency)
    
    def tan(self,x,frequency = 1):
        return np.tan(x/(2*np.pi) * frequency)

    def exp(self,x):
        return np.exp(x)
    
    def ln(self,x):
        if x.any() <= 0:
            return 0
        return np.log(x)

    def log_base_n(self,x,n):
        return np.log(x)/np.log(n)

    def circle(self,x,radius,centre_x,centre_y):
        if (radius ** 2 - (x-centre_x) ** 2).any() <= 0:
            return [x,0]

        y_co_ordinate = centre_y + np.sqrt(radius ** 2 - (x-centre_x) ** 2)
        return [-y_co_ordinate,y_co_ordinate]

    def hyperbola(self,x,major,minor):
        y_co_ordinate = major * np.sqrt(1+(x/minor) ** 2)
        return [-y_co_ordinate,y_co_ordinate]

    def elipse(self,x,major,minor):
        if (1-(x/minor) ** 2).any() <= 0:
            return [x,0]
        y_co_ordinate = major * np.sqrt(1-(x/minor) ** 2)
        return [-y_co_ordinate,y_co_ordinate]