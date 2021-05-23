#iterating arrays:
import numpy as np
#1-D arrays:
ar = np.array([12,34,56,78,90])
print(ar)
for x in ar:
    print(x)

#for 2-D arrays:
arr = np.array([[10,13,24,57,69],[32,54,76,98,100]])
print(arr)
print('2-D ARRAYS: ')
for a in arr:
    for b in a:
        print(b)

#for 3-D arrays:
arrr = np.array([[[1,2,3,4,5],[2,4,6,7,8]],[[12,34,2,6,89],[12,4,56,78,90]]])
print("3-D ARRAYS: ")
for c in arrr:
    for d in c:
        for e in d:
            print(e)


# using nditer function:
print("NDITER FUNCTION:  ")
for s in np.nditer(arr):
    print(s)

#iterating arrays with different data types:
print("we wiill use one buffer:")
ara = np.array([12,34,21,67,8,90])
for q in np.nditer(ara, flags=['buffered'],op_dtypes=['S']):
    print(q)

#iterating arrays with different step size:
print("differen step size:", end="")
arra = np.array([[2,3,4,5,6],[7,8,9,10,11]])
for a in np.nditer(arra[:,::2]) :
    print(a)


#enumerated iteration using ndenumerate()
print("Elements with indices")
araray = np.array([12,13,15,78,45,23,98,76])
for idx, x in np.ndenumerate(araray):
    print(idx,x)
