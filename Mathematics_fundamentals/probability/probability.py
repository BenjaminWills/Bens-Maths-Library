import random


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
        """_summary_

        Parameters
        ----------
        probability : float
            _description_
        n : int
            _description_
        x : int
            _description_

        Returns
        -------
        float
            _description_
        """