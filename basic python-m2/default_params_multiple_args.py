# default parameters
def all_(x, y, z=0):
    print(x, y, z)


all_(12, 3)


# multiple arguments


def sum(*args):
    s = 0
    for num in args:
        s += num
    return s


total = sum(12, 21, 33, 53)
print('all sum: ', total)
