'''Write a Python program to remove an item from a tuple.'''
class RemoveItem:

    #Create methos to remove value
    def toRemoveItem(self,tupleValue,remVal,indexVal):
        '''
             :param:tupleValue: tuple value
             :param:remVal: remove value
             :param:index: index value
             :return : return after the remove
             '''
        tupleValue = tupleValue[:indexVal] + tupleValue[indexVal+1:]
        print("Using Merging Removed Value : ",tupleValue)
        listTuple = list(tupleValue)
        listTuple.remove(remVal)
        tupleValue = tuple(listTuple)
        print("Using Conversion Removed Value : ",tupleValue)
try :
    tupleData = RemoveItem()
    rangeVal = int(input("Enter The range of value you want to enter : "))
    tupleValue = ( )
    for j in range(rangeVal):
        val = input("Enter The Int value for tuple : ")
        tupleValue = tupleValue[ : j] + (val,) + tupleValue[ j : ]
        print("Tuple Data :- ", tupleValue)
        indexVal = int(input("Enter index value you want to Remove : "))
        remVal = input("Enter value you want to Remove : ")
except RemoveItem:
    tupleData.toRemoveItem(tupleValue,remVal,indexVal)