'''Write a Python program to reverse a string.'''
class ReverseString:

    #This method create Reverse the string
    def toReverse(self,strVal):
        '''
        :param:strVal: Reverse the string
        :return : return after the remove
        '''

        revStr = ''
        index = len(strVal)
        while index > 0:
            revStr += strVal[index - 1]
            index = index - 1
        return revStr
stringData = ReverseString()
strVal = input("Enter a String To Reverse : ")
print("Reverse String : ",stringData.toReverse(strVal))