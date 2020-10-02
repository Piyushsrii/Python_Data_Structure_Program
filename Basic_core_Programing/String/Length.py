'''Write a Python function that takes a list of words and returns the length of the longest
one.'''
class StringLength:

    #create this method to checkthe length
    def chkLength(self,strVal):
        '''
        :param:strVal: Sting length
        :return : Character count
         '''
        charCount = 0
        for x in strVal:
            charCount += 1
        return charCount
stringData = StringLength()
strVal = input("Enter A String : ")
print("String Character Count is : ",stringData.chkLength(strVal))