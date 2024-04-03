def reverse(num):
    rev = 0
    while (num > 0):
        rev = rev*10+num % 10
        num = num // 10
    print(rev)
    return rev


N = int(input())
re = reverse(N)
if (N == re):
    print("YES")
else:
    print("NO")
