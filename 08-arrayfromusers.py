from array import  *

# n = int(input('Enter the length of the array: '))
#
# arr = array('i', [])
#
# for i in range(n):
#     x = int(input('Enter a number: '))
#     arr.append(x)
#
# print(arr)
#
# # search a number from that array
# findNum = int(input('Enter a number: '))
#
# k = 0
# for i in arr:
#     if arr[i] == findNum:
#         print(k)
#         break
#     k+=1

# OR    arr.index(findNum)

# --------------------------------------------------
# ASSIGNMENT

# Create an array with 5 values & delete the value at index number 2 without using in-built function.

# arr1 = int(input("Enter the length of the array: "))
#
# inputs = array('i', [])
#
# for i in range(arr1):
#     x = int(input('Enter a number: '))
#     inputs.append(x)
# print(inputs)
#
# index = int(input('Enter the index value wangt to delete: '))
#
# for i in range(index, len(inputs)-1):
#     inputs[i] = inputs[i+1]
# inputs = inputs[:len(inputs) - 1]
#
# print("Array after deletion:", inputs)

# OR
# inputs.pop(2)
# print(inputs)

# --------------------------------------------------

# Write a code to reverse an array.

arr = [50, 30, 10, 20, 80]

start = 0
end = len(arr)-1
while start<end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

print('Reversed Array:', arr)