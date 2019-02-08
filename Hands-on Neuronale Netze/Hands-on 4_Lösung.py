import numpy as np

class MyNet:
    def __init__(self):
        hiddenLayerWeights = np.array([[1,0,1,0],[0,1,0,1],[0,0,1,1]])
        outputLayerWeights = np.array([[1,0,1],[0,1,0]])        
        self.hiddenLayer = Layer(hiddenLayerWeights)
        self.outputLayer = Layer(outputLayerWeights)        
       
        
    def classify(self, inputs):
        results = self.outputLayer.getResultForInput(self.hiddenLayer.getResultForInput(inputs))     
        return np.argmax(results, axis=0)+1
    
class Layer:
    #Die Größe eines Gewichts-Arrays bestimmt, wie viele Inputs anliegen (da jeder Input ein Gewicht hat)
    #Die Anzahl an Gewichts-Arrays bestimmt, wie viele Outputs ausgegeben werden (Jedes Neuron der Schicht hat eigene Gewichte)
    #Über die Gewichts-Arrays kann somit die Anzahl an Inputs und Outputs dynamisch bestimmt werden
    #(Nur zum Verständnis; An dieser Stelle muss nichts weiter angepasst werden.)
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

def testMe():
    net = MyNet()
    res1 = net.classify(np.array([0,0,0,0]))
    res2 = net.classify(np.array([0,1,0,1]))
    res3 = net.classify(np.array([1,0,1,0]))
    res4 = net.classify(np.array([1,1,1,1]))   
    if res1==1 and res2==2 and res3==1 and res4==1:
        print("This net seems ok")
    else:
        print("There is something wrong with this net")
    
testMe()



