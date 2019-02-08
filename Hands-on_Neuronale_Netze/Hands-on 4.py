import numpy as np

class MyNet:
    def __init__(self):
        hiddenLayerWeights = np.array([[1,0,1,0],[0,1,0,1],[0,0,1,1]])
        outputLayerWeights = np.array([[1,0,1],[0,1,0]])        
        self.hiddenLayer = Layer(hiddenLayerWeights)
        self.outputLayer = Layer(outputLayerWeights)        
       
    #Hier muss die Klassifikation einer Eingabe für das gesamte Netz vorgenommen werden
    #Wie in der vorigen Ausgabe soll auch hier die Klasse des Ausgabe-Neurons ausgegeben werden, welches
    #für die jeweilige Eingabe den größten Wert liefert (1 für Neuron 1, 2 für Neuron 2)    
    def classify(self, inputs):
       return 0
    
class Layer:
    #Die Größe eines Gewichts-Arrays bestimmt, wie viele Inputs anliegen (da jeder Input ein Gewicht hat)
    #Die Anzahl an Gewichts-Arrays bestimmt, wie viele Outputs ausgegeben werden (Jedes Neuron der Schicht hat eigene Gewichte)
    #Über die Gewichts-Arrays wird somit die Anzahl an Inputs und Outputs dynamisch bestimmt
    #(Nur zum Verständnis; An dieser Stelle muss nichts weiter angepasst werden.)
    def __init__(self, weights):
        self.weights = weights              
    
    #Diese Funktion soll die Ausgabe einer Schicht für einen Input liefern
    #Die Ausgabe muss erneut ein numpy-array sein, da sie in anderen Schichten ggf. als Eingabe verwendet wird.    
    def getResultForInput(self,inputs):        
        return 0
    
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



