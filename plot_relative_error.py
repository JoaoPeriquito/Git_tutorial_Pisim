import matplotlib.pyplot as plt
import numpy as np

def main (pi,n):
    pi = np.array(pi)
    pi_ref = np.repeat(np.pi,n)

    pi_error = np.abs((pi_ref - pi)/pi_ref *100)
    iterations = np.arange(n)

    plt.plot(iterations,pi_error)
    plt.show()