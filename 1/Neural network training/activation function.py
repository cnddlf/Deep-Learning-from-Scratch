# 1. step function

import numpy as np
# x = np.array([-1.0, 1.0, 2.0])
# print(x)
# y = x > 0
# y = y.astype(int)
# print(y)

#  2. graph of step function
import matplotlib.pylab as plt

# def step_function(x):
#     return np.array(x > 0, dtype = int)

# x = np.arange(-5.0, 5.0, 0.1)
# y = step_function(x)
# plt.plot(x, y)
# plt.ylim(-0.1, 1.1)
# plt.show()

# 3. sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
t = np.array([1.0, 2.0, 3.0])
print(1.0 + t)
print(1.0 / t)

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()