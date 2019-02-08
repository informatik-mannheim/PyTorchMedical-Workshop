import numpy as np

arr6x6 = np.arange(36).reshape(6, 6)

split = split_6x6_into_4_quadrants(arr6x6)

arr1 = np.array([[0, 1, 2], [6, 7, 8], [12, 13, 14]])
solutionSplit = (arr1, arr1 + 3, arr1 + 18, arr1 + 21)


def check(quadrantIndex):
    boolean_to_compare = np.array_equal(
        solutionSplit[quadrantIndex], split[quadrantIndex])
    test.expect(boolean_to_compare is True,
                "Your array\n{user_solution}\n at quadrant {position} did not match the solution\n{solution}".format(position=quadrantIndex, solution=solutionSplit[quadrantIndex], user_solution=split[quadrantIndex]))


for i in range(4):
    check(i)
