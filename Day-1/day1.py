with open("input.txt") as f:
    myList = list(map(int, f.read().split()))

ans1=0
ans2=0
tList = []
flag=0
temp=0

for i in range(len(myList)):
    temp+=myList[i]
    if flag == 0:
        if temp in tList:
            flag=1
            ans2=temp
        else:
            tList.append(temp)
ans1=temp
print(ans1)

if flag == 0:
    while flag == 0:
        for i in range(len(myList)):
            temp+= myList[i]
            if flag == 0:
                if temp in tList:
                    flag = 1
                    ans2 = temp
                    break
print(ans2)