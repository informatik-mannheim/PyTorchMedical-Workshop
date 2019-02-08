import solution
import template
from random import randint
from head import test_singleton as test


for i in range(100):
    random_test_value = randint(0, 9999)
    sol = solution.isLeap(random_test_value)
    attempt = template.isLeap(random_test_value)
    test.expect(sol == attempt, "isLeap({}) = {} should've been {}"
                .format(random_test_value, attempt, sol))

print("{}/{} tests failed".format(test.failedTests, test.totalTests))
