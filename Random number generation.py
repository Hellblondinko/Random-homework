import timeit
import matplotlib.pyplot as plt


numbers = range(1, 100)
REPEAT = 100

rand_rand = [min(timeit.Timer('random.uniform(0, 1)', setup='import random').repeat(repeat=REPEAT, number=i)) for i in numbers]
rand_np = [min(timeit.Timer('random.uniform(0, 1)', setup='from numpy import random').repeat(repeat=REPEAT, number=j)) for j in numbers]


plt.plot(numbers, rand_np, 'g', label='numpy', linewidth=2)
plt.plot(numbers, rand_rand, 'r', label='random', linewidth=2)
plt.ylabel('Performance in sec')
plt.xlabel('Numbers generated')
plt.legend()
plt.show()
