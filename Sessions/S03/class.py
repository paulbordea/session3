class Car:
    has_motor = 'abc'  # variabila de clasa

    def __init__(self, name, year):
        self.name = name        # variabile de instanta
        self.year = year

    # dunder methods
    def __repr__(self):
        return f'Car is {self.name} from year {self.year}'


c1 = Car('Dacia', 1998)
c2 = Car('Audi', 2003)
print(c1)
print(c2)
print(c1.has_motor)
print(c2.has_motor)