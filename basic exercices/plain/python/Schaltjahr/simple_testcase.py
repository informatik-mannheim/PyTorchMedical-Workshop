from template import *
from head import test_singleton as test

a = 1000
b = 1004
c = 1200
d = 1990

test.expect(isLeap(a) is False, "Error on {}".format(a))

test.expect(isLeap(b), "Error on {}".format(b))

test.expect(isLeap(c), "Error on {}".format(c))

test.expect(isLeap(d) is False, "Error on {}".format(d))

print("{}/{} tests failed".format(test.failedTests, test.totalTests))
