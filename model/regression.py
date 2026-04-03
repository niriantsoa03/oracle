import numpy as np
from typing import Tuple

def linear_regression(x: np.array, y: np.array, alpha: float = 0.1,
                      max_iter: int = 10000, eps: float = 1e-5)->Tuple:
    """apply linear regression to (x, y) dataset and compute parameter theta0 and theta1
        of the model with learning rate alpha using gradient descent algorithm

    Args:
        x (np.array): independent variable
        y (np.array): dependent variable
        alpha (float, optional): learning rate. Defaults to 0.1.
        max_iter(float, optional): maximum number of iteration. Default to 100000.
        eps(float, optional): minimum value triggering convergence

    Returns:
        (theta0, theta1, i): theta0(y intercept) and theta1(slope) that best fit the dataset
                            i is the number of iteration at which the algorithm stopped
    """

    assert len(x) == len(y), "x and y must have the same length"
    
    n = len(x)
    ## initial theta0 and theta1
    (theta0, theta1) = (0, 0)
    for i in range(max_iter):
        ## yhat
        yhat = theta0 + x * theta1
        ## error
        err = y - yhat ## elementwise substraction
        ## gradient definition
        grad_theta0 = (- 1 / n) * np.sum(err)
        grad_theta1 = (- 1 / n) * np.sum(err * x)

        ## alpha is equal to alpha' / 2, which is practically the same
        theta0 = theta0 - alpha * grad_theta0
        theta1 = theta1 - alpha * grad_theta1

        ## check for convergence
        if abs(grad_theta0) < eps and abs(grad_theta1) < eps:
            break
    return (float(theta0), float(theta1), i)

if __name__ == "__main__":
    import sys
    import pandas as pd

    assert len(sys.argv) != 3, "data path must be given as an argument"

    df = pd.read_csv(sys.argv[1], sep='\t')
    xarr = np.array(df.x)
    yarr = np.array(df.y)
    print(linear_regression(xarr, yarr, 0.00051))
