import sys
sys.path.append('/Users/benwills/Desktop/personal_projects/Mathematics_fundamentals')

from linear_algebra import Linalg
from functions.functions import Functions
from visualisations.visualisations import Visualisation

import numpy as np


theta = 5 / 3 * np.pi
TRANSFORMATION_MATRIX = [
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta), np.cos(theta)],
]


lin = Linalg()
func = Functions()
vis = Visualisation()

ax = vis.make_axis()

# Example of solving a linear equation

a = [[1,2],[2,1]]
print(lin.get_inverted_matrix(a))




