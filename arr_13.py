print("FILTERING ARRAYS:  ")
#filterng an array using a boolean index list.
import numpy as np
a = np.array([12,44,56,45,78,66])
x = [True,True,True,False,True,False]
print(a[x])

print("CREATING FILTER ARRAYS: ")
ar = np.array([12,34,56,13,23,78,90,10])
#print the numbers those are greatr than 13:
ar_filter = []
for elements in ar :
    if elements>13 :
        print(ar_filter.append(True))
    else:
        print(ar_filter.append(False))

newAr = ar[ar_filter]
print("filtered array :", ar_filter)
print(newAr)

#2nd method:
arr = np.array([22,44,66,88,11,33,55,99,23,45,67,89])
filter_arr = arr>44
newarr = arr[filter_arr]
print("new array: ", newarr)
