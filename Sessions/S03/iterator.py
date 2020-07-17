class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        if True:
            return self.value
        else:
            raise StopIteration


rep = Repeater('hello')

for item in rep:
    print(item)
