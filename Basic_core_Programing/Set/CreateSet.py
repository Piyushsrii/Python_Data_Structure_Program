'''Write a Python program to create a set'''
class CreateSet:

    #create method for set
    def create(self,dictOfNum):
        """
                        :param dictOfNum: input of dicOfNum is taken
                        :return: return set of element
                    """
        emptySet = set()
        print("Empty Set : ", emptySet)
        nonEmptySet = set(dictOfNum)
        print("Non Empty Set : ", nonEmptySet)
rangeVal = int(input("Enter The range of value you want to enter : "))
dictOfNum = [ ]
try:
    for i in range(1,rangeVal+1):
        val = input("Enter The value : ")
        dictOfNum.append(val)
except ValueError:
    print("Check your input")
    if __name__=="__main__":
        setData = CreateSet()
        setData.create(dictOfNum)
