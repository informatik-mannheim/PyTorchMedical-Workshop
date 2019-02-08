import numpy as np

class MyNet:
    def __init__(self):
        self.hiddenLayerWeights = np.array([[1.0,1.0],[1.0,1.0]])
        self.outputLayerWeights = np.array([[1.0,1.0]])        
        self.hiddenLayer = Layer(self.hiddenLayerWeights)
        self.outputLayer = Layer(self.outputLayerWeights)      
        
    def classify(self, inputs):
        results = self.outputLayer.getResultForInput(self.hiddenLayer.getResultForInput(inputs))     
        return np.argmax(results, axis=0)+1
    
    def printWeights(self):
        print("#################Gewichte#################")
        print("Gewichte der Hidden layer:")
        print(self.hiddenLayerWeights)
        print("Gewichte der Output layer:")
        print(self.outputLayerWeights)
    
    def train(self, data, solution):
        learningRate = 0.01
        iterations = 100
        derivateReLU = 1
        
        for i in range(iterations):
            for j in range(data.shape[0]):
                hiddenLayerResult = self.hiddenLayer.getResultForInput(data[j])                
                outputLayerResult = self.outputLayer.getResultForInput(hiddenLayerResult)                             
                
                outputLayerError = outputLayerResult - solution[j]
                hiddenLayerError = derivateReLU * self.outputLayerWeights * outputLayerError               
                
                deltaOutputLayer = outputLayerError * hiddenLayerResult
                deltaHiddenLayer = hiddenLayerError * data[j] 
                
                self.outputLayerWeights -= learningRate * deltaOutputLayer
                self.hiddenLayerWeights -= learningRate * deltaHiddenLayer  
                
                print("Differenz zu Zielwert: "+str(outputLayerResult))  
                
        self.printWeights()
             
    
class Layer:    
    def __init__(self, weights):
        self.weights = weights              
        
    def getResultForInput(self,inputs):
        result = np.array([])
        for i in range(self.weights.shape[0]):            
            neuron = Neuron(self.weights[i])
            result = np.append(result, neuron.activate(inputs))
        return result
    
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
    
  
  
#Als Eingabedaten dienen uns 1er
#Der Zielwert soll in diesem Fall stets 0 sein.
#Das Netzt scheint korrekt zu lernen, wenn die Gewichte nach dem Training 0.15596091 sind
#Die ausgegebene Differenz zum Zielwert sollte langsam kleiner werden
Data = np.ones((10,1))
Targets = np.zeros(10)

net = MyNet()
net.train(Data,Targets)
