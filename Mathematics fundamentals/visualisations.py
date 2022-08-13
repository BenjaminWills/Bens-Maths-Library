import numpy as np
import matplotlib.pyplot as plt

class Visualisation:
    def get_function_visualisation(self, function, start, end, steps):
        if start >= end:
            return None
        plotting_space = np.linspace(start, end, steps)
        fig, ax = plt.subplots()
        ax.plot(plotting_space, function(plotting_space))
        ax.set_aspect('auto')
        ax.grid(True, which='both',linestyle=':')
        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.yaxis.tick_left()
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')
        ax.xaxis.tick_bottom()
        plt.show()