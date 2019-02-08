def sum_from_zero_to(x):
    sum = 0
    for i in range(1, x + 1):
        sum += i
    return sum


def sum_of_collection(collection):
    sum = 0
    for element in collection:
        sum += element
    return sum


def argmin(collection):
    if len(collection) > 0:
        x = collection[0]
        minIndex = 0
        for i in range(len(collection)):
            if collection[i] < x:
                x = collection[i]
                minIndex = i
        return minIndex
    else:
        return None
