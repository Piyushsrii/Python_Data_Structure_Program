'''Write a Python program to count occurrences of a substring in a string.'''
class SubStringOccurence:

    #Create this method to find the occurence of substring
    def countOccurence(self,strVal,subString):
        '''
                   :param:strval: String value
                   :return : return the string element
                   '''
        print("The Count Of SubString ",subString," is : ",strVal.count(subString))
try:
    stringData = SubStringOccurence()
    strVal = input("Enter a string : ")
    subString = input("Enter a substring to count : ")
    stringData.countOccurence(strVal,subString)
except ValueError:
    print("Enter the correct value")