print("NUMPY SPILITING ARRAY: ")
import  numpy as np
ar1 = np.array([10,20,30,40,50,60,70,80,90])
ar = np.array_split(ar1,3)
print(ar)
arr = np.array_split(ar1,5)
print(arr)

print("FOR 2-D ARRAYS:  ")
arr1 = np.array([[11,22,33],[44,55,77],[88,99,55],[22,66,33]])
arr2 = np.array([[12,13],[14,15],[16,33],[21,23],[24,25],[33,26]])
arrr = np.array_split(arr1,2)
aarr = np.array_split(arr2,4)
print("FOR 1ST ARRAY ")
print(arrr)
print("FOR 2ND ARRAY  ")
print(aarr)
print("HSPLIT() FUNCTIONS....")
newar1= np.hsplit(arr1,3)
print(newar1)
newar2 = np.hsplit(arr2,2)
print(newar2)
print("VSPLIT() FUNCTION.....")
newarr1 = np.vsplit(arr1,2)
print(newarr1)
#araa = np.dsplit(arr1,2)  dsplit only works with three dimensions or more.
#print(araa)