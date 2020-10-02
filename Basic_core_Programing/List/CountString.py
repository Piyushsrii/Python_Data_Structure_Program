'''Write a Python program to count the number of strings where the string length is 2 or
more and the first and last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2'''
class CountStrings:

    #Create method to count the ring
    def matchCharacter(self,listOfStr):
        '''
        :param:firstSetvalue pass the first value
        :param:SecondSetValue pass the second value
        :return : return the insection value
        '''
        countStr = 0
        for Str in listOfStr:
            if len(Str) > 1 and Str[0] == Str[-1]:
                countStr += 1
        print("The String Count Whos First And Last Char Is Same Are : ",countStr)
try :
    rangeVal = int(input("Enter The range of value you want to enter : "))
    listOfStr = [ ]
    for i in range(1,rangeVal+1):
        val = input("Enter The value for List in Strings : ")
        listOfStr.append(val)
        print("List Data :- ",listOfStr)
except ValueError:
     if __name__=="__main__":
         listData = CountStrings()
         listData.matchCharacter(listOfStr)