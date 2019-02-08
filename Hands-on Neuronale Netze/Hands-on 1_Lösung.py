import numpy as np

input1 = np.array([0.1, 0.2, 0.3])
input2 = np.array([0.4, 0.5, 0.6])
input3 = np.array([0.7, 0.8, 0.9])

def activate(inputs):
    netsum = 0.0
    for i in range(inputs.size):
        netsum+=inputs[i]
    return (netsum > 2).astype(int)

print(activate(input1))
print(activate(input2))
print(activate(input3))