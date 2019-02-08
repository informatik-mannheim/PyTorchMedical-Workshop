import numpy as np

input1 = np.array([3, 5, 7])
input2 = np.array([4, 8, 2])
input3 = np.array([9, 1, 6])

#Hier sollen nun die Gewichte definiert werden.
#In diesem vereinfachten Beispiel verwenden wir Ganzzahlen als Gewichte.
#Setzen Sie die Gewichte initial alle auf 1. Welche Ausgabe liefert die Aktivierungsfunktion für die Inputs?
#Passen Sie nun die Gewichte nacheinander so an, dass das Neuron jeweils nur für einen der drei Inputs anspricht.
weights = 

#Erweitern Sie die Aktivierungsfunktion um die Verwendung der Gewichte
def activate(inputs):
    netsum = 0.0
    for i in range(inputs.size):
        netsum+=inputs[i]
    return (netsum > 10).astype(int)

print(activate(input1))
print(activate(input2))
print(activate(input3))