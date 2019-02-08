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
##########################################################################
