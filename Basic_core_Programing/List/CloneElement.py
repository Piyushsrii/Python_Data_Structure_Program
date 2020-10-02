'''Write a Python program to remove duplicates from a list.'''
class CloningList:

    #create method clone
    def getClone(self,ListOfNum):
        '''
                      :param:ListOfNum: Clone the element in list
                      :return : return the insection value
               '''
        cloneList = list(ListOfNum)
        print("Original List : ",ListOfNum)
        print("Clone List : ",cloneList)
try:
    listData = CloningList()
    rangeVal = int(input("Enter The range of value you want to enter : "))
    ListOfNum = [ ]
    for i in range(1,rangeVal+1):
        val = int(input("Enter The value for List : "))
        ListOfNum.append(val)
except ValueError:
    print("enter the correct value")
    listData.getClone(ListOfNum)