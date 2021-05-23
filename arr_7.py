import numpy as np

#reshaping arrays:
#reshape from 1-D to 2-D

ar = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
newar = ar.reshape(3,5)
print(newar)

#reshape from 1-D to 3-D
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
newarr = arr.reshape(2,3,3)
print(newarr)
print(newarr.base)


a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x = a.reshape(3,2,-1)
print(x)

#flattering the arrays means converting array into 1-D array:
ara = np.array([[[1,2,3],[2,3,4]],[[2,3,4],[3,5,6]]])
newara = ara.reshape(-1)
print(newara)
print(newara.sort())