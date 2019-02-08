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


def check(quadrantIndex, split, solutionSplit):
    if(split is None and solutionSplit is not None):
        test_singleton.expect(False, "Your function returned None")
    else:
        boolean_to_compare = np.array_equal(
            solutionSplit[quadrantIndex], split[quadrantIndex])
        test_singleton.expect(boolean_to_compare is True,
                              "Your array\n{user_solution}\n at quadrant\
                               {position} did not match the solution\n´\
                                   {solution}"
                              .format(
                                  position=quadrantIndex,
                                  solution=solutionSplit[quadrantIndex],
                                  user_solution=split[quadrantIndex]))
##########################################################################
