''' Write a Python program which accepts the user's first and last name and print them in
reverse order with a space between them.'''
class ReverseString: # define class of this program

    def toReverse(self,strVal): # Define here user define function and using variables revStr and index
        '''
        :param self:
        :param strVal:
        :return:
        '''
        revStr = ''
        index = len(strVal)
        while index > 0:        # Using while loop for reverse the value
            revStr += strVal[index - 1]
            index = index - 1
        return revStr
stringData = ReverseString()
strVal = input("Enter a String To Reverse : ")
print("Reverse String : ",stringData.toReverse(strVal))
