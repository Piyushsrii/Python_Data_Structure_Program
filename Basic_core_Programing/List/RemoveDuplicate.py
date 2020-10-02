import itertools

class RemDupLists:
    def toRemDupLists(self,mainList):
        print("Original List : ", mainList)
        mainList.sort()
        newList = list(num for num, _ in itertools.groupby(mainList))
        print("Updated List : ", newList)

listData = RemDupLists()
rangeVal = int(input("Enter The Number of List you want to enter : "))
mainList = [ ]
for i in range(1,rangeVal+1):
    subList = [ ]
    rangeSubVal = int(input("Enter how times you want to add value : "))
    for j in range(rangeSubVal):
        val = int(input("Enter The value for tuple : "))
        subList.append(val)
    mainList.append(subList)

listData.toRemDupLists(mainList)