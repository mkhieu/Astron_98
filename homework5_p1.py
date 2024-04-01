import numpy as np

def findEqual(array):
    equal_rows = []
    for row in array:
        if np.all(row == row[0]):
            equal_rows.append(row)
    return np.array(equal_rows)

a = np.array([[1, 1, 1], [2, 2, 2], [4, 3, 4]])
print(findEqual(a))
