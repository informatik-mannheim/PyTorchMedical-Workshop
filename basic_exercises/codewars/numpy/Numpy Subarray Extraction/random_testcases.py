import numpy as np

for i in range(100):
    print("Run {}".format(i+1))
    arr6x6 = np.random.rand(36).reshape(6, 6)

    split = split_6x6_into_4_quadrants(arr6x6)

    def solution(arr):
        return [arr[0:3, 0:3], arr[0:3, 3:6], arr[3:6, 0:3], arr[3:6, 3:6]]
    solutionSplit = solution(arr6x6)

    def check(quadrantIndex):
        boolean_to_compare = np.array_equal(
            solutionSplit[quadrantIndex], split[quadrantIndex])
        test.expect(boolean_to_compare is True,
                    "Your array\n{user_solution}\n at quadrant {position} did not match the solution\n{solution}".format(position=quadrantIndex, solution=solutionSplit[quadrantIndex], user_solution=split[quadrantIndex]))

    for i in range(4):
        check(i)
