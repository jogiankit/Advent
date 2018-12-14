def CountTwo(sTwo = []):
    for i in range(len(sTwo)):
        if sTwo[i] == 2:
            return True

def CountThree(sThree = []):
    for i in range(len(sThree)):
        if sThree[i] == 3:
            return True

def ProcessString(s):
    global a
    global b
    myArray = [0]*27
    for c in s:
        myArray[(ord(c)-97)]+=1
    if CountTwo(myArray):
        a+=1
    if CountThree(myArray):
        b+=1

def CountOccurance(a1 = [], a2 = []):
    t = -2
    for d in range(len(a1)):
        if a1[d] != a2[d]:
            t+=1
    return t

def GetMissingIndex(a1 = [], a2 = []):
    #t = 0
    #f = 0
    #for y in range(len(a1)):
    #    if (a1[y] >= 0 or a2[y] >= 0):
    #        f = y;
    #        break
    for d in range(len(a1)):
        if a1[d] != a2[d]:
            return d

def GetCommonBoxID(s1, s2):
    global ans2
    a1 = [0] * 26
    a2 = [0] * 26
    for c in s1:
        a1[(ord(c) - 97)] += 1
    for c in s2:
        a2[(ord(c) - 97)] += 1

    if CountOccurance(a1,a2) == 0:
        #m = GetMissingIndex(a1, a2)
        #ans2 = s1[:m] + s1[m+1:]
        return True
    return False


with open("input2.txt") as f:
    myList = list(map(str, f.read().split()))

a=0
b=0
ans1=0
ans2 = None

for x in range(len(myList)):
    ProcessString(myList[x])

ans1=a*b
print(ans1)

for p in range(len(myList)):
    for q in range(len(myList)):
        if GetCommonBoxID(myList[p], myList[q]):
            m = GetMissingIndex(myList[p], myList[q])
            s1 = myList[p]
            s2 = myList[q]
            ans2 = s1[:m] + s2[m + 1:]
            break
    if ans2 != None:
        break

print(ans2)