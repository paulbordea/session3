class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f'{self.fname} {self.lname}'


p1 = Person('John', 'Smith')


class Student(Person):
    pass


if __name__ == '__main__':
    s = Student('Tom', 'Adams')
    print(s)

    print(isinstance(s, Student))
    print(isinstance(s, Person))

    print(issubclass(Student, Person))
