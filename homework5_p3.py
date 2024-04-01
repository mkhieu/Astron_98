import numpy as np

def spaceBetween(myrray):
    strings = []  
    for string in myrray:
        characters = list(string)
        strings.append(' '.join(characters))
    return np.array(strings)

print(spaceBetween(np.array(['python', 'is', 'fun'])))