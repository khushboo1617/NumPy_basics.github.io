print("RANDOM NUMBERS:  ")
from numpy import random
x = random.randint(100, size=(10))
print(x)

y = random.rand(5)
print("value of y: ", y )

print("generate a2-D array:::;")
z = random.randint(1000 , size = (4,5))
print(z)

c = random.choice([2,4,6,8,1,5,7,9], size=(6,4))
print(" choice() method  ", c)
