import numpy as np


def split_6x6_into_4_quadrants(arr):
    return [arr[0:3, 0:3], arr[0:3, 3:6], arr[3:6, 0:3], arr[3:6, 3:6]]
