import Array2d
import numpy as np
# array function is used to complete the task
class Array:
    # array function is created
    def Array2d(row, col):
        """
        :param row: no of row
        :param col: no of col
        :return: 2d array
        """
        try:  # try is used for locating the error
            array = [[[np.random.randint(0, 10)] for i in range(row)] for j in range(col)]  # array is created by this
            # function
            print(array)
            return array  # array is returned
        except IndexError:
            print("index error please check ")
        if __name__ == '__main__':
            while True:
                try:
                    row = int(input("number of rows : "))   # user input is taken
                if row <= 0 or row >= 1000:
                    print("check the input for row")
                continue
                col = int(input("number of cols : "))
                if col <= 0 or col >= 1000:
                    print("check the input for row")
                continue
            # array function is called to do the need full
            Array2d(row, col)
            break
        except ValueError:
            print("check the input")