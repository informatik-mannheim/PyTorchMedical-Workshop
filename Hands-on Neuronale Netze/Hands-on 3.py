import numpy as np

class MyNet:
    def __init__(self):
        self.neuron1Weights = np.array([0.1, 0.2, 0.3, 0.0, 0.5])
        self.neuron2Weights = np.array([0.2, 0.0, 0.1, 0.3, 0.1])
        self.neuron3Weights = np.array([0.5, 0.1, 0.7, 0.2, 0.3])
        self.neuron1 = Neuron(self.neuron1Weights)        
        self.neuron2 = Neuron(self.neuron2Weights)
        self.neuron3 = Neuron(self.neuron3Weights)
    
    #Hier soll die Klasse als Ergebnis ausgegeben werden, deren Neuron für diese Eingabe
    #den größten Wert als Ergebnis geliefert hat. (1 für Neuron1, 2 für Neuron2, ...)
    def classify(self, inputs):
        return 1
    
class Neuron:    
    def __init__(self, weights):
        self.weights = weights    
    
    def ReLu(self,val):
        return max(0, val)
    
    #Die Aktivierungsfunktion soll hier nun so angepasst werden, dass
    #anstelle der Schwellenwert-Funktion nun die ReLu-Funktion verwendet wird.
    def activate(self,inputs):
        return 0
    

net = MyNet()
myInput = np.array([1,0,1,0,1])
print(net.classify(myInput))

