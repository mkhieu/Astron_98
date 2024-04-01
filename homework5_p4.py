import numpy as np

def sorting(a):
    sorted = np.sort(a, axis=0)
    return sorted

a = np.random.randint(1, 50, (4,5))
print(a)
print(sorting(a))