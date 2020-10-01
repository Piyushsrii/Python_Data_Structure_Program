'''Write a Python program to iteration over sets.'''
class IterateSets:

    #create a method to iterate  the dict
    def toIterate(self,dictOfNum):
        """
         :param dictOfNum: use for iterate set value
         :return: Remove the repeating value
        """
        numItrSet = set(dictOfNum)
        for n in numItrSet:
            print(n)

rangeVal = int(input("Enter The range of value you want to enter : "))
dictOfNum = []
try:
    for i in range(1, rangeVal + 1):
        val = input("Enter The value : ")
        dictOfNum.append(val)
except ValueError:
    print("enter the correct value")
    if "__name__"=="__main__":
            setData = IterateSets()
            setData.toIterate(dictOfNum)