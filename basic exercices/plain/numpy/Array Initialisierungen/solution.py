import numpy as np


def init_array_from_range_and_put_it_into_shape(range_limit, shape):
    return np.arange(range_limit).reshape(shape)


def init_array_with_given_value(value, shape):
    return np.full(shape, value)


def init_array_with_ones(shape):
    return np.ones(shape)


def init_array_with_zeros(shape):
    return np.zeros(shape)
