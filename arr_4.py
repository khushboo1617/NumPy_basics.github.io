#checking the data type of an array.
import numpy as np

ar = np.array(['app','grap','guav','bana'])
print(ar.dtype)
arr = np.array([1,2,3,4])
print(arr.dtype)

#converting data type on existing arrays

ara = np.array([12.34,23.45,0,2.34,1.43,45.6])
newAra = ara.astype('i')
newaara = ara.astype(int)
newwra = ara.astype(bool)
print(newAra)
print(newaara)
print(newwra)