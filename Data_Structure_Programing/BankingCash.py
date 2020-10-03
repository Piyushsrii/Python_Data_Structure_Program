'''Desc -> Create a Program which creates Banking Cash Counter where people
come in to deposit Cash and withdraw Cash. Have an input panel to add people
to Queue to either deposit or withdraw money and dequeue the people. Maintain
the Cash Balance.'''
class Queue:

    #this method set balance 0
    def __init__(self):
        '''
                  :param:self: By default value generated
                  :return:this show the banking portal
                  '''
        self.balance = 0
        print("Welcome .....")
        print("This is a Banking portal")

    # this method for deposit the money
    def enqueue_deposit(self):
        '''
                  :param:self: By default value generated
                  :return:the deposit money
                  '''
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\nAmount Deposited:", amount)

    #this method for withDraw the monney
    def dequeue_withdraw(self):
        '''
               :param:self: By default value generated
               :return:return return the withdraw money
               '''
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\nYou Withdrew:", amount)
        else:
            print("\nInsufficient balance ")

    #this method for dispaly the amount
    def queue_display(self):
        '''
                  :param:self: By default value generated
                  :return:return didplay the balnced
                  '''
        print("\nNet Available Balance=", self.balance)

    # this method for exit the queue
    def queue_exit(self):
        '''
                  :param:self: By default value generated
                  :return:return this for the exist the queue
                  '''
        exit()

if __name__ == '__main__':
    q = Queue()
    try:
        while True:
            print("Please Enter the option that you want to make a transaction:")
            n = int(input(
                " Press \n 1. Deposite Amount to the account \n 2. Withdraw Amount from the account \n 3. Display the amount \n 4. Cancel Transaction \n"))
            if n == 1:
                q.enqueue_deposit()
            elif n == 2:
                q.dequeue_withdraw()
            elif n == 3:
                q.queue_display()
            elif n == 4:
                q.queue_exit()
    except ValueError:
        print("Enter the Proper Option")
    except KeyboardInterrupt:
        print("Force Quit!")
        print("Bye!")