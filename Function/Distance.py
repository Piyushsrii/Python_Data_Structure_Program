'''Write a program Distance.java that takes two integer command-line arguments x
and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The
formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function'''
import math
class Distance:
    def distance(x, y):
        """
    :param x: point 1
    :param y: point 2
    :return:  distance between 2 point
        """

        diff = math.sqrt((x ** 2 + y ** 2))
        print(diff)
        # here difference is returned
        return diff
if __name__ == '__main__':
        try:  # try is used for catching errors
            x = int(input("enter num 1 : "))
            if x <= 0 or x >= 1000:
                print("enter the number between 0 and 1000")
            y = int(input("enter num 2 : "))
            if y <= 0 or y >= 1000:
                print("enter the number between 0 and 1000")
            # function is called
            calling=Distance()
            calling.distance(x, y)
        except ValueError:  # if error is caught then below statement will be printed
            print("check the input ")