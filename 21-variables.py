# Type of Variables:
#     1. Instance Variables
#     2. Class(static) Variables


class Car:

    wheels = 4      # Class Variables

    def __init__(self):
        self.company='BBT'
        self.mileage = 10       # These two are Instance Variables

c1 = Car()
c2 = Car()

c1.company = 'RR'
c2.mileage = 20

c1.wheels = 8

print(c1.company, c1.mileage, c1.wheels)
print(c2.company, c2.mileage, c2.wheels)