import numpy as np
import matplotlib.pyplot as plt
from linear_algebra import Linalg


class Visualisation:
    def make_axis(self):
        fig, ax = plt.subplots()
        return ax

    def matplotlib_config(self, ax, start, end):
        ax.set_aspect("equal")
        ax.grid(True, which="both", linestyle=":")
        ax.spines["left"].set_position("zero")
        ax.spines["right"].set_color("none")
        ax.yaxis.tick_left()
        ax.spines["bottom"].set_position("zero")
        ax.spines["top"].set_color("none")
        ax.xaxis.tick_bottom()

    def get_function_visualisation(self, function, start, end, steps, ax):
        if start >= end:
            return None
        plotting_space = np.linspace(start, end, steps)
        ax.plot(plotting_space, function(plotting_space))
        self.matplotlib_config(ax, start, end)

    def get_conic_visualisation(self, function, start, end, steps, ax):
        # Conic sections are one to many functions. So we need to plot them differently.
        plotting_space = np.linspace(start, end, steps)
        ax.plot(plotting_space, function(plotting_space)[0])
        ax.plot(plotting_space, function(plotting_space)[1])
        self.matplotlib_config(ax, start, end)

    def visualise_linear_transform(
        self, function, start, end, steps, ax, transformation_matrix
    ):
        space = np.linspace(start, end, steps)
        lin = Linalg()
        points = lin.transform_function(space, function, transformation_matrix)
        self.matplotlib_config(ax, start, end)
        ax.scatter(points[0], points[1], marker=".", s=0.2)

    def show_visualisation(self):
        plt.show()
