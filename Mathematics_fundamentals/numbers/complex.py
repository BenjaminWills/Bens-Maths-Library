from real import Real
import numpy as np

class Complex:
    def __init__(self,real,imaginary):
        self.re = real
        self.im = imaginary

    def get_conjugate(self):
        return Complex(self.re,-self.im)
        
    def get_complex_number(self):
        return f'{self.re}{"+" if self.im >= 0 else ""}{self.im}i'

    def get_magnitude(self):
        real = Real()
        return real.sqrt(self.re ** 2 + self.im ** 2)

    def get_argument(self):
        return np.arctan(self.im/self.re)

    def multiply_complex(self,num):
        if isinstance(num,Complex):
                return Complex(self.re * num.re - self.im * num.im, self.re * num.im + self.im * num.re)
        else:
            return Complex(num * self.re,num * self.im)
    
a = Complex(4,2)
b = a.get_conjugate()
# print(a.get_complex_number(),b.get_complex_number())
print(a.multiply_complex(b).get_complex_number())
