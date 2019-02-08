import numpy as np
from head import check, test_singleton as test
import solution
import template

for i in range(100):
    arr6x6 = np.random.rand(36).reshape(6, 6)

    split = template.split_6x6_into_4_quadrants(arr6x6)
    solutionSplit = solution.split_6x6_into_4_quadrants(arr6x6)

    for i in range(4):
        check(i, split, solutionSplit)

print("{}/{} tests failed".format(test.failedTests, test.totalTests))
