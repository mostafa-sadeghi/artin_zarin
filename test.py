import matplotlib.pyplot as plt
import numpy as np

xs = np.linspace(0, 9, 10)
ys = np.sin(xs)
with plt.style.context("seaborn"):
    plt.plot(xs, ys, label="ssss")
    plt.show()
input()
