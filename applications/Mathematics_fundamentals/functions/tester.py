
from Mathematics_fundamentals.functions.functions import Functions
from Mathematics_fundamentals.visualisations.visualisations import \
    Visualisation

func_space = Functions()
visualiser = Visualisation()


def line(x):
    return func_space.line(x, 3, 1)


def circle(x):
    return func_space.circle(x, 4, 0, 0)


ax = visualiser.make_axis()
visualiser.get_function_visualisation(line, -4, 4, 100, ax)
visualiser.get_conic_visualisation(circle, -4, 4, 100, ax)
visualiser.show_visualisation()
