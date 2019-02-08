import solution
import template
import random
from head import test_singleton as test, check


def sum_by_gauss(x):
    return (x*x + x)/2


for i in range(100):
    random_list = random.sample(range(1, 101), random.randint(1, 10))

    check(template.sum_of_collection(random_list),
          sum(random_list), "sum_of_collection")
    random_value = random.randint(0, 9999)
    check(template.sum_from_zero_to(random_value),
          sum_by_gauss(random_value), "sum_from_zero_to")
    check(template.argmin(random_list),
          random_list.index(min(random_list)), "argmin")

print("{}/{} tests failed".format(test.failedTests, test.totalTests))
