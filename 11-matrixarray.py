from numpy import *

arr1 = array([[1,2,3],[4,5,6]])

print(arr1)
print(arr1.ndim)    # show the no. of dimension
print(arr1.shape)   # show the no. of rows & columns
print(arr1.size)    # show the total numbers
print(arr1.flatten())   # make 2d array to 1d array

arr2 = array([[1,2,3,4,5,1],[4,5,6,8,2,9]])
print(arr2.reshape(4,3))    # it show the 2d array make it 3d array (4 rows 3 columns)

# MATRIX
# m = matrix([[1,2,3],[4,5,6],[7,8,9]])
m = matrix('1 2 4 5; 6 5 3 2 ; 8 5 3 9')    # to add the ';' to create matrix this way
print('matrix value: ',m)
print('Diagonal: ', m.diagonal())

m2 = matrix('1 2 4 8; 6 3 3 2 ; 6 5 3 1')

print('addition of matrix: ', m + m2)
# print(m * m2)

# --------------------------------------------------
# ASSIGNMENT

# Write a code to multiply 2 matrices using 2D array & using for loops

matrix1 = [[1,2], [3,4]]
matrix2 = [[5,6],[7,8]]

result = [[0,0],[0,0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

for row in result:
    print('result: ', row)

