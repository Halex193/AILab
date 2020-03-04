# https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.random.html
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

from numpy.random import normal
from numpy.random import uniform
if __name__ == '__main__':
    print("Distribution type:")
    print("1.normal")
    print("2.uniform")
    distribution = input()
    if distribution == "1":
        mu = float(input("mu="))
        variance = float(input("variance="))
        sigma = math.sqrt(variance)

        x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)

        generated = normal(mu, sigma, 10000)

        plt.subplot(2, 1, 1)
        plt.hist(generated, 50)
        plt.subplot(2, 1, 2)
        plt.plot(x, stats.norm.pdf(x, mu, sigma))
        plt.show()
    elif distribution == "2":
        a = float(input("a="))
        b = float(input("b="))

        x = np.linspace(a, b, 100)

        generated = uniform(a, b, 100000)

        plt.subplot(2, 1, 1)
        plt.hist(generated, 50)
        plt.subplot(2, 1, 2)
        plt.plot(x, stats.uniform.pdf(x, a, b))
        plt.show()
    else:
        print("Invalid choice")
