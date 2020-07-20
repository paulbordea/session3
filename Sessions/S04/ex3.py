try:
    with open('c:\\tmp\\abc33.txt', 'r') as fh:
        for line in fh.readlines():
            print(line)
except FileNotFoundError as e:
    print(e)
else:
    print('on else')
finally:
    print('finally block')

print('Continuing flow')

with open('c:\\tmp\\abc1.txt', 'a') as fh:   # w - overwrites; a - appends
    fh.write('line 1\n')
    fh.write('line 2\n line 3\n')


