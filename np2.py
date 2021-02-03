import numpy as np

#1. get the value of the one dimensional array
print("1.")
a=np.arange(0,6)   
print(a)                #[0 1 2 3 4 5]       
print(a[0])             #0
print(a[5])             #5
print(a[1:5])           #[0 1 2 3 4]
print(a[1:5:2])         #[1 3]
print(a[:])             #[0 1 2 3 4 5]
print(a[:3])            #[0 1 2]
print(a[3:])            #[3 4 5]

#2. get the value of the N dimensional array
print("2.")
