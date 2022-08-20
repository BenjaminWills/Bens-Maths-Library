import sys
sys.path.append('/Users/benwills/Desktop/personal_projects/Mathematics_fundamentals')

import numpy as np
import matplotlib.pyplot as plt
from linear_algebra.linear_algebra import Linalg

plt.style.use("dark_background")


class Visualisation:
    def make_axis(self):
        fig, ax = plt.subplots()
        return ax

    def matplotlib_config(self, ax, set_y_lim=False, y_lim1=0, y_lim2=0):
        ax.set_aspect("equal")
        ax.grid(True, which="both", linestyle=":")
        ax.spines["left"].set_position("zero")
        ax.spines["right"].set_color("none")
        ax.yaxis.tick_left()
        ax.spines["bottom"].set_position("zero")
        ax.spines["top"].set_color("none")
        ax.xaxis.tick_bottom()
        if set_y_lim:
            ax.set_ylim(y_lim1, y_lim2)

    def get_function_visualisation(self, function, start, end, steps, ax):
        if start >= end:
            return None
        plotting_space = np.linspace(start, end, steps)
        ax.plot(plotting_space, function(plotting_space))
        self.matplotlib_config(ax)

    def get_conic_visualisation(self, function, start, end, steps, ax):
        # Conic sections are one to many functions. So we need to plot them differently.
        plotting_space = np.linspace(start, end, steps)
        ax.plot(plotting_space, function(plotting_space)[0])
        ax.plot(plotting_space, function(plotting_space)[1])
        self.matplotlib_config(ax)

    def visualise_function_linear_transform(
        self, function, start, end, steps, ax, transformation_matrix
    ):
        space = np.linspace(start, end, steps)
        lin = Linalg()
        points = lin.transform_function(space, function, transformation_matrix)
        self.matplotlib_config(ax, set_y_lim=True, y_lim1=-2, y_lim2=10)
        ax.scatter(points[0], points[1], marker=".", s=0.2)

    def visualise_conic_linear_transform(self,function, start, end, steps, ax, transformation_matrix):
        space = np.linspace(start, end, steps)
        lin = Linalg()
        pos_points = lin.transform_conic_function(space,function,transformation_matrix)[0]
        neg_points = lin.transform_conic_function(space,function,transformation_matrix)[1]
        self.matplotlib_config(ax)
        ax.scatter(pos_points[0], pos_points[1], marker=".", s=0.2)
        ax.scatter(neg_points[0], neg_points[1], marker=".", s=0.2)

    def show_visualisation(self):
        plt.show()
