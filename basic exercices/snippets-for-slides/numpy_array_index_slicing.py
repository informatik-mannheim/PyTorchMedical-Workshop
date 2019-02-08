import numpy as np

# 4x4 Array mit Werten 0-15
"""
 [[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]
  [12 13 14 15]]
"""
arr4x4 = np.arange(16).reshape((4, 4))

"""
 [[0 1]
  [4 5]]
"""
# Bereich in Zeile [0;2) und Spalte [0;2)
topLeft = arr4x4[0:2, 0:2]

"""
 [[2 3]
  [6 7]]
"""
# Bereich in Zeile [0;2) und Spalte [2;4)
topRight = arr4x4[0:2, 2:4]
