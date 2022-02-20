from math import sqrt
from random import random
import numpy as np


n_iter=100
n_points=1000
 

class Point():
    """
    A point in a 2D (xy) space
    properties:
        x: float, x-coordinate
        y: float, y-coordinate
    """
    x=0.0
    y=0.0

    def __init__(self, xy=None):
        """
        Constructor
        If xy is not provided, randomly generate xy coordiantes.
        Otherwise, xy can be assigned by a tuple (e.g., (2, 3))
        """
        x_random=random()*2
        y_random=random()*2
        # properties
        self.x = None
        self.y = None

        # assign values to x and y
        if xy is None:
            self.x=x_random
            self.y=y_random
        else:
            (self.x,self.y)=xy

    def __repr__(self):
        """
        Allow the xy-coordinates to be printed when the point is called
        """
        return "Point: %.2f, %.2f" % (self.x, self.y)

    def distance(self, point):
        """
        input: a Point() object
        output: Euclidean distance between self point and the input point
        """
        return sqrt((self.x-point.x)*(self.x-point.x)+(self.y-point.y)*(self.y-point.y))
        
        

def estimate_pi(n_points=n_points):
    """
    input: number of points to be generated
    output: estimated pi through the simulation
    """
    n_red=0
    n_black=0
    for i in range(n_points):
        point=Point()
        distance=point.distance(center)
        if distance<=1:
            n_red+=1
        if distance>1:
            n_black+=1
    pi=4*n_red/(n_red+n_black)
    return pi


# estimate pi for 100 iterations

center=Point(xy=(1,1))
pi = np.zeros(n_iter)
pis=0
for i in range(n_iter):
    pi[i]=estimate_pi(n_points)


print(f"estimated_pi : {np.average(pi)}")

