def greet():
    print('hello world')
    print('Good Morning')

greet()

# --------------------------------------------------

def add(a,b):
    c = a+b
    return c

print(add(5, 7))

# --------------------------------------------------

def add_sub(a,b):
    c = a+b
    d = a - b
    return c, d

result1, result2 = add_sub(10,5)
print(result1)
print(result2)
# print(add_sub(10,5))