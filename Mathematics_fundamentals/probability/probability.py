import random


class Probability:
    """
    A class that contains all things probability!
    """

    @staticmethod
    def uniform_distribution(lower:float,upper:float) -> float:
        """Will return a value in the range [lower,upper] according to the
        uniform distribution, in which each value is equally likely to be chosen with
        probability 1/(upper-lower).

        Parameters
        ----------
        lower : float
            Lower bound
        upper : float
            Upper bound

        Returns
        -------
        float
            
        """
        if lower < upper:
            return random.uniform(lower,upper)
        else:
            raise TypeError('Lower is greater than or equal to upper.')

    