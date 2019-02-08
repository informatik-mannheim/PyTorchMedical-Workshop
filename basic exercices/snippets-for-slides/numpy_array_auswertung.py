import numpy as np

my_arr = np.arange(6).reshape((2, 3))  # =>

np.argmax(my_arr)          # = 5 <=> Index von max für eindimensionales Array
# = [1,1,1] <=> Index von max entlang axis=0 (Spalten)
np.argmax(my_arr, axis=0)
np.argmax(my_arr, axis=1)  # = [2,2] <=> Index von max entlang axis=1 (Reihen)

my_arr.max()            # 5
my_arr.max(axis=0)      # [3, 4, 5]
my_arr.min()            # 0
my_arr.mean()           # 2,5 <=> Mittelwert
