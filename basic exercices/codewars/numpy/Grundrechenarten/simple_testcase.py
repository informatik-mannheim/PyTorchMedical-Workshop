import numpy as np


def check(user_arr, sol_list, function_name):
    sol_arr = np.array(sol_list)
    test.expect(np.array_equal(user_arr, sol_arr),
                "Error at {fct}\nuser result:\n{usr}\nsolution:\n{sol}\n"
                .format(usr=user_arr, sol=sol_arr, fct=function_name))


value = 1
array = np.array([[1, 1], [1, 1]])
check(addition(array, value), [[2, 2], [2, 2]], "addition")
check(substraction(array, value), [[0, 0], [0, 0]], "substraction")

# division and multiplication by 1 is boring
value2 = 2
check(multiplication(array, value2), [[2, 2], [2, 2]], "multiplication")
check(division(array, value2), [[0.5, 0.5], [0.5, 0.5]], "division")

array2 = np.array([[2, 2], [2, 2]])
check(add_array_to_array(array, array2), [
      [3, 3], [3, 3]], "addition of arrays")
