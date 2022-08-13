import numpy as np
import matplotlib.pyplot as plt

class Functions:
    def polynomial(self,x,*arr):
        output = 0
        degree = len(arr) - 1
        for index,coefficient in enumerate(arr):
            output += coefficient * x ** (degree - index)
        return output
    def reciprocal(self,x,a,b):
        if x.any() == 0:
            return 0
        return 1/(x-a) + b
    


func_space = Functions()

space = np.linspace(-5,5,100)
plt.plot(space,func_space.reciprocal(space,0,0))
plt.show()

