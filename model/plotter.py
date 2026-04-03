import matplotlib.pyplot as plt
import numpy as np
from regression import linear_regression
from typing import Tuple

def plot_dataset(x: np.array, y: np.array, **kwargs)->None:
    """plot the dataset given by vectory x, y

    Args:
        x (np.array): dependent variable
        y (np.array): indenpendent variable
    """
    assert len(x) == len(y), "x and y length must be equal"
    plt.scatter(x, y, label=kwargs.get("label") or "dataset")

def plot_regression_line(x: np.array, theta0: float, theta1: float, **kwargs)->None:
    """plot the regression line having parameter theta0 and theta1

    Args:
        x (np.array): dependent variable
        theta0 (float): slope of the line
        theta1 (float): y-intercept
    """
    yhat = theta0 + theta1 * x
    plt.plot(x, yhat, label=kwargs.get("label") or f"{theta0:.3f} + x * {theta1:.3f}")

def plot(x: np.array, y: np.array, theta: Tuple | None, **kwargs)->None:
    plot_dataset(x, y)
    if theta is not None:
        for t in theta:
            if len(t) == 2:
                plot_regression_line(x, t[0], t[1])
    plt.grid(True)
    plt.legend()
    plt.xlabel(kwargs.get("xlabel") or "x")
    plt.ylabel(kwargs.get("ylabel") or "y")
    plt.show()

if __name__ == "__main__":
    import sys
    import pandas as pd

    assert len(sys.argv) == 3, "data path must be given as an argument"

    df = pd.read_csv(sys.argv[1], sep='\t')
    xarr = np.array(df.x)
    yarr = np.array(df.y)
    (theta0, theta1, rest) = linear_regression(xarr, yarr, 0.0005)

    plot(xarr, yarr, ((theta0, theta1), ))
