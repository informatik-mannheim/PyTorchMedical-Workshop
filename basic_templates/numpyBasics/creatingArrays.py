import numpy as np
################################################
seperatorTemplate = "##### {} #####"


def section(input=""):
    print()
    if(input == ""):
        print("#"*20)
    else:
        print(seperatorTemplate.format(input))
################################################


section("manual init")
manualInitS = "np.array([[1, 1], [2, 2]])"
print("manualInit = "+manualInitS+"\n" + str(eval(manualInitS)))
print("note that the array contains int values")

section("Init with fixed values")
shape = (2, 2)
# np.empty(shape)
# np.zeros(shape)
# np.ones(shape)
# np.full(shape, value)
oneS = "np.ones({})".format(shape)
one = eval(oneS)
print("one = {}\n".format(oneS) + str(one))
print("note that the value type defaults to " + str(one.dtype))

section("Init with range")
# inclusive first, exclusive second
range3dS = "np.arange(1, 10)"
range3d = eval(range3dS)
print("range3d = {}\n".format(range3dS) + str(range3d))
print()
oneToNine3x3S = "range3d.reshape(3, 3)"
oneToNine3x3 = eval(oneToNine3x3S)
print("oneToNine3x3 = {}\n".format(oneToNine3x3S) + str(oneToNine3x3))


section("accesing array attributes")
one = np.ones((2, 2))
print("one[0] = " + str(one[0]))
print("one[0][0] = " + str(one[0][0]))
print("one.size = " + str(one.size))
print("one.shape = " + str(one.shape))
print("one.shape[0] = " + str(one.shape[0]))
