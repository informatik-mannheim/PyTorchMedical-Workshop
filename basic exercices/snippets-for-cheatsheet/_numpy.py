import numpy as np

### Werte initialisieren ###
shape = (2, 2)
np.full(shape, 5)   # 2x2 Array: überall 5
np.zeros(shape)     # 2x2 Array: überall 0 <=> np.ones

### Array aus Liste ###
python_liste = [[5, 5], [5, 5]]
np.array(python_liste)  # Python-Liste zu Array

### Array aus range ###
zero_to_eight = np.arange(9)  # [0,..., 8]
arr3x3 = zero_to_eight.reshape((3, 3))

### Operationen auf Arrays ###
arr3x3.max()    # maximaler Wert
arr3x3.min()    # min. Wert
arr3x3.mean()   # Mittelwert
arr3x3.sum()    # Summe allert Werte
arr3x3.shape    # (3, 3) Form/Dimensionen

np.argmax(arr3x3)          # IndexMax in "flachem" Array
np.argmax(arr3x3, axis=0)  # "argmax pro Spalte"


### Operatorüberladung ###
# + - * / und weitere
two2x2 = np.ones((2, 2)) * 2    # Alle Werte mal 2

four2x2 = two2x2 + two2x2       # Array addition
