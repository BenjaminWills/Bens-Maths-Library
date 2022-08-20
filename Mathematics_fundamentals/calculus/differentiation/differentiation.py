import sys
sys.path.append('/Users/benwills/Desktop/personal_projects/Mathematics_fundamentals')

class Differentiation:
    def get_derivative(self,function,x):
        dx = 10 ** -5
        vert_change = function(x+dx) - function(x)
        slope = vert_change/dx
        return slope
    
    def get_turning_points(selfmfunction,start,end,method = ''):
        if method == '':
            # NEWTON RAPHSON
            pass

