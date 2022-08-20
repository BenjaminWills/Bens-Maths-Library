from real import Real

class Complex:
    def __init__(self,real,imaginary):
        self.re = real
        self.im = imaginary

    def get_conjugate(self):
        return Complex(self.re,-self.im)
        
    def get_magnitude(self):
        real = Real()
        return real.sqrt(self.re ** 2 + self.im ** 2)

z = Complex(1,4)
z_bar = z.get_conjugate()
print(z_bar.get_magnitude())