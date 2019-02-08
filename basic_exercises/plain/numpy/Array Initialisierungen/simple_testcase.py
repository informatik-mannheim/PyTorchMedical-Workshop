import numpy as np
from template import *
from head import test_singleton as test, check

test_shape = (2, 2)

user_arr = init_array_from_range_and_put_it_into_shape(4, test_shape)
sol_arr = [[0, 1], [2, 3]]
check(user_arr, sol_arr,
      "init_array_from_range_and_put_it_into_shape")

user_arr = init_array_with_given_value(5.5, test_shape)
sol_arr = [[5.5, 5.5], [5.5, 5.5]]
check(user_arr, sol_arr, "init_array_with_given_value")

user_arr = init_array_with_ones(test_shape)
sol_arr = [[1, 1], [1, 1]]
check(user_arr, sol_arr, "init_array_with_ones")

user_arr = init_array_with_zeros(test_shape)
sol_arr = [[0, 0], [0, 0]]
check(user_arr, sol_arr, "init_array_with_zeros")

print("{}/{} tests failed".format(test.failedTests, test.totalTests))
