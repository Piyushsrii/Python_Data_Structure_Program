'''Write a program Quadratic.java to find the roots of the equation a*x*x + b*x + c.
Since the equation is x*x, hence there are 2 roots. The 2 roots of the equation
can be found using a formula (Note: Take a, b and c as input values)'''
class Quadratic :

    # Quad function is created
    def Quad(num1, num2, num3):
        """
            :param num1: number 1 taken as input
            :param num2: number 2 taken as input
            :param num3: number 3 taken as input
            :return: after calculating quad results are returned
        """
        delta = num2 * num2 - 4 * num1 * num3
        # have to convert -ve delta to +ve ,as -ve val does not have square roots
        print(abs(delta))
        root1 = (-num2 + math.sqrt(abs(delta))) / (2 * num1)
        root2 = (-num2 - math.sqrt(abs(delta))) / (2 * num1)
        # after calculating roots output is printed
        print("root 1: ", root1)
        print("root 2 : ", root2)
        # roots are returned
        return root1, root2
if __name__ == '__main__':
        try:  # try is used for catching any error
            num1 = int(input("enter number 1 :"))
            if num1 <= 0 or num1 >= 1000:
                print("enter between 0 and 1000")
            num2 = int(input("enter number 2 :"))
            if num2 <= 0 or num2 >= 1000:
                print("enter between 0 and 1000")
            num3 = int(input("enter number 3 :"))
            if num3 <= 0 or num3 >= 1000:
                print("enter between 0 and 1000")
            calling=Quadratic()
            calling.Quad(num1, num2, num3)
        except ValueError:
            print("check user input")