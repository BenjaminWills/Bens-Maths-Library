import sys
sys.path.append('/Users/benwills/Desktop/personal_projects/Mathematics_fundamentals')

class Differentiation:
    def get_derivative(self,function,x):
        dx = 10 ** -5
        vert_change = function(x+dx) - function(x)
        slope = vert_change/dx
        return slope
    
    def newton_raphson_method(self,function,start,end,initial_point):
        x0 = initial_point
        max_iterations = 100000
        iteration_count = 0
        while abs(self.get_derivative(function,x0)) > 10 ** -5:
            if iteration_count == max_iterations:
                return 'DIVERGENT'
            slope = self.get_derivative(function,x0)
            func_value = function(x0)
            x0 = x0 - (func_value/slope)
            iteration_count += 1
        return x0


