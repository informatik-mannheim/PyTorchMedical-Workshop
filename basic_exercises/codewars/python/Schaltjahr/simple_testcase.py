a = 1000
b = 1004
c = 1200
d = 1990


def check(is_leap, year):
    test.expect(is_leap, "{} wrongfully evaluated to {}".format(year, is_leap))


check(isLeap(a) is False, a)
check(isLeap(b), b)
check(isLeap(c), c)
check(isLeap(d) is False, d)
