import numpy as np
import matplotlib.pyplot as plt


dims = 2
step_n = 1000
step_set = [-1, 0, 1]
origin = np.zeros((1, dims))
step_shape = (step_n, dims)
steps = np.random.choice(a=step_set, size=step_shape)
path = np.concatenate([origin, steps]).cumsum(0)

plt.scatter(path[:, 0], path[:, 1], c='r', marker='o')
plt.show()
