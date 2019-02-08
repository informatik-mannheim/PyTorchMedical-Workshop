import numpy as np

#Vervollständigen Sie die Funktion, sodass für einen gegebenen Input ein max pooling
#der gegebenen Größe durchgeführt wird.
#
#Hinweis: Sie müssen nicht auch noch eine Fehlerbehndlung für ungültige Eingaben umsetzen.
#         Das Ziel der Übung ist, dass die vorhandenen Eingaben korrekt gepoolt werden.
def maxPool(inpt, filterSize):    
    size = int(inpt.shape[0]/filterSize)    
    result = np.zeros((size,size))
    
    for x in range(size):
        for y in range(size):            
            inptWindow = inpt[x*filterSize:x*filterSize+filterSize, y*filterSize:y*filterSize+filterSize]           
            result[x,y]=inptWindow.max()
    
    return result

inpt = np.array([[0,1,5,8,6,2,7,0,1,0],
                 [9,4,6,5,0,1,0,9,0,6],
                 [7,8,6,4,3,0,8,0,1,9],
                 [4,6,9,1,0,3,2,8,4,0],
                 [4,5,6,9,3,1,7,0,3,1],
                 [9,5,0,1,6,4,0,9,0,7],
                 [1,2,5,3,4,7,9,0,5,0],
                 [0,2,0,3,0,5,7,9,1,3],
                 [6,4,0,3,8,7,0,1,9,2],
                 [4,6,2,3,9,1,0,3,0,8]])
    
filter2Result = maxPool(inpt,2)
filter5Result = maxPool(inpt,5)

targetFilter2 = np.array([[9,8,6,9,6],
                          [8,9,3,8,9],
                          [9,9,6,9,7],
                          [2,5,7,9,5],
                          [6,3,9,3,9]])
targetFilter5 = np.array([[9,9],
                          [9,9]])

print("Entspricht das Ergebnis dem erwarteten Ergebnis? : "+str((filter2Result==targetFilter2).all()))
print("Entspricht das Ergebnis dem erwarteten Ergebnis? : "+str((filter5Result==targetFilter5).all()))
