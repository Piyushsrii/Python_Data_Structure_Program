'''Write a Python script to sort (ascending and descending) a dictionary by value.'''
import operator
class SortingDictionary:
    def sorting(self, dictOfNum):
        '''
            :param self:
            :param dictOfNum:
            :return:
            '''
        print('Original dictionary : ', dictOfNum)
        sortedAsc = dict(sorted(dictOfNum.items(), key=operator.itemgetter(1)))
        print('Dictionary in ascending order by value : ', sortedAsc)
        sortedDesc = dict(sorted(dictOfNum.items(), key=operator.itemgetter(1), reverse=True))
        print('Dictionary in descending order by value : ', sortedDesc)
dictionary = SortingDictionary()
rangeVal = int(input("Enter The range of value you want to enter : "))
dictOfNum = { }
for i in range(1,rangeVal+1):
    val = int(input("Enter The value for array : "))
    dictOfNum.setdefault(i, val)
dictionary.sorting(dictOfNum)