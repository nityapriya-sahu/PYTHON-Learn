from array import *

vals = array('i',[5,8,9,0])
# vals.reverse()
# print(vals)

# To copy the same array and put in new Array

newArr = array(vals.typecode, (a for a in vals))    # The "typecode" character used to create the array.
for item in newArr:
    print(item)

# do the array in square
newArr1 = array(vals.typecode, (a*a for a in vals))
for item in newArr1:
    print(item)


# --------------------------------------------------
# ASSIGNMENT

# Write a code to sort an array in ascending order.

givenArr = [7,13, 5, 8, 15, 2]
for item in range(len(givenArr)):
    for j in range(item+1, len(givenArr)):
        if givenArr[item] > givenArr[j]:
            givenArr[item],givenArr[j] = givenArr[j],givenArr[item]

print("Sorted Array: ", givenArr)

# OR        givenArr.sort()
# --------------------------------------------------

# Write a code to find the factorial of a given number

givenInput = int(input('Enter a number: '))

factorial = 1
i = 1
while i <= givenInput:
    factorial*= i
    i+=1

print('Factorial of', givenInput, 'is: ', factorial)