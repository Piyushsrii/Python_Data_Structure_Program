'''Desc -> Given N distinct Coupon Numbers, how many random numbers do you
need to generate distinct coupon number? This program simulates this random
process.'''
import numpy as np
class CouponsProgram :

    # CoinToss function is created to count number of heads and tails
    def Coupons(number):
        """
        :param number: no of coupons wants to print
        :return:
        """
        array = []  # empty array is used for storing data
        for i in range(number):
            rand = np.random.randint(10, 100)
            array.append(rand)
            # only selecting unique numbers using set.
            unique = set(array)
            print(list(unique))
if __name__ == '__main__':
        try:  # try is used for catching the errors
            number = int(input("please enter number to generate coupons : "))
            if number <= 1 or number >= 1000:
                print("please enter the number between 0 and 1000")
            caller=CouponsProgram()
            caller.Coupons(number)
        except ValueError:  # errors are caught and below statement is printed
            print("check the input")