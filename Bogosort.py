import timeit
import matplotlib.pyplot as plt
from random import shuffle
from numpy import random
import pandas as pd

numbers = range(1, 10)
list_data = [random.randint(0, 999, j) for j in numbers]

def is_sorted(data):
     return all(data[i] <= data[i + 1] for i in range(len(data) - 1))


def bogosort(data):
     while not is_sorted(data):
         shuffle(data)
     return data


df = pd.DataFrame(columns=['mean', 'std'])

for l in list_data:
     ser = pd.Series(timeit.Timer('bogosort(l)', globals=globals()).repeat(repeat=10, number=1)).agg(['mean', 'std'])
     df = df.append(ser, ignore_index=True)

plt.errorbar(numbers, df['mean'], yerr=df['std'], label='bogosort', fmt='-o')
plt.ylabel('Performance in sec')
plt.xlabel('List size')
plt.legend()
plt.show()