import sys
from typing import Callable

sys.path.append('/Users/benwills/Desktop/personal_projects/Mathematics_fundamentals/linear_algebra')

from linear_algebra import Vector

class MVC:
    @staticmethod
    def get_partial_derivative(x:Vector,function:Callable,component:int) -> float:
        """
        Will get the derivative of a scalar valued function f(x,y,z,...) w.r.t the specified
        component
        """
        dx = 10 ** -8
        unit_vector = Vector.get_unit_vector(position = component,dimension = x.dim)
        function_diff = function(x+unit_vector*dx) - function(x)
        gradient = function_diff/dx
        return gradient
    @staticmethod
    def get_gradient(x:Vector,function:Callable) -> Vector:
        """
        Will return a gradient vector of a multivariate function. (the vector of partial derivatives)
        """
        dim = x.dim
        gradient_list = []
        for component in range(dim):
            partial_derivative = MVC.get_partial_derivative(x,function,component)
            gradient_list.append(partial_derivative)
        return Vector(*gradient_list)




if __name__ == '__main__':
    def f(v):
        x,y,z = Vector.unpack_vector(v)
        return x + 2*y - z

    v = Vector(1,1,1)
    deriv = MVC.get_gradient(v,f)
    print(deriv.vector)