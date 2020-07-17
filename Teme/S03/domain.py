from enum import Enum


class Sex(Enum):
    male = 1
    female = 2


class Human:
    def __init__(self, name: str, age: int, sex: Sex):
        self.name: str = name
        self.age: int = age
        self.sex: Sex = sex

    def __repr__(self):
        return f'{self.name} is {self.age} years old and is a {self.sex.name}'


if __name__ == '__main__':
    human_male = Human('Some human', 33, Sex.male)
    human_female = Human('Some human', 33, Sex.female)
    print(human_male)
    print(human_female)
