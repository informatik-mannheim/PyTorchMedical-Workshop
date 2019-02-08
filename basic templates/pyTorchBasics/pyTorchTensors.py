import torch

seperatorTemplate = "##### {} #####"


def sep(input=""):
    print()
    if(input == ""):
        print("#"*20)
    else:
        print(seperatorTemplate.format(input))


sep("tensor from list")
tensorFromList = torch.tensor([1, 2, 3])
print(tensorFromList)

sep("tensor initialization utils include torch.zeros, torch.ones, torch.empty and torch.full")
height = 1
width = 3
dataType = torch.double
zeroTensor = torch.zeros(height, width, dtype=dataType)
print(zeroTensor)
# default dtype
sep("tensor from default type")
oneTensor = torch.ones(height, width)
print("tensor with 1 values:\n" + str(oneTensor))
print("Default tensor type: " + str(oneTensor.dtype))
sep("creating tensor of same size with different values can be done using the helpers X_like(tensorWithSizeToUse, ...args), where X can be 'ones', 'zeros', 'full'... ")
print("our zero tensor has size", zeroTensor.size())

sep("Casting tensor types")
# casting tensor types
zeroInt = torch.zeros(1, 3, dtype=torch.int)
zeroDouble = zeroInt.type(torch.double)
print(zeroInt)
print(zeroDouble)
zeroInt + torch.tensor([1, 2, 3], dtype=torch.int)
print(zeroInt)

# tensor
#   view
#   other tensor operations

# cuda?
#   gibt's?
#   was kann man machen?
#       verteilen
#       parallelisieren
