import numpy as np


def split_6x6_into_4_quadrants(arr):
    return [arr[:3, :3], arr[:3, 3:], arr[3:, :3], arr[3:, 3:]]
