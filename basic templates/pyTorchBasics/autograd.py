import torch

seperatorTemplate = "##### {} #####"


def sep(input=""):
    print()
    if(input == ""):
        print("#"*20)
    else:
        print(seperatorTemplate.format(input))


sep("Using autograd (automatic differentiation)")
# the default value for requires_grad is False
ones2x2 = torch.ones(2, 2, requires_grad=True)
print(ones2x2)
# as no operation (other than the creation/init) has been executed on ones2x2 the result will be None
print(ones2x2.grad_fn)

three2x2 = ones2x2 + 2
print(three2x2)
# three2x2 is the result of an operation (and ones2x2 has grad enabled)
# the following object describes the operation applied to the new vector
print(three2x2.grad_fn)

nine2x2 = three2x2 * three2x2
print(nine2x2)

t27_2x2 = nine2x2 * 3
print(t27_2x2)
# as multiple operations have been applied to the original, the object will contain a "MulBackward" reference (multiple backward references)
print(t27_2x2.grad_fn)

# mean/average over all values of the vector
tensorWithMeanValue = t27_2x2.mean()
print(tensorWithMeanValue)

# start backpropagation
print(tensorWithMeanValue.backward())
print(ones2x2.grad)


sep("Grad/Autograd can also be enabled on existing tensors, however operations will only be tracked after grad has been enabled")
size = (2, 2)
twos = torch.full(size, 2)
# Note that the tensor "twos" does not hold a grad_fn at this point
print(twos)
print(twos.grad_fn)
# an operations performed before grad is enabled
fours = twos * 2
fours.requires_grad_(True)
print("tracking is enabled now")
print("grad_fn is still", fours.grad_fn,
      "because no operation has been tracked yet")
back22 = fours / 2
# a division is tracked with the tensor
print(back22)
print(back22.grad_fn)
