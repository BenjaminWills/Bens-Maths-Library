from ast import Num
from complex import Complex
import numpy as np

class Real:
    def sqrt(self,x):
        if x < 0:
            return Complex(0,np.sqrt(-x))
        else:
            return np.sqrt(x)

num = Real()