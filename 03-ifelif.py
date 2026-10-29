x = 10
result = x%2

if result == 0:
    print('Even')
else:
    print('Odd')


# --------------------------------------------------

a = 2

if  a==1:
    print('One')
elif a ==2:
    print('Two')
elif a==3:
    print('Three')
else: print('Wrong input')

# --------------------------------------------------
# ASSIGNMENT
# 01: Write a code to check a given number is positive or negative
num = -12
if num>0: print('Positive number')
else: print('Negative number')

# 02: Take three values from user & find the greatest number from them.
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))

if num1 >= num2 >= num3:
    print("Greatest number is : ",num1)
elif num2>=num1 and num2>=num3:
    print("Greatest number is : ",num2)
else:
    print("Greatest number is : ",num3)

# OR
greatestNum = max(num1,num2,num3)
print(greatestNum)