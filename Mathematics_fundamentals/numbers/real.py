from complex import Complex
import numpy as np

class Real:
    def sqrt(self,x):
        if x < 0:
            return Complex(0,np.sqrt(-x))
        else:
            return np.sqrt(x)

    def factorial(self,x):
        if x == 0:
            return 1
        else:
            return x * self.factorial(x-1)