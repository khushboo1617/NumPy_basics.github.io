print("NUMPY JOINING ARRAYS:")
import numpy as np
#USE OF CONCATENATE FUNCTION FOR 1-D ARRAYS:
print("USING CONCATENATE() FUNCTION:")
ar1 = np.array([10,23,45,67,89,10,34])
ar2 = np.array([23,45,67,80,14,36,56])
ar = np.concatenate((ar1,ar2))
print(ar)

#FOR 2-D ARRAYS:
arr1 = np.array([[1,23,3,12,4,5],[23,5,67,8,9,34]])
arr2 = np.array([[12,45,78,89,56,23],[20,30,50,40,16,89]])
arr = np.concatenate((arr2,arr1), axis=1)
print(arr)

print("USING STACK FUNCTION:")
ara = np.stack((ar1,ar2), axis=1)
arra = np.hstack((ar1,ar2)) #stacking along rows
arra1=np.vstack((ar1,ar2)) #stacking along columns
arra2 = np.dstack((ar1,ar2)) #stackng along depth
print(ara)
print("stacking along rows: ")
print(arra)
print("stacking along columns: ")
print(arra1)
print("stackng along depth: ")
print(arra2)

