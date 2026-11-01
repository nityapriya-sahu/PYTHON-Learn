# Position Argument:
def person1(name, age):
    print(name)
    print(age)

person1('Nitya', 28)    # Here if i change the position of the args then it gives error. (Position Argument)

# Keyword Argument:
def person2(name, age):
    print(name)
    print(age)

person2(age = 25, name='Sahu')     # To prevent the position args then we have to use keyword args. No error comes (Keyword Argument)


# Default Argument:
def person3(name, age=18):
    print(name)
    print(age)

person3('Chintu')   # if here not pass age args it will not gives error, because we give default value 18. (Default Argument)


# Variable length Argument:
def sum(a, *b):      # here we have to use * if user added more args it will store in b parameter
    c = a
    for i in b:
        c = c+i
    print(c)

sum(5, 10, 15, 20)


# Keyworded Variable Length Arguments (KWARGS):
# It is denoted as **
def person4(name, **data):
    # print(name)
    print('DATA: ',data)

    # or we can write it as key value pair
    for i, j in data.items():
        print(i, j)
person4('Chintesh', age=28, gender='male', city="pune", country='India', mob=1234567890)