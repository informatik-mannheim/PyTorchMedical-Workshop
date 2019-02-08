import numpy as np
from template import *
from head import check, test_singleton as test

arr6x6 = np.arange(36).reshape(6, 6)

split = split_6x6_into_4_quadrants(arr6x6)

quadrant_0 = np.array([[0, 1, 2], [6, 7, 8], [12, 13, 14]])
solutionSplit = (quadrant_0, quadrant_0 + 3, quadrant_0 + 18, quadrant_0 + 21)

for i in range(4):
    check(i, split, solutionSplit)

print("{}/{} tests failed".format(test.failedTests, test.totalTests))
