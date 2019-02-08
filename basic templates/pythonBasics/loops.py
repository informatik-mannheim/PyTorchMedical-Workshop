def whileLoop():
    i = 0
    while i < 3:
        print(i)
        i = i+1


whileLoop()


def forLoop_OverElements(elements):
    for element in elements:
        print(element)


x = ["a", "b", "c"]
forLoop_OverElements(x)


def forLoop_usingLength(elements):
    for i in range(len(elements)):
        print("elements[{0}] = {1}".format(i, elements[i]))


forLoop_usingLength(x)


def forLoop_overElements_WithoutUsingThem(elements):
    """ Coding conventions use _ as a throwaway variable
        other uses of _:
                - store the value of last executed expression
                - reference internationalization library
                - see https://stackoverflow.com/a/5893946/10761360
    """
    for _ in range(len(elements)):
        # don't use _ at all, e.g. if you wanted to print something x times:
        print("iteration")


forLoop_overElements_WithoutUsingThem(x)
