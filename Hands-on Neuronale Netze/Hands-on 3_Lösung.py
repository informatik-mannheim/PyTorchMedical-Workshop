import numpy as np

class MyNet:
    def __init__(self):
        self.neuron1Weights = np.array([0.1, 0.2, 0.3, 0.0, 0.5])
        self.neuron2Weights = np.array([0.2, 0.0, 0.1, 0.3, 0.1])
        self.neuron3Weights = np.array([0.5, 0.1, 0.7, 0.2, 0.3])
        self.neuron1 = Neuron(self.neuron1Weights)        
        self.neuron2 = Neuron(self.neuron2Weights)
        self.neuron3 = Neuron(self.neuron3Weights)
        
    def classify(self, inputs):
        results = np.array([self.neuron1.activate(inputs),self.neuron2.activate(inputs),self.neuron3.activate(inputs)])        
        return np.argmax(results, axis=0)+1
    
class Neuron:    
    def __init__(self, weights):
        self.weights = weights    
     
    def ReLu(self,val):
        return max(0, val)
    
    def activate(self,inputs):
        netsum = 0.0
        for i in range(inputs.size):
            netsum+=self.weights[i]*inputs[i]        
        return self.ReLu(netsum)
    

net = MyNet()
myInput = np.array([1,0,1,0,1])
myClass2Input = np.array([0,0,0,1,0])
print(net.classify(myInput))
print(net.classify(myClass2Input))
