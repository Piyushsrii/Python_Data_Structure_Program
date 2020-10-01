'''Write a Python program to remove item(s) from set'''
class RemoveItems:

    #create method to remove element
    def toremove(self,setValue,rmVal):
        for i in range(rmVal):
            setValue.pop()
        print(setValue)
try:
    setValue = set()
    rangeVal = int(input("Enter The Range Of Values You Want To Enter : "))
    for i in range(1, rangeVal + 1):
        valAdd = input("Enter The String Or Value : ")
        setValue.add(valAdd)
        print(setValue)
        rmVal = int(input("How Many Items You Want To Remove From List : "))
except setValue:
    print("enter the correct value")
    if __name__=="__main__":
        setMembers = RemoveItems()
        setMembers.toremove(setValue,rmVal)