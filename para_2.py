class Student:
    print("Hi!")
    def __init__(self, height=168):
        self.height = height


vasya = Student()
print(vasya.height)

dima = Student(height=186)
print(dima.height)

