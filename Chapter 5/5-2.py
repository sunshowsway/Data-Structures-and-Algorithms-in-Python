import sys


data = []
highest = sys.getsizeof(data)
for k in range(27):
    a = len(data)
    b = sys.getsizeof(data)
    if b > highest:
        highest = b
        print("Length: {0:3d};".format(a-1))
    data.append(None)
