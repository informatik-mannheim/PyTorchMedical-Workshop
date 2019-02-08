import numpy as np

def conv(inpt, convMask):
    #Die Größe der Ausgabe wird um 2x2 Pixel kleiner, da die Faltungsmaske auf die
    #äußerste Reihen nicht angewendet werden kann.
    #(Die Maske würde sonst in mind. einer Seite über die Matrix "hinausragen")
    #Das Bild "schrumpft" von 10x10 auf 8x8 Pixel.
    result = np.zeros((8,8))
    
    for x in range(result.shape[0]):
        for y in range(result.shape[1]):
            currentInptWindow = np.zeros((3,3))            
            currentInptWindow[0] = inpt[x,(y):(y+3)]
            currentInptWindow[1] = inpt[x+1,(y):(y+3)]
            currentInptWindow[2] = inpt[x+2,(y):(y+3)]            
            result[x,y] = (currentInptWindow*convMask).sum() / convMask.sum()
    
    return result
    
convMask = np.array([[1,2,1],[2,4,2],[1,2,1]])
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
result = conv(inpt, convMask)
target = np.array([[5.125,  5.3125, 4.75,   2.75,   2.0,    3.25,   3.3125, 2.6875],
                   [6.625,  5.875,  3.8125, 1.875,  2.0,    3.5625, 3.625,  3.3125],
                   [6.1875, 6.25,   4.125,  2.125,  2.4375, 3.8125, 3.9375, 3.125 ],
                   [5.25,   5.1875, 4.5625, 3.3125, 2.875,  3.625,  3.75,   2.875 ],
                   [4.25,   3.3125, 3.625,  4.25,   4.1875, 4.125,  3.75,   3.0625],
                   [2.6875, 2.5625, 2.75,   3.8125, 5.3125, 5.6875, 4.5,    3.125 ],
                   [2.0,    2.0,    2.5625, 3.75,   5.1875, 5.5625, 4.8125, 3.6875],
                   [3.125,  2.0,    3.1875, 5.125,  4.5,    3.0,    3.375,  4.1875]])
print("Entspricht das Ergebnis dem erwarteten Ergebnis? : "+str((result==target).all()))
