'''Write a Python program to multiplies all the items in a list.'''
class MulListItems:

    #Create a method fo list element and multiply
    def toMul(self,ListOfNum):
        """
                :param dListOfNum: multiply the list element
                :return: output after the multiplication
               """
        sum = 1
        for x in ListOfNum:
            sum *= x
            print("Multiplication Of List Items is : ",sum)
try :
    rangeVal = int(input("Enter The range of value you want to enter : "))
    ListOfNum = [ ]
    for i in range(1,rangeVal+1):
        val = int(input("Enter The value for List : "))
        ListOfNum.append(val)
        print("List Data :- ",ListOfNum)
except OverflowError:
    print("check the output")
    if __name__=='__main__':
        listData = MulListItems()
        listData.toMul(ListOfNum)