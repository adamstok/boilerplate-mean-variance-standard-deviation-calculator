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

        outp['variance'].append(list(arr.var(axis=0)))
        outp['variance'].append(list(arr.var(axis=1)))
        outp['variance'].append(arr.flatten().var())

        outp['standard deviation'].append(list(arr.std(axis=0)))
        outp['standard deviation'].append(list(arr.std(axis=1)))
        outp['standard deviation'].append(arr.flatten().std())

