def by_value(param):
    param += 1
    print(f'din functie, param={param}')


in_test = 1
by_value(in_test)
print(f'in afara functiei, in_test={in_test}')



def by_ref(param):
    param.append(100)
    print(f'din functie, param={param}')


in_test_2 = [1, 2, 3]
by_ref(in_test_2)
print(f'in afara functiei, in_test={in_test_2}')