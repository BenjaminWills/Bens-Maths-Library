# from complex import Complex
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

    def get_powerset(self,arr:list):
        """
        This function will find the set of all subsets of an array (excluding the empty set),
        for an array of length n the power set has a length of 2 ** n - 1.

        for [1,2] the power set is [],[1],[2],[1,2]. Note that it has 4 elements.
        """
        power_set = []
        n = len(arr)
        for i in range(2 ** n):
            sub_set = []
            for j in range(n):
                if i & 2 ** j:
                    sub_set.append(arr[j])
            power_set.append(sub_set)
        return power_set

num = Real()
list = [1,2,3]
power_set = num.get_powerset(list)
print(power_set)
