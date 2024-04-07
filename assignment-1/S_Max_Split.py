string = input()
point = 0
list=[]
ans = 0
i = 0

for c in string:
    i+=1
    if(c=="R"):
        point+=1
    elif(c=="L"):
        point-=1
    if (point == 0):
        ans+=1
        # print(i)
        list.append(i)
print(ans)
strt = 0
for itr in list:
     
     print(string[strt:itr])
     strt = itr

