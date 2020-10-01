'''Desc -> Simulates a gambler who start with $stake and place fair $1 bets until
he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
times he/she wins and the number of bets he/she makes. Run the experiment N
times, averages the results, and prints them out.'''
import numpy as np
class GamblerSimulation :

    # gambler function is made for simulating gambling
    def Gambler(amount):
        """
        :param amount: amount to want to play
        :return: after player final amount is returned
        """
    try:
            play = int(input("times u want to play : "))
            # player input is taken for number of times he want to play
            if play <= 0 or play >= 11:
                print("enter between 1 and 10")
            # here input id taken on which dice number he wants to bet on
            dice = int(input("which number on the dice you want to bet : "))
            if dice <= 0 or dice >= 7:
                print("enter between 1 and 6")
            # win and loss are keeping track
            win = 0
            loss = 0
            # for loop is used for generating dice number
            for i in range(play):
                rand = np.random.rand(0, 7)
                if rand == dice:
                    amount = amount * 2
                    win += 1
                else:
                    amount = amount / 2
                    loss += 1
                # below number of win and losses are printed
                print("after round 1 total amount is ", amount)
            print("total amount won is ", amount)
            print("number of wins are ", win, "and number of losses are ", loss)
    except ValueError:
            print("check the input ")
if __name__ == '__main__':
                    try:  # try is used for catching any error
                        amount = int(input("amount :"))
                        if amount <= 0 or amount >= 1000:
                            print("enter the number between 0 and 1000")
                        caller=GamblerSimulation()
                        caller.Gambler(amount)
                    except ValueError:
                        print("check the input")