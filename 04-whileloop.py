i = 1
while i<=5:
    print('Nitya ', end='')
    j=1
    while j<= 4:
        print('Sahu ', end='')
        j=j+1
    i=i+1
    print()  # for new line

# --------------------------------------------------
# ASSIGNMENT
# 01: Write the code to print all the values from 1 to 100. Skip the numbers which are divisible by 3 or 5.
i = 1
while i<=100:
    if i%3 !=0 and i%5!=0:
        print(i)
    i+=1

# 02: Write a code to print below pattern.
    # # # #
    # # # #
    # # # #
    # # # #

row = 1
while row<=4:
    column = 1
    while column<=4:
        print('#', end='')
        column +=1
    print()
    row+=1