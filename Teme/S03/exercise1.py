import re


def splitter(value: str) -> list:
    if len(value) % 2 == 1:
        value += "_"

    return re.findall("[\\w\\s]{2}", value)


print(splitter('String with odd number of characters'))
print(splitter('String with even number of characters'))
