import sys

sys.path.append("/Users/benwills/Desktop/personal_projects/Mathematics_fundamentals")

import numpy as np
from differentiation import Differentiation
from functions.functions import Functions
from visualisations.visualisations import Visualisation


diff = Differentiation()
fun = Functions()
vis = Visualisation()


def parabola(x):
    return fun.ln(x) - fun.sin(x, 2 * np.pi) - fun.bell_curve(x)


# def parab_deriv(x):
#     return diff.get_derivative(parabola,x)

# ax = vis.make_axis()
# vis.get_function_visualisation(parab_deriv,-10,10,100,ax)
# vis.show_visualisation()

print(diff.newton_raphson_method(parabola, 128, True))
