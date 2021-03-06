import numpy as np
from random import randint


def solution_init_array_from_range_and_put_it_into_shape(range_limit, shape):
    return np.arange(range_limit).reshape(shape)


def solution_init_array_with_given_value(value, shape):
    return np.full(shape, value)


def solution_init_array_with_ones(shape):
    return np.ones(shape)


def solution_init_array_with_zeros(shape):
    return np.zeros(shape)


def check(user_arr, sol_list, function_name):
    sol_arr = np.array(sol_list)
    test.expect(np.array_equal(user_arr, sol_arr),
                "Error at {fct}\nuser result:\n{usr}\nsolution:\n{sol}\n"
                .format(usr=user_arr, sol=sol_arr, fct=function_name))


def check_init_from_range(range, shape):
    user_arr = init_array_from_range_and_put_it_into_shape(range, shape)
    sol_arr = solution_init_array_from_range_and_put_it_into_shape(
        range, shape)
    check(user_arr, sol_arr, "init_array_from_range_and_put_it_into_shape")


def check_init_with_value(value, shape):
    user_arr = init_array_with_given_value(value, shape)
    sol_arr = solution_init_array_with_given_value(value, shape)
    check(user_arr, sol_arr, "init_array_with_given_value")


def check_init_ones(shape):
    user_arr = init_array_with_ones(shape)
    sol_arr = solution_init_array_with_ones(shape)
    check(user_arr, sol_arr, "init_array_with_ones")


def check_init_zeros(shape):
    user_arr = init_array_with_zeros(shape)
    sol_arr = solution_init_array_with_zeros(shape)
    check(user_arr, sol_arr, "init_array_with_zeros")


for i in range(100):
    shape = (randint(1, 10), randint(1, 10))
    range_limit = shape[0] * shape[1]
    check_init_from_range(range_limit, shape)
    check_init_with_value(range_limit, shape)
    check_init_ones(shape)
    check_init_zeros(shape)
