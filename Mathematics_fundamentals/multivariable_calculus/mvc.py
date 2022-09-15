from ast import Call
from gc import callbacks
from os import stat
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
        dx = 10 ** -5
        unit_vector = Vector.get_unit_vector(position = component,dimension = x.dim)
        function_diff = function(x+unit_vector*dx) - function(x)
        gradient = function_diff/dx
        return gradient

    @staticmethod
    def get_gradient(x:Vector,function:Callable) -> Vector:
        """
        Will return a gradient vector of a scalar multivariate function. (the vector of partial derivatives)
        """
        dim = x.dim
        gradient_list = []
        for component in range(dim):
            partial_derivative = MVC.get_partial_derivative(x,function,component)
            gradient_list.append(partial_derivative)
        return Vector(*gradient_list)

    @staticmethod
    def get_laplacian(x:Vector,function:Callable) -> float:
        """
        Will return a laplacian of a scalar multivariate function. (the sum of second partial derivatives)
        """
        def gradient(y:Vector):
            return MVC.get_gradient(y,function)
        return Vector_Calculus.get_divergence(x,gradient)

            
    # @staticmethod
    # def pure_gradient_descent(x:Vector,function:Callable,)

class Vector_Calculus:
    
    @property
    def levi_civita_tensor(i:int,j:int,k:int) -> int:
        """
        Will return the (i,j,k) entry of the Levi Civita tensor.
        Note i,j,k belong to the set {1,2,3}.
        """
        return(i-j)*(j-k)*(k-i)/2

    @staticmethod
    def find_ith_derivative(x:Vector,position:int,function:Callable) -> float:
        """
        Will find the derivative of the i'th component of a vector valued function
        i.e many co-ordinates to many co-ordinates.
        """
        if position > x.dim:
            return 0
        dx = 10 ** -5
        grad = function(x+Vector.get_unit_vector(position,x.dim)*dx) - function(x)
        component = Vector.unpack_vector(grad)[position]
        return component/dx

    @staticmethod
    def get_divergence(x:Vector,function:Callable) -> float:
        """
        Will get the divergence of a vector field.
        """
        output_dim = function(Vector(*[1]*x.dim)).dim
        gradients = [
            Vector_Calculus.find_ith_derivative(x,position,function)
            for position in range(output_dim)
            ]
        return sum(gradients)

    @staticmethod
    def get_curl(x:Vector,function:Callable) -> Vector:
        pass


if __name__ == '__main__':
    def f(vector):
        v = Vector.unpack_vector(vector)
        return v[0] ** 2 + v[1]
    def g(vector):
        v = Vector.unpack_vector(vector)
        return v[0]/2

    def F(vector):
        return Vector(f(vector),g(vector))

    # x = Vector(1,1,1,1)
    # def f(vector):
    #     x,y,z,w = Vector.unpack_vector(vector)
    #     return x ** 2 + y ** 2 + z ** 2 + w ** 2
    v = Vector(1,1,1,3,4,5,6)
    print(Vector_Calculus.get_divergence(v,F))