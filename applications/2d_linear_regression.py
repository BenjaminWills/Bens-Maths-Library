"""
Linear regression beginning with 2-d
"""
TRAIN_NUM = 700
TEST_NUM = 200
import csv

from ..Mathematics_fundamentals.linear_algebra.linear_algebra import Vector
from ..Mathematics_fundamentals.multivariable_calculus.mvc import MVC

with open("/Users/benwills/Desktop/personal_projects/test.csv", newline="") as f:
    reader = csv.reader(f)
    training_data = list(reader)

with open("/Users/benwills/Desktop/personal_projects/train.csv", newline="") as f:
    reader = csv.reader(f)
    test_data = list(reader)

def cost_function(vector: Vector, data: list = training_data[:TRAIN_NUM]) -> float:
    m, c = Vector.unpack_vector(vector)
    n = len(data)
    sum = 0
    for i in range(n):

        sum += (m * float(data[i][0]) + c - float(data[i][1])) ** 2
    return sum / n

optimal_values = MVC.hybrid_backtracking_newton_gradient(
    x=Vector(1, 1),
    function=cost_function,
    tolerance=10**-5,
    verbose=True,
    max_iterations=2000,
    beta = 0.3,
    alpha = 0.01
)

m, c = Vector.unpack_vector(optimal_values)
print(m,c)

def line_of_best_fit(x):
    return m * x + c


import matplotlib.pyplot as plt
import numpy as np

x  = [test_data[i][0] for i in range(TEST_NUM)]
y = [test_data[i][1] for i in range(TEST_NUM)]

space = np.linspace(0, 100, 10000)
plt.scatter(x,y)
plt.plot(space, line_of_best_fit(space))
plt.show()
