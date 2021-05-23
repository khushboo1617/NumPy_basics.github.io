#finding elements using array index for 1-D array.

import numpy as np

arr = np.array([1,2,3,4,5,6])
print(arr[0])
print(arr[0],arr[3])

# in same way we can access elements from 2-D array.

ara = np.array([[1,2,3],[4,5,6]])
print(ara[0,1],ara[1,2])

#we can even add them.

print(ara[0,2]+ara[0,0]+ara[1,1])

#let's do for 3-D array

arra = np.array([[[1,2,3],[5,6,7]],[[7,8,9],[8,9,10]]])
print('value of 0,0,1 is : ',arra[0,0,1])
print('value of 1,1,2 is :', arra[1,1,2])

#using negative indexing to access an element from array.
print(ara[1,-2])
print(ara[0,-2])

