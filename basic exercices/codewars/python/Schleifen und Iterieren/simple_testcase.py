test.expect(sum_from_zero_to(5) == 15, "Wrong from zero to 5")
y = [1, 2, 3, 4, 5]

test.expect(sum_of_collection(y) == 15,
            "Wrong sum over collection {}".format(y))

test.expect(argmin([5, 4, 3, 2, 1, 0, 0]) == 5, "Wrong index returned")
