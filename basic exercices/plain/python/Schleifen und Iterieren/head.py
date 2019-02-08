import numpy as np

################################# HEADER #################################
print("======================================")


class test_proxy:

    def __init__(self):
        self.failedTests = 0
        self.totalTests = 0

    def expect(self, shouldBeTrue, message):
        self.totalTests += 1
        if shouldBeTrue is False:
            print(message)
            self.failedTests += 1


test_singleton = test_proxy()


def check(user_value, solution_value, function_name):
    test_singleton.expect(user_value == solution_value,
                          "{} does not match {} for function {}"
                          .format(user_value, solution_value, function_name))
##########################################################################
