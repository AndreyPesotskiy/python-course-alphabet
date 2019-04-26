


# This is object of class
# There is only one object of the same class.
from utils import describe_object


class Student:
    def __init__(self, name):
        pass

print(describe_object(name="Student", obj=Student))
# This is instances of class Student

# It could be a lot of instances of one class
student_1 = Student()

student_2 = Student()

student_3 = Student()

print(describe_object("student_1", student_1))
print(describe_object("student_2", student_2))
print(describe_object("student_3", student_3))


def some_func():
    return


some_int = 10
