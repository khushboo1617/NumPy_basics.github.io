import numpy as np

#difference between copy and view.
#copy:
ar = np.array([12,34,56,78,90])
c = ar.copy()
ar[1]=24
c[4]=14
print(ar)
print(c)
print(c.base)

#view:
arr = np.array([13,24,35,46,57,68,79])
x=arr.view()
arr[2]=21
print(arr)
print(x)
print(x.base)