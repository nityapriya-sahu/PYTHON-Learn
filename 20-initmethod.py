class Computer:
    # This is init method
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print('config is: ', self.cpu, self.ram)


com1 = Computer('i7', '16gb')
com2 = Computer('Ryzen 3', '8gb')

com1.config() # preferrable syntax to call
com2.config()

# Computer.config(com1)

