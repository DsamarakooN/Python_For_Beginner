numList = [2,4,6,8,3,4,2,1]
evenList = []

for i in numList:
    if(i%2 == 0 ) and (i not in evenList):
        evenList.append(i)

print(evenList)