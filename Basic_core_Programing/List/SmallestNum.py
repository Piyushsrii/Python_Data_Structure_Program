'''Write a Python program to get the smallest number from a list.'''
class MinListItems:

    # find the minimum value
    def findMin(self,ListOfNum):
        """
         :param dictOfNum: use for iterate set value
         :return: Remove the repeating value
       """
        min = ListOfNum[0]
        for x in ListOfNum:
            if x < min:
                min = x
        print("Smallest Number in List Items is : ",min)
listData = MinListItems()
rangeVal = int(input("Enter The range of value you want to enter : "))
ListOfNum = [ ]
for i in range(1,rangeVal+1):
    val = int(input("Enter The value for List : "))
    ListOfNum.append(val)
print("List Data :- ",ListOfNum)
listData.findMin(ListOfNum)