import random

from Mathematics_fundamentals.numbers.numbers import Real


class Probability:
    """
    A class that contains all things probability!
    """

    @staticmethod
    def uniform_distribution_cdf(lower:float,upper:float,x:float) -> float:
        """Will return the probability of finding a number x, within a uniform distribution
        defined on the range [lower,upper].

        Parameters
        ----------
        lower : float
            Lower bound
        upper : float
            Upper bound

        Returns
        -------
        float
            probability that we find a number that is <= x.
        """
        if lower < upper:
            return random.uniform(lower,upper)
        else:
            raise TypeError('Lower is greater than or equal to upper.')

    @staticmethod
    def binomial_pdf(probability:float,n:int,x:int) -> float:
        """Will find the probability of finding exactly x occurances
        of an event in a binomial distribution

        Parameters
        ----------
        probability : float
            A number in (0,1] that defines the probability of success
        n : int
            Number of samples
        x : int
            Number of occurrences of event

        Returns
        -------
        float
            The probability of x events happening with a probability p of success 
            and n samples.
        """
        if n < x or 0 < probability <= 1:
            return TypeError("Invalid values entered.")
        n_choose_x = Real.n_choose_m(n,x)
        return n_choose_x * (probability ** x) * (1-probability) ** (n-x)

    @staticmethod
    def binomial_cdf(probability:float,n:int,x:int) -> float:
        """Will find the probability of finding <= x occurrences
        of an event in a binomial distribution

        Parameters
        ----------
        probability : float
            A number in (0,1] that defines the probability of success
        n : int
            Number of samples
        x : int
            Number of occurrences of event

        Returns
        -------
        float
            The probability of <= x events happening with a probability p of success 
            and n samples.
        """
        cdf = 0
        for i in range(x+1):
            cdf += Probability.binomial_pdf(probability,n,i)
        return cdf