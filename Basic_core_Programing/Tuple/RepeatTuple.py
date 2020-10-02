'rite a Python program to find the repeated items of a tuple.'
class RepeatedItem:

    #Create Method to count the number
    def findRepetedItem(self,tupleValue,findVal):
        '''
        :param:tupleValue: colection of Tuple Element
        :return : return count the value
        '''
        countValue = tupleValue.count(findVal)
        print("Count Of Value ",findVal,"Is : ",countValue)
try :
    tupleData = RepeatedItem()
    rangeVal = int(input("Enter The range of value you want to enter : "))
    tupleValue = ( )
    for j in range(rangeVal):
       val = int(input("Enter The Int value for tuple : "))
       tupleValue = tupleValue[ : j] + (val,) + tupleValue[ j : ]
       print("Tuple Data :- ", tupleValue)
       findVal = int(input("Enter value you want to Count : "))
except OverflowError:
    tupleData.findRepetedItem(tupleValue,findVal)