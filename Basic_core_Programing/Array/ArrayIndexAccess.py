'''Write a Python program to create an array of 5 integers and display the array items.
Access individual element through indexes.'''
class ArrayOfIntegers:
    def index(self,arrayNum,indexValue):
        '''
               :param:self
               :param:arrayNum
               :param:indexValue
               :return
              '''
        print(arrOfNum)
        print("Access first three items individually")
        print("Searched Index Element : ",arrayNum[indexValue])
        print("Last Element : ", arrayNum[-1])
        print("First Element :", arrayNum[1])
arr = ArrayOfIntegers()
arrOfNum = []
n=int(input("Enter the value of Array"))
for i in range(n):
    val = int(input("Enter The value for array : "))
    arrOfNum.append(val)
indexValue = int(input("Enter The Index Value You Want To Find : "))
arr.index(arrOfNum,indexValue)