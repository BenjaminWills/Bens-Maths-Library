from complex import Complex
import numpy as np


class Real:
    def sqrt(self, x):
        if x < 0:
            return Complex(0, np.sqrt(-x))
        else:
            return np.sqrt(x)

    def factorial(self, x):
        if x == 0:
            return 1
        else:
            return x * self.factorial(x - 1)

    def get_powerset(self, arr: list):
        """
        This function will find the set of all subsets of an array,
        for an array of length n the power set has a length of 2 ** n.

        for [1,2] the power set is [],[1],[2],[1,2]. Note that it has 4 elements.
        """
        power_set = []
        n = len(arr)
        for i in range(2**n):
            sub_set = []
            for j in range(n):
                if i & 2**j:
                    sub_set.append(arr[j])
            power_set.append(sub_set)
        return power_set

    def is_prime(self, n):
        for i in range(2, int(n / 2)):
            if n % i == 0:
                return False
        return True

    def find_HD_and_LD(self, x):
        """
        Finds highest and lowest divisor of a number (one of which will always be prime.)
        """
        for i in range(2, int(x / 2)):
            if x % i == 0:
                LD = i
                HD = int(x / i)
                return [LD, HD]

    def prime_factors(self, n):
        i = n
        list_of_prime_factors = []
        while not self.is_prime(i):
            HD_LD = self.find_HD_and_LD(i)
            list_of_prime_factors.append(HD_LD[0])
            i = HD_LD[1]
        list_of_prime_factors.append(i)
        factor_dict = {}
        for i in list_of_prime_factors:
            if str(i) not in factor_dict.keys():
                factor_dict[str(i)] = 1
            else:
                factor_dict[str(i)] += 1
        return factor_dict
