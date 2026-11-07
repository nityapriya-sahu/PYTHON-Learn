class Computer:

    def config(self):       # 'self' is the object which we are passing
        print('i5, 16gb, 1tb')


com1 = Computer()   # Here com1 is a Object
print(type(com1))   # output: class '__main__.computer'

com1.config() # preferrable syntax to call

Computer.config(com1)

