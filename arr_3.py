# slicing arrays

import numpy as n
# this is for 1-D array.
ar = n.array([11,21,33,42,52,62,71,85,99,10])
print(ar[1:6])   #[start:end]
print(ar[0:9:2]) #[start:end:step]
print(ar[2:], ar[:6])
#negative slicing
print(ar[-4:-1])
print(ar[::4])

#this is for 2-D array.
arr = n.array([[12,34,56,33,21],[78,98,67,54,87]])
print(arr[0,1:4])
print(arr[1,0:5])
print(arr[0:3,4])
print(arr[0:3 , 3:4])


