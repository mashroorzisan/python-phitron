def full_name(fi, la):
    name = f'full name is : {fi} {la}'
    return name


name = full_name(la='Ishtiaque', fi='Ahmed')
print(name)


def famous_name(first, last, **kargs):
    name = f'{first} {last}'
    # print(kargs['sur'])
    for key, val in kargs.items():
        print(key, val)
    return name


my_name = famous_name(first='aian', last='waniya',
                      sur='zania', fake='zanziber')
print(my_name)


# python can return multiple values

def multiple(num1, num2):
    sum = num1+num2
    sub = num1-num2
    mul = num1*num2
    div = num1/num2
    return sum, mul, sub, div


print(multiple(1, 2))
