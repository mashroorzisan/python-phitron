n = int(input())
numlist = list(input().split())
for i in range(0,n):
    numlist[i]=int(numlist[i])

# print(numlist)
def check(numlist):
    for num in numlist:
        if(num%2!=0):
            return False
    return True

count=0
while check(numlist):
    for i in range(0,n):
        numlist[i] /= 2
    count+=1

print(count)