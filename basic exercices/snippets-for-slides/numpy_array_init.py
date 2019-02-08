import numpy as np

shape = (2, 2)
np.zeros(shape)         # => [[0,0],[0,0]]

value = 5
np.full(shape, value)   # => [[5,5],[5,5]]

np.array([[5, 5], [5, 5]])  # Python-Liste zu Array

np.arange(4).reshape(shape)  # [0,1,2,3] wird zu [[0,1],[2,3]]

# ..._like  ist auch für die anderen Initialisierungsfunktionen verfügbar
np.full_like(array, value)  # => array's shape, data_type ... werden benutzt


##################
np.ones(shape)          # => [[1,1],[1,1]]
np.empty(shape)         # => [[?,?],[?,?]]
