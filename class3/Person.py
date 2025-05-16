class Person:
    def show(self):
        print("I am a person")


class Student(Person):
    def study(self):
        print("I am Studying")


s = Student()
s.study()
s.show()
