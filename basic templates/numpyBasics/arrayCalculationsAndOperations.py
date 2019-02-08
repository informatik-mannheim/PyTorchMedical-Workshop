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


section("Simple calculations that are applied to every element in the array")
one = np.ones((2, 2))

four = 4 * one
print("4 * one\n" + str(four))

print()
three = four - one
print("four - one\n" + str(three))

section()
oneToNine3x3 = np.arange(1, 10).reshape(3, 3)
#                                   Sum of rows
#                 [[1   2   3]           6
#                  [4   5   6]          15
#                  [7   8   9]]         24
#
# Sum of columns   12  15  18

# is 9
print("Max of all values: " + str(oneToNine3x3.max()))

# is 45
print("Sum of all values: " + str(oneToNine3x3.sum()))

sumsPerColumn = oneToNine3x3.sum(axis=0)
print("Sums per column: " + str(sumsPerColumn))

sumsPerRow = oneToNine3x3.sum(axis=1)
print("Sums per row: " + str(sumsPerRow))


section("get the index of the max element in an (multi-dimensional) array")
index = np.argmax(oneToNine3x3)
# index = 8: The 3-dimensional array is flattened
print("Max of flattened array is at index: " + str(index))

section("Argmax with axis")
oneToFour2x2 = np.arange(1, 5).reshape(2, 2)
fiveToEight2x2 = np.arange(5, 9).reshape(2, 2)

maxIndexPerArrayByVerticalAxis = np.argmax(
    [oneToFour2x2, fiveToEight2x2], axis=0)  # index
print(maxIndexPerArrayByVerticalAxis)


threeDimensional = np.array([oneToFour2x2, fiveToEight2x2])
# index of max along the 2nd (index=1) dimension
# note: the input is a
# axis-1 applies argmax to each array "oneToFour" and "fiveToEight"
# and combines the results accordingly
maxIndexPerArrayByHorizontalAxis = np.argmax(
    threeDimensional, axis=1)
print("Max is at index: " +
      str(maxIndexPerArrayByHorizontalAxis))

# axis=0
section("Axis for visualizations")
print(threeDimensional.shape)
for one in range(threeDimensional.shape[0]):
    print("a[{}]".format(one))
    for two in range(threeDimensional[one].shape[0]):
        print("     a[{0}][{1}]".format(one, two))
        for three in range(threeDimensional[one][two].shape[0]):
            print("         a[{0}][{1}][{2}] = ".format(one, two, three) +
                  str(threeDimensional[one][two][three]))
print()
print(np.argmax(threeDimensional, axis=0))

section("Argmax axis 2d")
d2 = np.array([[1, 2], [3, 1], [0, 4]])
print("D2: " + str(d2))
print()
print("d2.shape\n" + str(d2.shape))
print("Argmax axis 0\n" + str(np.argmax(d2, axis=0)))  # a[*][x]
print("Argmax axis 1\n"+str(np.argmax(d2, axis=1)))  # a[a][*]

section("Argmax axis 3d")
d3 = np.array([d2, d2])
print(d3)
print()
print(d3.shape)
# a[*][a][b] max aller a[0][0][0], a[1][0][0], ... a[a.shape[0]-1][0][0]
print(np.argmax(d3, axis=0))
# a[a][*][b] <=> a,b Konstant, * wird eingesetzt und verglichen
print(np.argmax(d3, axis=1))
# a[a][b][*]
print(np.argmax(d3, axis=2))

section("Extract subarrays into 4 3x3 arrays")

arr6x6 = np.arange(0, 36).reshape(6, 6)
print(arr6x6)

# note that arr6x6[y:y, x:x], as y is the "first" dimension and x the "second", i.e. a[y][x]
topLeft = arr6x6[0:3, 0:3]
print(topLeft)
topRight = arr6x6[0:3, 3:6]
print(topRight)
botLeft = arr6x6[3:6, 0:3]
print(botLeft)
botRight = arr6x6[3:6, 3:6]
print(botRight)


section("Extract subarrays more generically")


def getSubArraysDinamically(array, length):
    subArrays = []
    for y in range(0, int(array.shape[0]/length)):
        for x in range(0, int(array.shape[1]/length)):
            lowerY = y * length
            upperY = (y + 1) * length
            lowerX = x * length
            upperX = (x + 1) * length
            temp = array[lowerY:upperY, lowerX:upperX]
            subArrays.append(temp)
    return subArrays


subArrayLength = 3
subArrays = getSubArraysDinamically(arr6x6, subArrayLength)
for subArray in subArrays:
    print(subArray)

# weitere array funktionen?
