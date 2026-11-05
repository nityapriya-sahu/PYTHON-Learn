def divide(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if a < b:
            a,b = b,a
        return func(a, b)

    return inner

divide = smart_div(divide)
divide(10,30)