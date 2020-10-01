'''Write a Python program to remove a key from a dictionary.'''
class RemoveKey:

    #this methos for remove key
    def remove(self, dictOfNum, keyValue):
        """
                   :param num1: input of dicOfNum is taken
                   :param num2: input of keyValue is taken
                   :return: return the deleted value
               """
        if keyValue in dictOfNum:
            del dictOfNum[keyValue]
        print("Updated Dictionary : ",dictOfNum)

dictkey = RemoveKey()
rangeVal = int(input("Enter The range of value you want to enter : "))
dictOfNum = {}
for i in range(1,rangeVal+1):
    key = input("Enter The Key : ")
    val = input("Enter The value for dictionary : ")
    dictOfNum.setdefault(key, val)

print("Dictionary : ", dictOfNum)
keyValue = input("Enter The Key You Want To Delete : ")
dictkey.remove(dictOfNum, keyValue)