

def is_lucky(n):
    for d in str(n):
        if d not in '47':
            return False
    return True


def lucky(start, end):
    lucky_num = []
    for i in range(start, end + 1):
        if is_lucky(i):
            lucky_num.append(i)
    return lucky_num


s = int(input())
e = int(input())

if s > e:
    print(-1)
else:
    for i in lucky(s, e):
        print(i)
