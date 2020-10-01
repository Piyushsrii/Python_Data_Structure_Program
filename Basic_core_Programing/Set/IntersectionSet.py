'''Write a Python program to create an intersection of sets.'''
class CreateIntersection:

    #create method to intersection
    def intersection(self,firstSetValue,SecondSetValue):
        '''
        :param:firstSetvalue pass the first value
        :param:SecondSetValue pass the second value
        :return : return the insection value
                     '''
        intersectionSet = firstSetValue & SecondSetValue
        print(intersectionSet)
try:
    firstSetValue = set()
    rangeVal = int(input("Enter The Range Of Values You Want To Enter In First Set: "))
    for i in range(1, rangeVal + 1):
        valAddFirst = input("Enter The String Or Value : ")
        firstSetValue.add(valAddFirst)

        SecondSetValue = set()
        rangeVal = int(input("Enter The Range Of Values You Want To Enter In First Set: "))
    for i in range(1, rangeVal + 1):
        valAddSecond = input("Enter The String Or Value : ")
        SecondSetValue.add(valAddSecond)
        print("Data Set First: ",firstSetValue)
        print("Data Set Second: ",SecondSetValue)
except firstSetValue:
    if __name__=="__main__":
        setMembers = CreateIntersection()
        setMembers.intersection(firstSetValue,SecondSetValue)