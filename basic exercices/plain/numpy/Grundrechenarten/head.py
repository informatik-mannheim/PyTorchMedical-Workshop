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


def check(user_arr, sol_list, function_name):
    sol_arr = np.array(sol_list)
    test_singleton.expect(np.array_equal(user_arr, sol_arr),
                          "Error at {fct}\nuser result:\n{usr}\nsolution:\n{sol}\n"
                          .format(usr=user_arr, sol=sol_arr, fct=function_name))
##########################################################################
