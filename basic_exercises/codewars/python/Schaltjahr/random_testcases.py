from random import randint


def sol_isLeap(year):
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))


for i in range(100):
    random_test_value = randint(0, 99999)
    sol = sol_isLeap(random_test_value)
    attempt = isLeap(random_test_value)
    test.expect(sol == attempt,
                "{} has not been evaluated correctly and returned {}"
                .format(random_test_value, attempt))
