import sys
from os import stat
from typing import Callable
from xmlrpc.client import Boolean

sys.path.append('/Users/benwills/Desktop/personal_projects/Mathematics_fundamentals/linear_algebra')
sys.path.append('/Users/benwills/Desktop/personal_projects/Mathematics_fundamentals/functions')

from functions import Functions
from linear_algebra import Matrix, Vector


class MVC:

    @staticmethod
    def get_partial_derivative(
        x:Vector,
        function:Callable,
        component:int) -> float:
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
    def get_gradient(
        x:Vector,
        function:Callable) -> Vector:
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
    def get_hessian(
        x:Vector,
        function:Callable) -> Matrix:
        """
        The hessian matrix contains the second derivatives of a function, the 
        (i,j) index of this matrix is the second derivative of the function w.r.t
        to i then to j. 

        NOTE: This matrix will have outputs equal to the dimension of the input,
        as all other entries would be zero.

        NOTE TO BEN: could use symmetry to speed up.
        """
        matrix_dimension = x.dim
        hessian = Matrix()
        for i in range(matrix_dimension):
            row = []
            for j in range(matrix_dimension):
                row.append(
                    Vector_Calculus.get_nth_derivative(
                        x,
                        2,
                        (i,j),
                        function))
            hessian.add_rows(row)
        return hessian

    @staticmethod
    def get_laplacian(
        x:Vector,
        function:Callable) -> float:
        """
        Will return a laplacian of a scalar multivariate function. (the sum of second partial derivatives)
        """
        def gradient(y:Vector):
            return MVC.get_gradient(y,function)
        return Vector_Calculus.get_divergence(x,gradient)

            
    @staticmethod
    def pure_gradient_descent(
        x:Vector,
        function:Callable,
        alpha:float,
        tolerance:float,
        max_iterations:int = 10_000,
        condition_number:bool = False) -> Vector:
        """
        For pure gradient descent, we have a few parameters that need defining:
            - x = starting vector
            - alpha = jump rate
            - tolerance = stopping criterion
            - max_iterations = max iterations before we terminate the program.

        First we check the hessian, to see if it is positive or negative definite.
        (can be found from the eigenvalues.)
        """
        hessian = MVC.get_hessian(x,function)
        if condition_number:
            eigenvalues = hessian.get_eigenvalues()
            condition = max(eigenvalues)/min(eigenvalues)
            print(condition)
        iter_count = 0
        x0 = x
        while abs(MVC.get_gradient(x0,function).get_magnitude()) > tolerance:
            iter_count += 1
            gradient = MVC.get_gradient(x0,function)
            grad_mag = 1/(gradient.get_magnitude())
            unit_gradient = gradient * grad_mag
            x0 = x - unit_gradient * alpha
            if iter_count > max_iterations:
                print(f"Exited, number of iterations > {max_iterations}")
                break
        print(f"iterations: {iter_count}")
        return x0

    @staticmethod
    def backtrack(
        x:Vector,
        function:Callable,
        grad:Vector,
        t:float = 1,
        alpha:float = 0.2,
        beta:float = 0.8
    ):
        """_summary_

        Parameters
        ----------
        x : Vector
            Vector to start line backtracking search
        function : Callable
            function
        grad : Vector
            gradient of function at that point
        t : float, optional
            initial value of the learning rate, by default 1
        alpha : float, optional
            backtracking coefficient (between 0 and 1), by default 0.2
        beta : float, optional
            The backtracking decrease rate (always between 0 and 1), by default 0.8

        Returns
        -------
        _type_
            _description_
        """
        while function(x - grad*t) > function(x) + alpha * t * Vector.get_dot_product(grad,grad * -1):
            t *= beta
        return t

    @staticmethod
    def backtracking_gradient_descent(
        x:Vector,
        function:Callable,
        tolerance:float,
        beta:float = 0.8,
        alpha:float = 0.2,
        max_iterations:int = 10_000,
        verbose:bool = False) -> Vector:
        """
        This version of gradient descent will calculate the learning rate at each step using the 
        backtracking line search algorithm.

        Parameters
        ----------
        x : Vector
            Initial point
        function : Callable
            Function that we wish to minimize
        tolerance : float
            Sufficient ending condition
        beta : float, optional
            The backtracking decrease rate (always between 0 and 1), by default 0.8
        alpha : float, optional
            backtracking coefficient (between 0 and 1), by default 0.2
        max_iterations : int, optional
            Maximum allowed condition before exiting the function, by default 10_000
        verbose : bool, optional
            Will print out at each step, by default False

        Returns
        -------
        Vector
            co-ordinates of minimal vector
        """
        iter = 1
        grad = MVC.get_gradient(x,function)
        while(abs(grad.get_magnitude()) > tolerance):
            grad = MVC.get_gradient(x,function)
            t = MVC.backtrack(x,function,grad,alpha = alpha,beta = beta)
            x = x - grad * t
            if verbose:
                print(f'at iteration {iter}, \n x is {x.vector}, \n the f(x) = {function(x)}, \n the gradient is {grad.vector}')
            iter += 1
            if iter > max_iterations:
                break
        return x

    @staticmethod
    def pure_newton_method(
        x:int,
        function:Callable,
        tolerance:float,
        max_iterations:int = 10_000) -> Vector:
        """
        The pure newton method only works if the hessian at the point x is positive definite.
        but we wont enforce that, as the problem is fixed with the hybrid newton-gradient method.

        tolerance - Stopping condition
        """
        iter_count = 0
        x0 = x
        gradient = MVC.get_gradient(x0,function)
        while abs(gradient.get_magnitude()) > tolerance:
            iter_count += 1
            gradient = MVC.get_gradient(x0,function)
            hessian = MVC.get_hessian(x0,function)
            inv_hessian = hessian.get_inverted_matrix()
            x0 = x0 - inv_hessian * gradient
            if iter_count > max_iterations:
                print(f"Exited, number of iterations > {max_iterations}")
                break
        print(f"iterations: {iter_count}")
        return x0    
            
class Vector_Calculus:
    
    @staticmethod
    def levi_civita_tensor(
        i:int,
        j:int,
        k:int) -> int:

        """
        Will return the (i,j,k) entry of the Levi Civita tensor.
        Note i,j,k belong to the set {1,2,3}.
        """
        return(i-j)*(j-k)*(k-i)/2

    @staticmethod
    def get_ith_component_derivative(
        x:Vector,
        position:int,
        wrt:int,
        function:Callable) -> float:
        """
        Will find the derivative of the position'th component of a vector valued function (i.e many co-ordinates to many co-ordinates.) 
        w.r.t the specified co-ordinate.
        """
        if position > x.dim:
            return 0
        dx = 10 ** -5
        grad = function(x+Vector.get_unit_vector(wrt,x.dim)*dx) - function(x)
        component = Vector.unpack_vector(grad)[position]
        return component/dx
        
    @staticmethod
    def get_nth_derivative(
        x:Vector,
        order:int,
        w_r_t:tuple,
        function:Callable,
        position:int = -1) -> float:
        """
        Will get the n'th derivative of a multivariate_function w.r.t a list of
        equal length to the order, eg second derivative w.r.t the first co-ordinate
        would have w_r_t = (0,0).
        """
        if position == -1:
            if order == 1:
                return MVC.get_partial_derivative(x,function,w_r_t[-1])
            else:
                def derivative_wrt_i(x):
                    return MVC.get_partial_derivative(x,function,w_r_t[-order])
                return Vector_Calculus.get_nth_derivative(x,order - 1,w_r_t,derivative_wrt_i)
        else:
            if order == 1:
                return Vector_Calculus.get_ith_component_derivative(x,position,w_r_t[-1],position)
            else:
                def derivative_wrt_i(x):
                    return Vector_Calculus.get_ith_component_derivative(x,position,w_r_t[-order],function)
                return Vector_Calculus.get_nth_derivative(x,order - 1,w_r_t,derivative_wrt_i,position)

    @staticmethod
    def get_divergence(
        x:Vector,
        function:Callable) -> float:
        """
        Will get the divergence of a vector field.
        """
        output_dim = function(Vector(*[1]*x.dim)).dim
        gradients = [
            Vector_Calculus.get_ith_component_derivative(x,position,position,function)
            for position in range(output_dim)
            ]
        return sum(gradients)

    @staticmethod
    def get_curl(
        x:Vector,
        function:Callable) -> Vector:
        """
        Will find the curl of a vector valued function. 
        """
        curl = []
        for i in range(3):
            row_total = 0
            for j in range(3):
                for k in range(3):
                    levi = Vector_Calculus.levi_civita_tensor(i+1,j+1,k+1) # List indexes are one less than actual indexes.
                    if levi != 0:
                        row_total += levi*Vector_Calculus.get_ith_component_derivative(x,j,k,function)
            curl.append(row_total)
        return Vector(*curl)


if __name__ == '__main__':
    def f(x):
        v = Vector.unpack_vector(x)
        return v[0] ** 2 + (v[1] + 1) ** 2


    x = Vector(5,8)
    min = MVC.backtracking_gradient_descent(
        x,
        f,
        10 ** -5
    )
    min.show_vector()