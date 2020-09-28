'''Write a Python program to reverse the order of the items in the array.'''
class ReverseArray:
    def reverse(self,arrOfNum):
        '''
                      :param:self
                      :param:arrOfNum
                      :return:
                     '''
        print("Original array: " + str(arrOfNum))
        arrOfNum.reverse()
        print("Reverse array: " + str(arrOfNum))
arr = ReverseArray()
rangeVal = int(input("Enter The range of value you want to enter : "))
arrOfNum = []
for i in range(rangeVal):
    val = int(input("Enter The value for array : "))
    arrOfNum.append(val)
arr.reverse(arrOfNum)