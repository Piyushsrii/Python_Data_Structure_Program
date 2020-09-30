class SumValues:
    def Sum(num1, num2, num3):
        """
        :param num1: input of num1 is taken
        :param num2: input of num2 is taken
        :param num3: input of num3 is taken
        :return: sum of all the input is checked is zero or not
        """
        if num1 + num2 + num3 == 0:
            print("sum is zero")
            return True
        else:
            print("sum is not zero")
            return False
# this function is called for calculating input of integer
if __name__ == '__main__':
    while True:
        try:   # try is used for catching any error

            num1 = int(input("enter number 1 :"))
            if num1 <= 0 or num1 >= 1000:
                print("enter between 0 and 1000")
                #continue
            num2 = int(input("enter number 2 :"))
            if num2 <= 0 or num2 >= 1000:
                print("enter between 0 and 1000")
                #continue
            num3 = int(input("enter number 3 :"))
            if num3 <= 0 or num3 >= 1000:
                print("enter between 0 and 1000")
                #continue
                calling = SumValues()
                calling.Sum(num1, num2, num3)
            break
        except ValueError:     # if error is found in input then below statement will be printed
            print("check the input")
