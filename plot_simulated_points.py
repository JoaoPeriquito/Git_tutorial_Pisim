import matplotlib.pyplot as plt

def main(x_inside, y_inside, x_outside, y_outside):

    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.scatter(x_inside, y_inside, color='g', marker='s')
    ax.scatter(x_outside, y_outside, color='r', marker='s')
    fig.show()
    plt.show()