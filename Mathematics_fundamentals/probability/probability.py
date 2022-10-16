import random

import numpy as np

from Mathematics_fundamentals.calculus.integration.integration import \
    Integration
from Mathematics_fundamentals.functions.functions import Functions
from Mathematics_fundamentals.numbers.numbers import Real


class Probability:
    """
    A class that contains all things probability!
    """
    

    @staticmethod
    def uniform_distribution_pdf(lower:float,upper:float) -> float:
        """_summary_

        Parameters
        ----------
        lower : float
        upper : float

        Returns
        -------
        float
            Probability of choosing x in the range [lower,upper]

        Raises
        ------
        ValueError
            If lower >= upper
        """

        if upper <= lower:
            raise ValueError("The upper bound is less than or equal to the lower bound.")
        return 1/(upper-lower)

    @staticmethod
    def uniform_distribution_cdf(lower:float,upper:float,x:float) -> float:
        """Will return the probability of finding a number <= x, within a uniform distribution
        defined on the range [lower,upper].

        Parameters
        ----------
        lower : float
            Lower bound
        upper : float
            Upper bound
        x : float
            The number that we are interested in, must be in range [lower,upper]

        Returns
        -------
        float
            probability that we find a number that is <= x.
        """
        if lower < upper:
            return random.uniform(lower,upper)
        else:
            raise ValueError('Lower is greater than or equal to upper.')

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
        if n < x or probability < 0 or probability > 1:
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
            cdf += Probability.binomial_pdf(
                probability = probability,
                n = n,
                x = i)
        return cdf

    @staticmethod
    def normal_pdf(x:float,mean:float,variance:float) -> float:
        """Returns the probability of choosing x in a normal distribution.

        Parameters
        ----------
        mean : float
            Mean value of normal distribution (horizontal shift)
        variance : float
            Variance of the normal distribution (stretch)
        x : float
            Value to evaluate probability of

        Returns
        -------
        float
            Probability of choosing exactly x in a normal distribution

        Raises
        ------
        ValueError
            Cannot have a negative variance.
        """
        if variance < 0:
            raise ValueError("Variance can't be negative")
        stretch_factor = 1/(np.sqrt(2 * np.pi * variance))
        exponential_factor = -1/2 * ((x-mean)**2)/variance
        return stretch_factor * Functions.exp(exponential_factor)

    @staticmethod
    def normal_cdf(mean:float,variance:float,x:float) -> float:
        """Returns the probability of choosing <= x in a normal distribution with mean and variance.

        Parameters
        ----------
        mean : float
            Mean value of normal distribution (horizontal shift)
        variance : float
            Variance of the normal distribution (stretch)
        x : float
            Value to evaluate probability of

        Returns
        -------
        float
            The probability of choosing <= x in a normal distribution with mean and variance.
        """
        integratable_pdf = lambda x : Probability.normal_pdf(x,mean,variance)
        return Integration.simpson_approximation(
            function = integratable_pdf,
            start = -10_000,
            end = x,
            steps = 10000
        )

    @staticmethod
    def standard_normal_cdf(mean:float,variance:float,x:float) -> float:
        if mean !=0 and variance != 1:
            standardised_import = (x-mean)/np.sqrt(variance)
        return Probability.normal_cdf(
            mean=0,
            variance=1,
            x = standardised_import
        )

class Empirical_probability():

    def get_mean(data:list) -> float:
        """Will find the mean of a list of data

        Parameters
        ----------
        data : list
            A list of numbers

        Returns
        -------
        float
            The mean of the inputted list
        """
        n = len(data)
        sum = sum(data)
        return sum/n