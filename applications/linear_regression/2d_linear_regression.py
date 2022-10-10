"""
Linear regression beginning with 2-d
"""
TRAIN_NUM = 700
TEST_NUM = 250
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from Mathematics_fundamentals.linear_algebra.linear_algebra import Vector
from Mathematics_fundamentals.multivariable_calculus.mvc import MVC

training_data = pd.read_csv('/Users/benwills/Desktop/personal_projects/applications/train.csv')
testing_data = pd.read_csv('/Users/benwills/Desktop/personal_projects/applications/test.csv')

training_data_dict = training_data.to_dict()
training_data_list = [[training_data_dict['x'][i],training_data_dict['y'][i]] for i in range(TRAIN_NUM)]

def cost_function(vector: Vector, data: list = training_data_list[:TRAIN_NUM]) -> float:
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
    alpha = 0.15
)

m, c = Vector.unpack_vector(optimal_values)
print(m,c)

def line_of_best_fit(x):
    return m * x + c

space = np.linspace(0, 100, 10000)

plt.scatter(testing_data.iloc[:, 0], testing_data.iloc[:, -1])
plt.plot(space,line_of_best_fit(space), color = 'red')
plt.show()