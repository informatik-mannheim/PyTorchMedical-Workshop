import numpy as np
from random import randint


def check(user_array, solution_array, operation):
    test.expect(np.array_equal(user_array, solution_array),
                "{usr}\n does not match\n{sol}\nfor {op}".format(usr=user_array, sol=solution_array, op=operation))


for i in range(100):
    value = randint(0, 10000)
    shape = (randint(0, 5), randint(0, 5))
    array = np.ones(shape)
    check(addition(array, value), array+value, "addition")
    check(substraction(array, value), array-value, "substraction")
    check(multiplication(array, value), array*value, "multiplication")
    check(division(array, value), array/value, "division")
    array2 = np.ones(shape)*3
    check(add_array_to_array(array, array2),
          array+array2, "addition of arrays")
