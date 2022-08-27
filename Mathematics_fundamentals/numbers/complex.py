from this import d
from real import Real
import numpy as np

class Complex:
    def __init__(self,real,imaginary):
        self.re = real
        self.im = imaginary

    def __add__(self,other):
        return Complex(self.re + other.re,self.im + other.im)

    def __sub__(self,other):
        return Complex(self.re - other.re,self.im - other.im)
        
    def __mul__(self,other):
        if isinstance(other,Complex):
                return Complex(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)
        else:
            return Complex(other * self.re,other * self.im)

    def get_conjugate(self):
        return Complex(self.re,-self.im)
        
    def get_complex_number(self):
        return f'{self.re}{"+" if self.im >= 0 else ""}{self.im}i'

    def get_magnitude(self):
        real = Real()
        return real.sqrt(self.re ** 2 + self.im ** 2)

    def get_argument(self):
        return np.arctan(self.im/self.re)

