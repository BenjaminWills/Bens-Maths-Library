import sys
sys.path.append('/Users/benwills/Desktop/personal_projects/Mathematics_fundamentals')

import numpy as np

class Differentiation:
    def get_derivative(self,function,x):
        dx = 10 ** -5
        vert_change = function(x+dx) - function(x)
        slope = vert_change/dx
        return slope
    
    def newton_raphson_method(self,function,initial_point, verbose = False):
        x0 = initial_point
        max_iterations = 100000
        iteration_count = 0
        while abs(self.get_derivative(function,x0)) > 10 ** -5:
            if iteration_count == max_iterations:
                return 'DIVERGENT: possibly a saddle point nearby.'
            slope = self.get_derivative(function,x0)
            func_value = function(x0)
            x0 = x0 - (func_value/slope)
            iteration_count += 1
        x0 = np.round(x0,4)
        if verbose:
            return \
                f"""Iteration count: {iteration_count}, root: ({x0},{function(x0)})"""

        return [[x0],[function(x0)]]

    def taylor_series(self,function,degree,centre):
        pass


