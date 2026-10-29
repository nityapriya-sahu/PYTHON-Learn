from numpy import *

arr1 = array([1,2,3,4,5])

res = arr1+5
print(res)

arr2 =  array([6,7,8,9,10])
print(arr1+arr2)

print(min(arr2))
print(max(arr2))
print(sqrt(arr2))
print(concatenate([arr1,arr2]))

# --------------------------------------------------

arr3 = array([6,8,2,1,3])

arr4 = arr3.view()

arr3[1] = 9     # here we can see the changes if we change the value in arr3 both the array is changed the values(arr3 &4) . [This is called shallow copy]

# so to change only arr3 value we need to add the function .copy(), which will change the value only in arr3. arr3.copy() [This is called deep copy]

print(arr3)
print(arr4)
# Different array but address is the same location.
print(id(arr3))
print(id(arr4))     # So to change the address different need to add .view() function in array

# --------------------------------------------------
# ASSIGNMENT

# Write a code to add 2 array using for loop

givenarr1 = [1,2,3,4,5]
givenarr2 = [6,7,8,9,10]
resultarr=[]
for i in range(len(givenarr1)):
    resultarr.append(givenarr1[i]+givenarr2[i])

print(resultarr)

# --------------------------------------------------

# Write a code to find the maximum value from an array without using in-built function.

givenarr3 = [10, 45, 23, 89, 12, 67]
maxnum= givenarr3[0]

for i in range(1, len(givenarr3)):
    if givenarr3[i] > maxnum:
        maxnum = givenarr3[i]

print("Maximum value from array is: ", maxnum)