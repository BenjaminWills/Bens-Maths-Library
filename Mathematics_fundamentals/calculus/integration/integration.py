import sys
sys.path.append('/Users/benwills/Desktop/personal_projects/Mathematics_fundamentals')

from functions.functions import Functions
import numpy as np
from visualisations.visualisations import Visualisation

class Integration:
    def trapezium_approximation(self,function,start,end,steps):
        width = (start-end)/steps
        area = .5*(function(start)+function(end))
        for i in range(1,steps-1):
            area += function(start + i*width)
        return area*width

    def get_midpoint(self,p1,p2):
        return (p1+p2)/2

    def get_individual_area(self,function,p1,p2):
        midpoint = self.get_midpoint(p1,p2)
        funcval_at_start = function(p1)
        funcval_at_mid = function(midpoint)
        funcval_at_end = function(p2)
        return funcval_at_start + 4*funcval_at_mid + funcval_at_end

    def simpson_approximation(self,function,start,end,steps):
        area = 0
        width = (end-start)/steps
        for i in range(steps):
            local_start = start + i * width
            local_end = start + (i+1) * width
            area += self.get_individual_area(function,local_start,local_end)
        return width/6 * area




vis = Visualisation()
int = Integration()
fun = Functions()

def line(x):
    return fun.bell_curve(x)


# plotting the integral of the bell curve.

def primitive(x):
    return int.simpson_approximation(line,0,x,1000)

ax = vis.make_axis()
vis.get_function_visualisation(primitive,-10,10,1000,ax)
vis.show_visualisation()