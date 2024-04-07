n = int(input())
numlist = list(input().split())
for i in range(0,n):
    numlist[i]=int(numlist[i])

freqdict = {}
for num in numlist:
    if num in freqdict:
        freqdict[num] += 1
    else:
        freqdict[num] = 1

overflow = 0
for num , freq in freqdict.items():
    if freq < num:
        overflow += freq
    elif freq > num:
        overflow += (freq - num)

print(overflow)
