# import numpy as np
# or we can import like
from numpy import *
arr = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
print(arr*2)

# --------------------------------------------------
#array()
arr1 = array([12,14,18,20.68])
print(arr1.dtype)   # dtype- show the datatype of an array

# --------------------------------------------------
# linspace()
arr2 = linspace(10,20)
print(arr2) # if add only 2 params then it print 50 values by default. which is float value always

arr3 = linspace(0, 15, 20)
print(arr3) # it gives 20 values between 0 to 15

arr4 = linspace(1, 15, 15)
print(arr4)

# --------------------------------------------------
# arange()
arr5 = arange( 1,10, 2)
print(arr5)     # it skip 2 step the values between 1 to 10

# --------------------------------------------------
# logspace()
arr6 = logspace(1, 10, 5)
print(arr6)     # the values show depend on the log of these 2 numbers (1 - 40)
print('%2f'%arr6[2])

# --------------------------------------------------
# zeros()
arr7 = zeros(10)
print(arr7)     # it gives only 0 with float datatype. (next params will declare the datatype)

# --------------------------------------------------
# ones()
arr8 = ones(10, int)
print(arr8)     # it gives one 1 , 10 times