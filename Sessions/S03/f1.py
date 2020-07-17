def print_it(value):
    """ Print the given parameter.
    :param value - value to print
    :return none
    """
    print(f'Hello, the result is {value}')


def add(a, b, f):
    result = a + b
    f(result)


add(4, 10, print_it)
