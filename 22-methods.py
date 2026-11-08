# Type of Methods
#     1. Class Methods
#     2. Static Methods
#     3. Instance Methods

class Student:

    school = 'My_School'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def get_school(cls):
        return cls.school

    @staticmethod
    def info():
        return 'Details of school Information'


s1 = Student(10, 20, 30)
s2 = Student(90, 40, 50)

print('s1 avg = ', s1.avg())
print('s2 avg = ', s2.avg())

print(Student.get_school())
print(Student.info())
