import matplotlib.pyplot as plt
import numpy as np


def main():
    x1 = np.arange(0, 2 * (np.pi), 0.1)
    y1 = np.sin(x1)

    x2 = np.arange(0, 2 * (np.pi), 0.1)
    y2 = np.cos(x2)

    plt.plot(x1, y1)
    plt.show()

    plt.plot(x2, y2)
    plt.show()


if __name__ == '__main__':
    main()
