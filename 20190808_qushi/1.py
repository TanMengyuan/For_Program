import numpy as np

def gradient_descent(X, y, lr=0.01, threshold=1e-3):
    params = np.array([0., 0., 0.])
    #

    #
    theta1, theta2 = 0, 0
    b = 0
    for i in range(10000):
        x1, x2= X[i, 0], X[i, 1]
        theta1 = theta1 - lr * theta1
        theta2 = theta2 - lr * theta2
        b = b - lr * b
        y_ = theta1 * x1 + theta2 * x2 + b
        if y[i] - y_ < threshold:
            return np.array([theta1, theta2, b])


    return params


#
# Please don't modify any code below.
#
if __name__ == "__main__":
    # Code to generate the data/test case
    n_samples = 10000
    x_1, x_2 = np.random.random(n_samples), np.random.random(n_samples)
    # theta_1, theta_2, b = map(float, input().split())
    theta_1, theta_2, b = 20.1, 123.4, 20
    #print (theta_1, theta_2, b)
    X, y = np.vstack([x_1, x_2]).T, theta_1 * x_1 + theta_2 * x_2 + b
    # Solution
    params = gradient_descent(X, y)
    result = []
    for param in params:
        result.append('{:.02f}'.format(param))
    print(' '.join(result))