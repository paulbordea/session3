def show_return():
    return 1, 2, 3, 'ceva'


result = show_return()
print(f'Type is {type(result)}')
print(f'Function returns {result}')


(a, b, c, d) = show_return()
print(f'c={c}')
