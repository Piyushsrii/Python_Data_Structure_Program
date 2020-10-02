'''Write a Python program to generate all permutations of a list in Python.'''
import itertools
class ListPermutation:

    #this method calculate the permutation
    def getPermutation(self, listOfStr):
        permList = (list(itertools.permutations(listOfStr)))
        return permList
listData = ListPermutation()
rangeVal = int(input("Enter The range of value you want to enter : "))
listOfStr = []
for i in range(1, rangeVal + 1):
    strVal = input("Enter The Words In List : ")
    listOfStr.append(strVal)
print("List Data :- ", listOfStr)
print("The Updated List Are : ", listData.getPermutation(listOfStr))