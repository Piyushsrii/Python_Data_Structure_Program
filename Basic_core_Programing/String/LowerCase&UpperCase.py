'''Write a Python script that takes input from the user and displays that input back in
upper and lower cases.'''
class CharacterLowerCase:

    #Create this method Upper & lower case
    def toLowecase(self,strVal,position):
        '''
              :param:strVal: colection of Tuple Element
              :param:strVal: position to check lower and Upper case
              :return : return the upper and lower case value
              '''
        print("Updated String : ",strVal[:position].lower() + strVal[position:])
stringData = CharacterLowerCase()
strVal = input("Enter a string : ")
position = int(input("Enter position number to which you want the character to lowercase :"))
stringData.toLowecase(strVal,position)