import sys

for item in sys.path:
    print(item)

if 'c:\\temp' not in sys.path:
    sys.path.append('c:\\temp')

for item in sys.path:
    print(item)
