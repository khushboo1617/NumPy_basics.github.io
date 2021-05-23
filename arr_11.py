print("SEARCHING ARRAYS...")
import  numpy as np
ar = np.array([11,23,34,45,56,67,89,90,67,87,65])
y = np.where(ar==45)
print(y)
x= np.where(ar%2==0)
print("divisible by 2  :",x)
z = np.searchsorted(ar,65)
print("searchsorted  :", z)
s = np.searchsorted(ar,89,side='right')
print(s)

print("FIND THE INDICES FOR INSERTING THE VALUES: ")
arr = np.array([1,3,5,7,9,11])
q = np.searchsorted(arr,[2,4,6,8,10])
print(q)
print(arr)


