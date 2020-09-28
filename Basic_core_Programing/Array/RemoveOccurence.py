class RemoveOccurence:
    def removeOccurence(self,arrOfNUm,value):
        print("Original array: " + str(arrOfNum))
        arrOfNum.remove(value)
        print("Number of occurrences of the number ",value," in array: " + str(arrOfNUm.count(value)))
        print("Updated array: " + str(arrOfNum))
arr = RemoveOccurence()
rangeVal = int(input("Enter The range of value you want to enter : "))
arrOfNum = []
for i in range(rangeVal):
    val = int(input("Enter The value for array : "))
    arrOfNum.append(val)
Value = int(input("Enter The Value You Want To Remove : "))
arr.removeOccurence(arrOfNum,Value)