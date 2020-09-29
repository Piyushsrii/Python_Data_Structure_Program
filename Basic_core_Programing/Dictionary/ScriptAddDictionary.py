'''Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}'''
class AddKeyToDict:
    def addKey(self, dictOfNum,key,value):
        print(dictOfNum)
        dictOfNum.update({key: value})
        print(dictOfNum)
'''
    :param self:
    :param dictOfNum:
    :param key:
    :param value:
    :return:
    '''
dictionary = AddKeyToDict()
rangeVal = int(input("Enter The range of value you want to enter : "))
dictOfNum = { }
for i in range(1,rangeVal+1):
    val = int(input("Enter The value for dictionary : "))
    dictOfNum.setdefault(i, val)
key = int(input("Enter The Key In Which You Want To Add The Value : "))
value = int(input("Enter The Value : "))
dictionary.addKey(dictOfNum,key,value)