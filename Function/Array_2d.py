'''Desc -> A library for reading in 2D arrays of integers, doubles, or booleans from
standard input and printing them out to standard output.'''
import numpy as np
# array function is used to complete the task
class Array:
    # array function is created
    def Array2d(self, row, col):
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
if __name__ == "__main__":
    row = int(input("number of rows : "))
    if row <= 0 or row >= 1000:
        print("check the input for row")
    col = int(input("number of cols : "))
    if col <= 0 or col >= 1000:
        print("check the input for row")
        calling = Array()
    calling.Array2d(row, col)