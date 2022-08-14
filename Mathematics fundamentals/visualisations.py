import numpy as np
import matplotlib.pyplot as plt


class Visualisation:
    def make_axis(self):
        fig, ax = plt.subplots()
        return ax 

    def matplotlib_config(self,ax,start,end):
        ax.set_aspect("equal")
        ax.grid(True, which="both", linestyle=":")
        ax.spines["left"].set_position("zero")
        ax.spines["right"].set_color("none")
        ax.yaxis.tick_left()
        ax.spines["bottom"].set_position("zero")
        ax.spines["top"].set_color("none")
        ax.xaxis.tick_bottom()
        ax.set_xlim(left = start - 1, right = end + 1, auto = True)

    def get_function_visualisation(self, function, start, end, steps,ax):
        if start >= end:
            return None
        plotting_space = np.linspace(start, end, steps)
        ax.plot(plotting_space, function(plotting_space))
        self.matplotlib_config(ax,start,end)

    def get_conic_visualisation(self,function,start,end,steps,ax):
        # Conic sections are one to many functions. So we need to plot them differently.
        plotting_space = np.linspace(start, end, steps)
        ax.plot(plotting_space, function(plotting_space)[0])
        ax.plot(plotting_space, function(plotting_space)[1])
        self.matplotlib_config(ax,start,end)

    def show_visualisation(self):
        plt.show()