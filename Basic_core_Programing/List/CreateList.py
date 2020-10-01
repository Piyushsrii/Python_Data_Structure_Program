'''Write a Python program to sum all the items in a list.'''
class SumListItems:

    #create method Sum of list element
    def toSum(self,ListOfNum):
        '''
                :param:ListOfNum: Element in list
                :return: sum of each element of list
        '''
        sum = 0
        for x in ListOfNum:
            sum += x
        print("Sum Of List is : ",sum)
try :
    rangeVal = int(input("Enter The range of value you want to enter : "))
    ListOfNum = [ ]
    for i in range(1,rangeVal+1):
        val = int(input("Enter The value for List : "))
        ListOfNum.append(val)
        print("List Data :- ",ListOfNum)
except OverflowError :
    if __name__=='__main__':
        listData = SumListItems()
        listData.toSum(ListOfNum)