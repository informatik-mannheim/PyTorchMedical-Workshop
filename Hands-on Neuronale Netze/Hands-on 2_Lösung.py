import numpy as np

input1 = np.array([3, 5, 7])
input2 = np.array([4, 8, 2])
input3 = np.array([9, 1, 6])

weights = np.array([1, 1, 1])
#weights = np.array([0, 1, 1]) #Mit diesen Gewichten spricht das Neuron nur bei Input 1 an.
#weights = np.array([1, 1, 0]) #Mit diesen Gewichten spricht das Neuron nur bei Input 2 an.
#weights = np.array([1, 0, 1]) #Mit diesen Gewichten spricht das Neuron nur bei Input 3 an.

def activate(inputs):
    netsum = 0.0
    for i in range(inputs.size):
        netsum+=weights[i]*inputs[i]
    return (netsum > 10).astype(int)

print(activate(input1))
print(activate(input2))
print(activate(input3))