import numpy as np
from random import randint
from head import check, test_singleton as test
import solution
import template

for i in range(100):
    value = randint(0, 10000)
    shape = (randint(0, 5), randint(0, 5))
    array = np.ones(shape)

    check(template.addition(array, value),
          solution.addition(array, value), "addition")

    check(template.substraction(array, value),
          solution.substraction(array, value), "substraction")

    check(template.multiplication(array, value),
          solution.multiplication(array, value), "multiplication")

    check(template.division(array, value),
          solution.division(array, value), "division")

    array2 = np.ones(shape)*3
    check(template.add_array_to_array(array, array2),
          solution.add_array_to_array(array, array2), "addition of arrays")

print("{}/{} tests failed".format(test.failedTests, test.totalTests))
