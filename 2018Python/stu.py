class Student(object):
    def __init__(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_major(self, major):
        self.major = major

alice = Student('alice')
alice.set_age(21)
alice.set_major('informatics')

print(alice.name,alice.age,alice.major)


class MasterStudent(Student):
    internship = 'mandatory, from March to June'

bob = MasterStudent('Bob')
print(bob.internship)
bob.set_age(23)
print(bob.name,bob.age)
