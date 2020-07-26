import numpy as np


def call():

    height = [1.56, 1.78, 1.9, 1.62, 1.7]
    weight = [89, 90, 100, 61, 50]

    np_height = np.array(height)
    np_weight = np.array(weight)

    return ((np_height*100/np_weight).round(2))

print (call())
