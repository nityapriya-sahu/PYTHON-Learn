from functools import reduce

nums = [5,6,3,4,8,7,10,3,2,12]
print('original array: ', nums)
# Filter() Function:
# * filter() function takes 2 parameters: a function and a iterable sequence

# def findeven(n):
#     if n%2==0:
#         return n
#
# even_nums = list(filter(findeven, nums))
# print(even_nums)

# Or to make it anonymous function we use lambda function
even_nums = list(filter(lambda n: n%2==0, nums))
print('filter: ',even_nums)

# --------------------------------------------------
# Map() Function:
# Doubles the even numbers using map() function
doubles = list(map(lambda n:n*2, even_nums))
print('map: ', doubles)

# --------------------------------------------------
# Reduce Function():
sum_of_nums = reduce(lambda a,b: a+b, nums)
print('Reduce: ',sum_of_nums)