import numpy as np


def calculate(listed):
    if len(listed) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        arr = np.array(listed).reshape(3, 3)

        outp = {
            'mean': [],
            'variance': [],
            'standard deviation': [],
            'max': [],
            'min': [],
            'sum': []
        }

        outp['mean'].append(list(arr.mean(axis=0)))
        outp['mean'].append(list(arr.mean(axis=1)))
        outp['mean'].append(arr.flatten().mean())

