import sys
sys.path.append('/Users/benwills/Desktop/personal_projects/Mathematics_fundamentals')

from numbers.real import Real
import numpy as np
import math 

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
            return f"""Iteration count: {iteration_count}, root: ({x0},{function(x0)})"""
        return [[x0],[function(x0)]]

    def get_nth_derivative(self,function,x,order = 1):
        # at each point we need to find another derivative of a derivative.
        if order == 1:
            return self.get_derivative(function,x)
        else:
            def deriv(x):
                return self.get_derivative(function,x)
            return self.get_nth_derivative(deriv,x,order-1)
        

    def taylor_series(self,function,x,order,centre = 0):
        output = function(centre)
        for i in range(1,order):
            output += (self.get_nth_derivative(function,centre,order) * ((x - centre) ** order)) / math.factorial(order)
        return output


diff = Differentiation()

def polynomial(x):
    return x**2


from visualisations.visualisations import Visualisation

def taylor_approximation(x):
    return diff.taylor_series(polynomial,x,2)

# vis = Visualisation()
# ax = vis.make_axis()
# vis.get_function_visualisation(polynomial,-10,10,1000,ax)
# vis.get_function_visualisation(taylor_approximation,-10,10,1000,ax)
# vis.show_visualisation()

print(diff.taylor_series(polynomial,1,10)) # PRECISION ISSUE IN NTH DERIVATIVE FUNCTION. TODO FIX.