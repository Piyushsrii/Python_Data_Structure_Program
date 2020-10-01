'''Write a Python program to iterate over dictionaries using for loops'''
class IterateDictionary:

    #create a method for iteration
    def iterate(self, dictOfNum):
        print("Dictionary : ", dictOfNum)
        for key, value in dictOfNum.items():
            print(key, " is the key belongs to " , dictOfNum[key])

dictionary = IterateDictionary()
rangeVal = int(input("Enter The range of value you want to enter : "))
dictOfNum = { }
for i in range(1,rangeVal+1):
    key = input("Enter The Key : ")
    val = input("Enter The value for dictionary : ")
    dictOfNum.setdefault(key, val)

dictionary.iterate(dictOfNum)