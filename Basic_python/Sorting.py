'''Write a Python program to sort three integers without using conditional statements and
loops.'''
class SortNumber:
    def sort(self,x,y,z):
        minNumber = min(x, y, z)
        maxNumber = max(x, y, z)
        middleNumber = (x + y + z) - minNumber - maxNumber
        print("Numbers in sorted order: ", minNumber, middleNumber, maxNumber)

number = SortNumber()
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

number.sort(x,y,z)