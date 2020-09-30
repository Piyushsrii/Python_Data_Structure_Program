import numpy as np
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

