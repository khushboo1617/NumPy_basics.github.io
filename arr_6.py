#get the shape of an array using an attribute called 'shape'.

import numpy as n
ar = n.array([[[1,2,3,4,5],[5,4,6,3,1]],[[2,4,6,7,8],[3,5,1,7,4]]])
print(ar.shape)
arr = n.array([[1,2,3,4,5,6,78],[2,4,6,1,7,8,4]])
print(arr.shape)

arrr = n.array([2,3,41,34,76,4,6,90], ndmin=5)
print(arrr.shape)
print(arrr)
