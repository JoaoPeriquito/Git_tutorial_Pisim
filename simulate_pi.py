import random
import numpy as np

def main(n):

    inside = 0

    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []
    pi = []

    for i in range(n):
        
        x = random.uniform(-1.0,1.0)
        y = random.uniform(-1.0,1.0)
        if x**2+y**2 <= 1:
            inside += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)
        pi.append (4*inside/(i+1))

    #pi = 4*inside/n
    return pi, x_inside, y_inside, x_outside, y_outside