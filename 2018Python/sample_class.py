class Student(object):
    def __init__(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_major(self, major):
        self.major = major

al = Student("Alice")
al.set_age(21)
al.set_major("Informatics")
print(al.name, al.age, al.major)

class MasterStudent(Student):
    internship = "mandatory, from March to June"

bo = MasterStudent("Bob")
bo.set_age(23)
print(bo.internship, bo.age)
