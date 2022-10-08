from mvc import *
from mvc import Matrix, Vector


def f(x):
    v = Vector.unpack_vector(x)
    # return (1-v[0]) ** 2 + 100 * ((v[1]-v[0]**2) ** 2)
    return (v[0]-1) ** 2 + v[1] ** 2 + 1

def backtrack(
    x0,
    f,
    grad,
    t = 1,
    alpha = 0.2,
    beta = 0.8
):
    while f(x0 - grad*t) > f(x0) + alpha * t * Vector.get_dot_product(grad,grad * -1):
        t *= beta
    return t

def grad(
    point,
    max_iter,
    f
):
    iter = 1
    grad = MVC.get_gradient(point,f)
    while(abs(grad.get_magnitude()) > 10 ** -5):
        grad = MVC.get_gradient(point,f)
        t = backtrack(point,f,grad)
        point = point - grad * t

        # print(point.vector,f(point),grad.vector,iter)
        print(f'at iteration {iter}, \n point is {point.vector}, \n the f(point) = {f(point)}, \n the gradient is {grad.vector}')
        iter += 1
        if iter > max_iter:
            break
    return point


point = Vector(2,2)
MAX_ITTER = 10_000

grad(point,MAX_ITTER,f)