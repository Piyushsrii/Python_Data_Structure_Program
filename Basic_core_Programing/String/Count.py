'''Write a Python program to count the number of characters (character frequency) in a
string.
Sample String : google.com
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}'''
class CharFrequency:

    #check method to character frequency
    def chkCount(self,strVal):
        '''
              :param:strval: String value
              :return : return the string element
              '''
        dictCharCount = { }
        for n in strVal:
            keys = dictCharCount.keys()
            if n in keys:
                dictCharCount[n] += 1
            else:
                dictCharCount[n] = 1
        return dictCharCount
stringData = CharFrequency()
strVal = input("Enter A String : ")
print("String Character Count is : ",stringData.chkCount(strVal))