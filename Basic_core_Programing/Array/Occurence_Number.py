'''Write a Python program to get the number of occurrences of a specified element in an
array.'''
class OccurenceInArray:
    def countOccurence(self, arrOfNum, value):
        '''
            :param:self
            :param:arrOfNUm
            :param:value
            :return:
            '''
        print("Original array: " + str(arrOfNum))
        print("Number of occurrences of the number ", value, " in array: " + str(arrOfNum.count(value)))
arr = OccurenceInArray()
rangeVal = int(input("Enter The range of value you want to enter : "))
arrOfNum = []
for i in range(rangeVal):
    val = int(input("Enter The value for array : "))
    arrOfNum.append(val)
Value = int(input("Enter The Value You Want To Find Ocuurence of : "))
arr.countOccurence(arrOfNum, Value)