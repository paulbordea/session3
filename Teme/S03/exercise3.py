from Teme.S03.domain import Sex
from Teme.S03.domain import Human


class Male(Human):
    def __init__(self, name, age):
        Human.__init__(self, name, age, Sex.male)


class Female(Human):
    def __init__(self, name, age):
        Human.__init__(self, name, age, Sex.female)


man1 = Male('Tom Adams', 25)
woman1 = Female('Diana Brows', 40)

print(man1)
print(woman1)